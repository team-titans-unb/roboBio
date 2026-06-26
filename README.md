# roboBio

Repositório: [github.com/team-titans-unb/roboBio](https://github.com/team-titans-unb/roboBio)

> **Documentação do projeto:** o plano de trabalho da Iniciação Científica (ProIC/UnB) está em [`plano-de-trabalho/`](./plano-de-trabalho/README.md), junto com o PDF original.

Controle dos **servos de direção** (180°) de um robô de **seis rodas** via **Raspberry Pi** e placa **PCA9685** (Adafruit).

Cada roda tem:

| Peça | Função | Controle |
|------|--------|----------|
| Servo 180° (canais 0–5) | **Direção** — gira o conjunto da roda | Este repositório |
| Servo 90° (motor 6) | Curso menor — calibrar com `g0`/`g9`/`g1` | `calibrate_servos.py` |
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

## Referência rápida de comandos

Ative o venv uma vez por sessão: `source venv/bin/activate`

### Controle (`servo_pca9685.py`)

| Comando | O que faz |
|---------|-----------|
| `./venv/bin/python servo_pca9685.py 90` | Frota reta (usa calibração JSON) |
| `./venv/bin/python servo_pca9685.py 0` | Frota em 0° |
| `./venv/bin/python servo_pca9685.py 180` | Frota em 180° |
| `./venv/bin/python servo_pca9685.py -c 5 120` | Só motor 6 (canal 5) |
| `./venv/bin/python servo_pca9685.py --sweep` | Varredura 0→180→0 (todos) |
| `./venv/bin/python servo_pca9685.py --no-calibration 90` | Ignora JSON |

### Calibração (`calibrate_servos.py`)

| Comando / tecla | O que faz |
|-----------------|-----------|
| `./venv/bin/python calibrate_servos.py --motor 6` | Calibrar motor 6 |
| `+` / `-` | Ajusta ±1° |
| `g0` | Grava posição = frota **0°** |
| `g9` ou `c` | Grava posição = frota **90°** (reto) |
| `g1` | Grava posição = frota **180°** |
| `f0` / `f9` / `f1` | Testa frota inteira em 0 / 90 / 180 |
| `v` | Varredura do motor atual |
| `p` | Mostra tabela 0/90/180 de todos |
| `s` | Salva `servo_calibration.json` |
| `m` | Troca de motor |
| `q` | Sair |

### Primeira calibração na Pi

```bash
cp servo_calibration.json.example servo_calibration.json   # opcional
./venv/bin/python calibrate_servos.py --motor 6
# g0 → g9 → g1 → f9 → s
./venv/bin/python servo_pca9685.py 90
```

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

- `servo_pca9685.py 90` → cada motor usa as posições calibradas (`positions` 0 / 90 / 180).
- Copie o exemplo: `cp servo_calibration.json.example servo_calibration.json` ou calibre com `calibrate_servos.py`.

---

## Calibração interativa (`calibrate_servos.py`)

Grava **três posições por motor**: onde ele fica quando a frota recebe **0°, 90° e 180°**.

```bash
./venv/bin/python calibrate_servos.py
./venv/bin/python calibrate_servos.py --motor 6
```

### Fluxo sugerido (ex. motor 6 — servo 90°)

1. `./venv/bin/python calibrate_servos.py --motor 6`
2. **`v`** — varredura; anote onde trava.
3. Alinhe visualmente com a frota em **0°** → **`g0`**
4. Alinhe **reto (90° de frota)** → **`g9`**
5. Alinhe **180° de frota** → **`g1`**
6. **`f0`**, **`f9`**, **`f1`** — testa todos os motores nos três pontos.
7. **`s`** — salva o JSON.

### Comandos do menu

| Tecla | Ação |
|-------|------|
| `+` / `-` | ±1° |
| `++` / `--` | ±5° |
| `0` `9` `1` | Jog manual 0° / 90° / 180° |
| `v` | Varredura |
| **`g0`** | Gravar posição = frota **0°** |
| **`g9`** / **`c`** | Gravar = frota **90°** |
| **`g1`** | Gravar = frota **180°** |
| **`f0`** **`f9`** **`f1`** | Frota inteira em 0 / 90 / 180 |
| `a` | Frota 90° nos outros; este no jog atual |
| `p` | Tabela 0/90/180 de todos |
| `s` | Salvar arquivo |
| `m` | Trocar motor |
| `q` | Sair |

### Formato de `servo_calibration.json`

```json
{
  "version": 2,
  "channels": {
    "5": {
      "positions": { "0": 55, "90": 90, "180": 125 },
      "invert": true,
      "min_limit": 45,
      "max_limit": 135
    }
  }
}
```

- **`positions`**: ângulo lógico em frota 0 / 90 / 180 (valores intermediários são interpolados).
- **`min_limit` / `max_limit`**: limite físico (útil no servo 90° do motor 6).

O arquivo fica na Pi (`gitignore`). Veja `servo_calibration.json.example`.

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
| Motor 6 desalinhado | `calibrate_servos.py --motor 6` → `g0` `g9` `g1` → `s` |
| Quer ignorar calibração | `servo_pca9685.py --no-calibration 90` |

---

## Licença

Uso do projeto Seguidor / roboBio — ajuste conforme o repositório principal.
