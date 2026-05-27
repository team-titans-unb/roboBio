#!/usr/bin/env python3
"""
Controle de servos via PCA9685 (Adafruit CircuitPython).

Motores do projeto: canais 0 a 5 (6 servos).

Ligação:
  Pi 3.3V -> VCC | SDA -> SDA | SCL -> SCL | GND -> GND
  Fonte 5V -> V+ e GND do terminal verde (servos)
  Servos nos canais PWM 0, 1, 2, 3, 4, 5

Uso:
  ./venv/bin/python servo_pca9685.py 90              # todos 0–5 em 90°
  ./venv/bin/python servo_pca9685.py --angles 0,45,90,90,45,0
  ./venv/bin/python servo_pca9685.py -c 2 45         # só canal 2
  ./venv/bin/python servo_pca9685.py --sweep         # varre todos 0–5 juntos
  ./venv/bin/python servo_pca9685.py --sweep -c 0    # varre só canal 0
"""

from __future__ import annotations

import argparse
import os
import sys
import time

PULSE_MIN_US = 500
PULSE_MAX_US = 2500
SERVO_PERIOD_US = 20_000
SERVO_HZ = 50
DEFAULT_I2C_BUS = 1
DEFAULT_ADDRESS = 0x40

# Motores do robô (PCA9685 canais 0–5)
SERVO_FIRST = 0
SERVO_LAST = 5
SERVO_CHANNELS = list(range(SERVO_FIRST, SERVO_LAST + 1))
STAGGER_S = 0.01  # atraso entre canais (reduz pico de corrente)


def angle_to_duty(
    angle: float,
    min_us: int = PULSE_MIN_US,
    max_us: int = PULSE_MAX_US,
) -> int:
    angle = max(0.0, min(180.0, float(angle)))
    pulse_us = min_us + (angle / 180.0) * (max_us - min_us)
    return int((pulse_us / SERVO_PERIOD_US) * 65535)


def setup_blinka_i2c_bus(bus: int) -> None:
    os.environ["BLINKA_I2C_ADAPTER"] = str(bus)


def create_pca9685(bus: int, address: int):
    setup_blinka_i2c_bus(bus)
    import board  # noqa: WPS433
    from adafruit_pca9685 import PCA9685  # noqa: WPS433

    i2c = board.I2C()
    pca = PCA9685(i2c, address=address)
    pca.frequency = SERVO_HZ
    return pca


def set_servo(
    pca,
    channel: int,
    angle: float,
    min_us: int = PULSE_MIN_US,
    max_us: int = PULSE_MAX_US,
) -> None:
    if channel < 0 or channel > 15:
        raise ValueError(f"Canal inválido: {channel} (use 0–15)")
    pca.channels[channel].duty_cycle = angle_to_duty(angle, min_us, max_us)


def set_servos(
    pca,
    angles_by_channel: dict[int, float],
    min_us: int = PULSE_MIN_US,
    max_us: int = PULSE_MAX_US,
    stagger: bool = True,
) -> None:
    channels = sorted(angles_by_channel.keys())
    for i, channel in enumerate(channels):
        set_servo(pca, channel, angles_by_channel[channel], min_us, max_us)
        if stagger and i < len(channels) - 1:
            time.sleep(STAGGER_S)


def set_all_same_angle(
    pca,
    angle: float,
    channels: list[int] | None = None,
    min_us: int = PULSE_MIN_US,
    max_us: int = PULSE_MAX_US,
) -> None:
    chans = channels if channels is not None else SERVO_CHANNELS
    set_servos(
        pca,
        {ch: angle for ch in chans},
        min_us=min_us,
        max_us=max_us,
    )


def parse_angles_list(text: str) -> dict[int, float]:
    """Ex.: '0,45,90,90,45,0' -> {0:0, 1:45, ...} para canais 0–5."""
    parts = [p.strip() for p in text.split(",")]
    if len(parts) != len(SERVO_CHANNELS):
        raise ValueError(
            f"--angles precisa de {len(SERVO_CHANNELS)} valores "
            f"(canais {SERVO_FIRST}–{SERVO_LAST}), recebeu {len(parts)}",
        )
    return {ch: float(parts[i]) for i, ch in enumerate(SERVO_CHANNELS)}


def sweep_channel(
    pca,
    channel: int,
    step: int = 10,
    delay_s: float = 0.05,
    min_us: int = PULSE_MIN_US,
    max_us: int = PULSE_MAX_US,
) -> None:
    for angle in range(0, 181, step):
        set_servo(pca, channel, angle, min_us, max_us)
        time.sleep(delay_s)
    for angle in range(180, -1, -step):
        set_servo(pca, channel, angle, min_us, max_us)
        time.sleep(delay_s)


def sweep_channels(
    pca,
    channels: list[int],
    step: int = 10,
    delay_s: float = 0.05,
    min_us: int = PULSE_MIN_US,
    max_us: int = PULSE_MAX_US,
) -> None:
    """Todos os canais no mesmo ângulo a cada passo (movimento sincronizado)."""
    for angle in range(0, 181, step):
        set_servos(
            pca,
            {ch: float(angle) for ch in channels},
            min_us=min_us,
            max_us=max_us,
        )
        time.sleep(delay_s)
    for angle in range(180, -1, -step):
        set_servos(
            pca,
            {ch: float(angle) for ch in channels},
            min_us=min_us,
            max_us=max_us,
        )
        time.sleep(delay_s)


def format_angles(angles: dict[int, float]) -> str:
    return ", ".join(f"{ch}:{angles[ch]:.0f}°" for ch in sorted(angles))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Servos 0–5 na PCA9685 (adafruit_pca9685)",
    )
    parser.add_argument(
        "angle",
        nargs="?",
        type=float,
        help="Ângulo 0–180 para todos os motores 0–5 (ou um canal com -c)",
    )
    parser.add_argument(
        "--angles",
        type=str,
        metavar="LIST",
        help="Ângulos por canal: 6 valores para 0,1,2,3,4,5 (ex.: 0,45,90,90,45,0)",
    )
    parser.add_argument(
        "-c",
        "--channel",
        type=int,
        default=None,
        help="Controlar só este canal (0–15). Sem -c: motores 0–5",
    )
    parser.add_argument(
        "--sweep",
        action="store_true",
        help="Varre 0°–180°–0° (todos 0–5, ou só -c se informado)",
    )
    parser.add_argument(
        "--bus",
        type=int,
        default=DEFAULT_I2C_BUS,
        help=f"Barramento I2C (padrão: {DEFAULT_I2C_BUS})",
    )
    parser.add_argument(
        "--address",
        type=lambda x: int(x, 0),
        default=DEFAULT_ADDRESS,
        help="Endereço I2C (padrão: 0x40)",
    )
    parser.add_argument("--min-us", type=int, default=PULSE_MIN_US)
    parser.add_argument("--max-us", type=int, default=PULSE_MAX_US)
    parser.add_argument(
        "--release",
        action="store_true",
        help="Para PWM ao sair (deinit)",
    )
    return parser.parse_args()


def resolve_target_channels(args: argparse.Namespace) -> list[int]:
    if args.channel is not None:
        return [args.channel]
    return SERVO_CHANNELS.copy()


def main() -> None:
    args = parse_args()
    targets = resolve_target_channels(args)

    if not args.sweep and args.angle is None and args.angles is None:
        print(
            "Informe um ângulo, --angles ou --sweep.\n"
            "  Ex.: servo_pca9685.py 90\n"
            "  Ex.: servo_pca9685.py --angles 0,45,90,90,45,0",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.angles is not None and args.channel is not None:
        print("Use --angles OU -c, não os dois.", file=sys.stderr)
        sys.exit(1)

    try:
        pca = create_pca9685(args.bus, args.address)
    except ImportError:
        print(
            "Bibliotecas Adafruit não instaladas.\n"
            "  ./venv/bin/pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)
    except (OSError, ValueError, RuntimeError) as e:
        print(f"Erro ao abrir PCA9685: {e}", file=sys.stderr)
        sys.exit(1)

    label = (
        f"canal {args.channel}"
        if args.channel is not None
        else f"motores {SERVO_FIRST}–{SERVO_LAST}"
    )
    print(
        f"PCA9685 0x{args.address:02x} | i2c-{args.bus} | {label} | {SERVO_HZ} Hz",
    )

    try:
        if args.sweep:
            if args.channel is not None:
                print(f"Varredura canal {args.channel}...")
                sweep_channel(
                    pca,
                    args.channel,
                    min_us=args.min_us,
                    max_us=args.max_us,
                )
            else:
                print(f"Varredura motores {SERVO_FIRST}–{SERVO_LAST} (sincronizado)...")
                sweep_channels(
                    pca,
                    SERVO_CHANNELS,
                    min_us=args.min_us,
                    max_us=args.max_us,
                )
            print("Pronto.")
            return

        if args.angles is not None:
            try:
                angles_map = parse_angles_list(args.angles)
            except ValueError as e:
                print(e, file=sys.stderr)
                sys.exit(1)
            set_servos(
                pca,
                angles_map,
                min_us=args.min_us,
                max_us=args.max_us,
            )
            print(format_angles(angles_map))
            return

        if args.channel is not None:
            set_servo(
                pca,
                args.channel,
                args.angle,
                min_us=args.min_us,
                max_us=args.max_us,
            )
            print(f"Canal {args.channel} -> {args.angle:.0f}°")
        else:
            set_all_same_angle(
                pca,
                args.angle,
                channels=targets,
                min_us=args.min_us,
                max_us=args.max_us,
            )
            print(f"Motores {SERVO_FIRST}–{SERVO_LAST} -> {args.angle:.0f}°")

        if not args.release:
            time.sleep(0.5)
    finally:
        if args.release:
            pca.deinit()
            print("PWM liberado (deinit).")


if __name__ == "__main__":
    main()
