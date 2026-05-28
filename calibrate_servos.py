#!/usr/bin/env python3
"""
Calibração interativa dos servos de direção (motores 1–6 / canais 0–5).

Salva neutro individual em servo_calibration.json. Quando todos recebem
comando 90° (reto), cada motor usa o neutro calibrado — ex. motor 6 em 110°.

Uso na Raspberry:
  ./venv/bin/python calibrate_servos.py
  ./venv/bin/python calibrate_servos.py --motor 6
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import servo_config as sc
from servo_config import DEFAULT_CONFIG_PATH, SERVO_CHANNELS, motor_label

import servo_pca9685 as sp


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Calibração interativa dos servos")
    p.add_argument(
        "--motor",
        type=int,
        choices=range(1, 7),
        help="Começar direto no motor 1–6",
    )
    p.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Arquivo JSON de calibração",
    )
    p.add_argument("--bus", type=int, default=None)
    p.add_argument("--address", type=lambda x: int(x, 0), default=None)
    return p.parse_args()


def print_help() -> None:
    print(
        """
Comandos:
  + / -     ±1° no motor em calibração
  ++ / --   ±5°
  0 9 1     Atalhos: 0°, 90°, 180° (só este motor)
  v         Varredura lenta 0° → 180° → 0° (só este motor)
  c         Definir posição ATUAL como neutro (centro calibrado)
  a         Testar ALINHAMENTO: todos em 90° de frota (com calibração)
  t         Testar posição de frota digitada (padrão 90)
  p         Mostrar neutros salvos
  s         Salvar em servo_calibration.json
  m         Escolher outro motor
  q         Sair (pergunta se salva)
"""
    )


def choose_motor() -> int:
    print("\nEscolha o motor (1–6):")
    for ch in SERVO_CHANNELS:
        print(f"  {ch + 1} → canal {ch}")
    while True:
        raw = input("Motor: ").strip()
        if raw.lower() in ("q", "sair"):
            raise SystemExit(0)
        try:
            num = int(raw)
            if 1 <= num <= 6:
                return num - 1
        except ValueError:
            pass
        print("Digite um número de 1 a 6.")


def sweep_one(pca, channel: int, config: dict, step: int = 5, delay: float = 0.06) -> None:
    print(f"Varredura {motor_label(channel)}...")
    for angle in range(0, 181, step):
        sp.set_servo_from_config(pca, channel, float(angle), config)
        time.sleep(delay)
    for angle in range(180, -1, -step):
        sp.set_servo_from_config(pca, channel, float(angle), config)
        time.sleep(delay)
    print("Varredura concluída.")


def apply_fleet_pose(
    pca,
    config: dict,
    fleet_angle: float,
    hold_channel: int | None = None,
    hold_logical: float | None = None,
) -> None:
    """Todos na pose de frota; opcionalmente um canal em ângulo manual."""
    for ch in SERVO_CHANNELS:
        if hold_channel is not None and ch == hold_channel and hold_logical is not None:
            logical = hold_logical
        else:
            logical = sc.fleet_to_logical(config, ch, fleet_angle)
        sp.set_servo_from_config(pca, ch, logical, config)
        time.sleep(sp.STAGGER_S)


def print_status(channel: int, logical: float, config: dict) -> None:
    entry = sc.get_channel(config, channel)
    hw = sc.map_to_hardware(config, channel, logical)
    fleet_neutral = float(config["fleet_neutral"])
    print(
        f"\n{motor_label(channel)} | lógico: {logical:5.1f}° | hardware: {hw:5.1f}° | "
        f"neutro salvo: {entry['neutral']:.1f}° | "
        f"offset frota 90°: {entry['neutral'] - fleet_neutral:+.1f}°",
    )


def calibration_loop(
    pca,
    config: dict,
    config_path: Path,
    start_channel: int | None,
) -> None:
    channel = start_channel if start_channel is not None else choose_motor()
    entry = sc.get_channel(config, channel)
    logical = float(entry["neutral"])
    dirty = False

    print_help()
    print_status(channel, logical, config)

    while True:
        cmd = input("> ").strip().lower()
        if not cmd:
            continue

        if cmd in ("q", "quit", "sair"):
            if dirty:
                save = input("Salvar calibração antes de sair? [S/n]: ").strip().lower()
                if save in ("", "s", "sim", "y", "yes"):
                    sc.save_config(config, config_path)
                    print(f"Salvo em {config_path}")
            break

        if cmd == "m":
            channel = choose_motor()
            entry = sc.get_channel(config, channel)
            logical = float(entry["neutral"])
            print_status(channel, logical, config)
            continue

        if cmd in ("h", "?"):
            print_help()
            continue

        if cmd == "+":
            logical = min(180.0, logical + 1.0)
        elif cmd == "-":
            logical = max(0.0, logical - 1.0)
        elif cmd == "++":
            logical = min(180.0, logical + 5.0)
        elif cmd == "--":
            logical = max(0.0, logical - 5.0)
        elif cmd == "0":
            logical = 0.0
        elif cmd in ("9", "90"):
            logical = float(config["fleet_neutral"])
        elif cmd in ("1", "180"):
            logical = 180.0
        elif cmd == "v":
            sweep_one(pca, channel, config)
            continue
        elif cmd == "c":
            entry["neutral"] = round(logical, 1)
            dirty = True
            print(f"Neutro de {motor_label(channel)} definido em {entry['neutral']:.1f}°")
            print_status(channel, logical, config)
            continue
        elif cmd == "a":
            print("Alinhamento: todos na frota 90°; este motor na posição atual.")
            apply_fleet_pose(
                pca,
                config,
                float(config["fleet_neutral"]),
                hold_channel=channel,
                hold_logical=logical,
            )
            print("Observe se está alinhado com os outros. Ajuste com +/- e use 'c' para salvar neutro.")
            continue
        elif cmd == "t":
            raw = input("Ângulo de frota para testar [90]: ").strip()
            fleet = float(raw) if raw else float(config["fleet_neutral"])
            apply_fleet_pose(
                pca,
                config,
                fleet,
                hold_channel=channel,
                hold_logical=logical,
            )
            print(f"Frota em {fleet:.0f}° aplicada.")
            continue
        elif cmd == "p":
            print("\nNeutros calibrados (frota neutro = {:.0f}°):".format(config["fleet_neutral"]))
            for ch in SERVO_CHANNELS:
                e = sc.get_channel(config, ch)
                off = e["neutral"] - float(config["fleet_neutral"])
                print(
                    f"  {motor_label(ch)}: neutro={e['neutral']:.1f}° "
                    f"offset={off:+.1f}° invert={e['invert']} trim={e['trim']:+.1f}",
                )
            continue
        elif cmd == "s":
            sc.save_config(config, config_path)
            dirty = False
            print(f"Salvo em {config_path}")
            continue
        elif cmd == "i":
            raw = input("Inverter este motor? [s/N]: ").strip().lower()
            entry["invert"] = raw in ("s", "sim", "y", "yes")
            dirty = True
            print(f"Invert={entry['invert']}")
            continue
        else:
            print("Comando desconhecido. Use h para ajuda.")
            continue

        sp.set_servo_from_config(pca, channel, logical, config)
        print_status(channel, logical, config)


def main() -> None:
    args = parse_args()
    config_path = args.config
    config = sc.load_config(config_path)
    sc.apply_runtime_globals(config)

    bus = args.bus if args.bus is not None else int(config["i2c_bus"])
    address = args.address if args.address is not None else int(config["i2c_address"])

    try:
        pca = sp.create_pca9685(bus, address)
    except (ImportError, OSError, RuntimeError) as e:
        print(f"Erro ao abrir PCA9685: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Calibração roboBio | i2c-{bus} | 0x{address:02x}")
    print(f"Arquivo: {config_path}")

    start_ch = (args.motor - 1) if args.motor else None
    try:
        calibration_loop(pca, config, config_path, start_ch)
    finally:
        pca.deinit()
        print("PWM liberado.")


if __name__ == "__main__":
    main()
