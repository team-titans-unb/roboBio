# roboBio

Repositório: [github.com/team-titans-unb/roboBio](https://github.com/team-titans-unb/roboBio)

Controle dos **servos de direção** (180°) de um robô de seis rodas via **Raspberry Pi** e placa **PCA9685**.

Cada conjunto de roda usa:

- **Servo 180°** (canais 0–5 na PCA9685) — vira o eixo de direção; neutro em **90°**
- **Motor de rotação contínua** (no cubo da roda) — tração; controle à parte (futuro)

## Hardware

| Item | Detalhe |
|------|---------|
| Raspberry Pi | SSH, I2C habilitado (`/dev/i2c-1` na Pi testada) |
| PCA9685 | Endereço `0x40`, 50 Hz |
| Servos de direção | Canais **PWM 0 a 5** |
| Alimentação | 3,3 V no **VCC** da placa; **5 V externo** no **V+** (servos) |
| GND | Comum entre Pi, placa e fonte 5 V |

### Ligação I2C (GPIO)

| Pi | PCA9685 |
|----|---------|
| 3,3 V (pino 1) | VCC |
| SDA (pino 3) | SDA |
| SCL (pino 5) | SCL |
| GND | GND |

### Calibração mecânica

- **Repouso:** todos os servos de direção em **90°** (rodas retas).
- Braço em C do motor contínuo: montar **para fora** (rodas afastadas do centro do robô).
- Canais espelhados na montagem podem precisar de inversão no software (controle remoto — futuro).

## Requisitos na Raspberry Pi

- Raspberry Pi OS com I2C
- Python 3.11+

## Instalação

Na Pi (clone ou cópia desta pasta em `~/roboBio`):

```bash
cd ~/roboBio
bash setup_pi.sh
sudo reboot   # após habilitar I2C (primeira vez)
```

Depois do reboot:

```bash
cd ~/roboBio
source venv/bin/activate
sudo i2cdetect -y 1    # deve aparecer 40 na linha 40:
```

> O Pi OS bloqueia `pip install` no sistema; o `setup_pi.sh` cria o **venv** local.

## Uso

Sempre com o venv ativo ou `./venv/bin/python`:

```bash
# Todos os servos 0–5 no mesmo ângulo (neutro / teste)
./venv/bin/python servo_pca9685.py 90

# Ângulo individual por canal (0,1,2,3,4,5)
./venv/bin/python servo_pca9685.py --angles 90,90,90,90,90,90

# Um canal só
./venv/bin/python servo_pca9685.py -c 2 120

# Varredura 0° → 180° → 0° (todos sincronizados)
./venv/bin/python servo_pca9685.py --sweep

# Varredura de um canal
./venv/bin/python servo_pca9685.py --sweep -c 0
```

### Opções úteis

| Opção | Descrição |
|-------|-----------|
| `--bus 1` | Barramento I2C (padrão: `1`) |
| `--address 0x40` | Endereço da PCA9685 |
| `--min-us` / `--max-us` | Ajuste de pulso (ex. SG90: 1000–2000) |
| `--release` | Para PWM ao sair (`deinit`) |

## Enviar código do PC para a Pi

```bash
scp -r roboBio bio@seguidor.local:~/
# ou só o script atualizado:
scp roboBio/servo_pca9685.py bio@seguidor.local:~/roboBio/
```

## Estrutura do repositório

```
roboBio/
├── README.md           # Este arquivo
├── .gitignore
├── requirements.txt    # adafruit-blinka, adafruit-circuitpython-pca9685
├── setup_pi.sh         # venv + I2C na Raspberry
└── servo_pca9685.py    # CLI — servos de direção 0–5
```

## Próximos passos

- [ ] Controle remoto (mapear eixo → ângulo com neutro 90°)
- [ ] Driver dos motores de rotação contínua (tração)
- [ ] Constantes de inversão por canal (`CHANNEL_INVERT`)
- [ ] Integração com câmera / visão (seguir alvo)

## Solução de problemas

| Problema | Ação |
|----------|------|
| `externally-managed-environment` | Use `bash setup_pi.sh` e `./venv/bin/python` |
| `/dev/i2c-1` não existe | `sudo raspi-config` → I2C → Enable → reboot |
| `i2cdetect` sem `40` | Fios SDA/SCL/GND, 3,3 V no VCC, fonte 5 V no V+ |
| Script OK, servo não mexe | Fonte 5 V nos servos; cabo no canal correto |
| `No Hardware I2C` (Blinka) | Use `--bus 1`; confira `sudo i2cdetect -y 1` |

## Licença

Uso do projeto Seguidor / roboBio — ajuste conforme o repositório principal.
