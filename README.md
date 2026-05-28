# roboBio

Repositório: [github.com/team-titans-unb/roboBio](https://github.com/team-titans-unb/roboBio)

Controle dos **servos de direção** (180°) de um robô de **seis rodas** via **Raspberry Pi** e placa **PCA9685** (Adafruit).

Cada roda tem:

| Peça | Função | Controle |
|------|--------|----------|
| Servo 180° (canais 0–5) | **Direção** — gira o conjunto da roda | Este repositório |
| Motor rotação contínua (no cubo) | **Tração** — frente/ré | Futuro (outro driver) |

**Neutro de direção:** com todos em “reto”, use `90°` de frota. O motor 6 (ou outro) pode precisar de neutro diferente — use `calibrate_servos.py`.

### Motores × canais na PCA9685

| Motor (nome) | Canal PWM |
|--------------|-----------|
| Motor 1 | 0 |
| Motor 2 | 1 |
| Motor 3 | 2 |
| Motor 4 | 3 |
| Motor 5 | 4 |
| Motor 6 | 5 |

---

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

### Montagem mecânica

- Braço em C do motor contínuo: montar **para fora** (rodas afastadas do centro do robô).
- Com o horn em **90°**, a roda deve ficar **reta** em relação ao robô.

### Espelhamento esquerda / direita

Os lados do chassi são espelhados: o mesmo ângulo no código pode virar a roda “para trás” de um lado e “para frente” do outro.

| Canais | Lado (padrão) | Software |
|--------|---------------|----------|
| 0, 1, 2 | Esquerda | Sem inverter |
| 3, 4, 5 | Direita | `180 - ângulo` |

Teste: `./venv/bin/python servo_pca9685.py 0` e `180` — os seis devem apontar para o **mesmo lado** do robô.

Ajuste em `servo_calibration.json` (`"invert": true/false`) ou no código / após `calibrate_servos.py` (comando `i`).

---

## Instalação na Raspberry Pi

```bash
cd ~/roboBio
bash setup_pi.sh
sudo reboot   # primeira vez, após habilitar I2C
```

Depois do reboot:

```bash
cd ~/roboBio
source venv/bin/activate
sudo i2cdetect -y 1    # deve aparecer 40 na linha 40:
./venv/bin/pip install -r requirements.txt   # se ainda não instalou no venv
```

> O Pi OS bloqueia `pip install` no sistema; use sempre o **venv** (`setup_pi.sh` cria `./venv`).

---

## Uso rápido (`servo_pca9685.py`)

Sempre com venv: `source venv/bin/activate` ou `./venv/bin/python`.

```bash
# Todos em 90° de frota (reto) — usa servo_calibration.json se existir
./venv/bin/python servo_pca9685.py 90

# Todos em 0° ou 180° (mesma direção física, com inversão L/R)
./venv/bin/python servo_pca9685.py 0
./venv/bin/python servo_pca9685.py 180

# Um motor só (ex. canal 5 = motor 6)
./venv/bin/python servo_pca9685.py -c 5 120

# Seis ângulos explícitos (motores 1–6 / canais 0–5)
./venv/bin/python servo_pca9685.py --angles 90,90,90,90,90,110

# Varredura sincronizada 0° → 180° → 0°
./venv/bin/python servo_pca9685.py --sweep

# Só um canal
./venv/bin/python servo_pca9685.py --sweep -c 0
```

### Opções da CLI

| Opção | Descrição |
|-------|-----------|
| `--bus 1` | Barramento I2C (padrão: `1`) |
| `--address 0x40` | Endereço da PCA9685 |
| `--min-us` / `--max-us` | Pulso PWM (ex. SG90: `1000`–`2000`) |
| `--trim 5:-5` | Ajuste fino em graus no canal (pode repetir) |
| `--nudge 5:20` | Move **só** o canal 5 de 0° + 20° (teste rápido) |
| `--raw` | Sem inversão L/R (só diagnóstico) |
| `--no-fleet` | Mesmo número em todos os canais, **sem** offset de neutro do JSON |
| `--no-calibration` | Ignora `servo_calibration.json` |
| `--release` | Para PWM ao sair (`deinit`) |

### Calibração automática (arquivo JSON)

Com `servo_calibration.json` na pasta:

- `servo_pca9685.py 90` → cada motor usa seu **neutro** salvo (ex. motor 6 em 110° quando a frota pede 90°).
- Copie o exemplo: `cp servo_calibration.json.example servo_calibration.json` e edite, ou gere com `calibrate_servos.py`.

---

## Calibração interativa (`calibrate_servos.py`)

Para quando um motor (ex. **motor 6**) para **antes** de alinhar com os outros em 90°:

```bash
./venv/bin/python calibrate_servos.py
./venv/bin/python calibrate_servos.py --motor 6
```

### Fluxo sugerido (ex. motor 6)

1. Escolha o motor **6** (canal 5).
2. **`v`** — varredura lenta 0° → 180° → 0° (vê o curso).
3. **`+`** / **`-`** — ajusta de 1° até ficar visualmente no meio.
4. **`a`** — põe **todos** em 90° de frota; este motor fica na posição que você está ajustando → compare com os outros.
5. **`c`** — define a posição atual como **neutro** desse motor.
6. **`s`** — grava `servo_calibration.json`.
7. **`q`** — sai.

### Comandos do menu

| Tecla | Ação |
|-------|------|
| `+` / `-` | ±1° no motor em calibração |
| `++` / `--` | ±5° |
| `0` | Ir para 0° |
| `9` | Ir para 90° (neutro de frota) |
| `1` | Ir para 180° |
| `v` | Varredura 0° → 180° → 0° |
| `c` | **Salvar neutro** = posição atual |
| `a` | **Testar alinhamento** — frota em 90°, este motor na posição atual |
| `t` | Testar outro ângulo de frota (ex. 0 ou 180) |
| `p` | Listar neutros salvos |
| `i` | Alternar inversão deste motor |
| `s` | Gravar arquivo JSON |
| `m` | Escolher outro motor |
| `h` | Ajuda |
| `q` | Sair (pergunta se salva) |

### Formato de `servo_calibration.json`

```json
{
  "fleet_neutral": 90,
  "channels": {
    "5": {
      "neutral": 110,
      "invert": true,
      "trim": 0
    }
  }
}
```

- **`fleet_neutral`**: ângulo quando você manda “todos em 90°” no `servo_pca9685.py`.
- **`neutral`** (por canal): onde **este** motor fica quando a frota está em `fleet_neutral`.
- **`invert`**: espelhamento esquerda/direita.
- **`trim`**: ajuste fino extra em graus (após inversão).

O arquivo é gerado na Pi e **não** vai para o Git (está no `.gitignore`). Use `servo_calibration.json.example` como referência.

---

## Enviar código do PC para a Pi

```bash
cd ~/Documentos/seguidor/versionamento
scp -r roboBio bio@seguidor.local:~/
```

Só arquivos alterados:

```bash
scp roboBio/servo_pca9685.py roboBio/calibrate_servos.py \
    roboBio/servo_config.py bio@seguidor.local:~/roboBio/
```

---

## Estrutura do repositório

```
roboBio/
├── README.md
├── .gitignore
├── requirements.txt
├── setup_pi.sh
├── servo_pca9685.py              # CLI principal
├── calibrate_servos.py           # Calibração interativa
├── servo_config.py               # Leitura/gravação do JSON
├── servo_calibration.json        # Gerado na Pi (local)
└── servo_calibration.json.example
```

---

## Próximos passos

- [ ] Controle remoto (eixo → ângulo de frota + neutros do JSON)
- [ ] Driver dos motores de rotação contínua (tração)
- [ ] Integração com câmera / visão

---

## Solução de problemas

| Problema | Ação |
|----------|------|
| `externally-managed-environment` | `bash setup_pi.sh` + `./venv/bin/python` |
| `/dev/i2c-1` não existe | `sudo raspi-config` → I2C → Enable → reboot |
| `i2cdetect -y 1` sem `40` | Fios SDA/SCL/GND; 3,3 V no VCC; 5 V no V+ |
| Script OK, servo não mexe | Fonte 5 V no terminal V+; servo no canal certo |
| `No Hardware I2C` (Blinka) | `--bus 1`; `sudo i2cdetect -y 1` |
| Esquerda/direita opostas em `0` | Inversão em JSON ou `calibrate_servos.py` → `i` |
| Motor 6 desalinhado em `90` | `calibrate_servos.py --motor 6` → ajustar → `c` → `s` |
| Quer ignorar calibração | `servo_pca9685.py --no-calibration 90` |

---

## Licença

Uso do projeto Seguidor / roboBio — ajuste conforme o repositório principal.
