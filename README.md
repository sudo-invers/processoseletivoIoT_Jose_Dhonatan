## Relatório do Candidato

**Nome completo:** Jose Dhonatan Fernandes de Almeida  
**GitHub:** [sudoinvers](https://github.com/sudo-invers)

# Visão Geral

Este projeto implementa um cyber pet virtual (estilo Tamagotchi) utilizando MicroPython em um ESP32 simulado no Wokwi.

O objetivo é demonstrar um sistema embarcado IoT com:

- comportamento baseado em estados  
- atualizações periódicas por temporização  
- interação do usuário via botões físicos  
- feedback visual em display OLED  

O sistema simula um pet digital cujo estado muda ao longo do tempo.

### Interação do usuário

O usuário interage por três botões:

```
| Botão | Função |
|------|--------|
| Feed | Reduz fome |
| Play | Aumenta felicidade |
| Sleep | Recupera energia |
```
O display OLED exibe humor e status do pet.

---

# Arquitetura do Sistema Embarcado

## Fluxo principal (`main.py`)

```
Inicialização
↓
Criar Pet
Criar Botões
Inicializar OLED
↓
Loop principal
├── Atualizar pet a cada 3 segundos
├── Ler botões
├── Executar ação
└── Atualizar display
```

## Estrutura modular

```
src/
├── main.py
├── pet.py
├── buttons.py
├── display.py
└── ssd1306.py
```

### Responsabilidades

- **main.py** → fluxo principal do firmware  
- **pet.py** → lógica e estados do pet  
- **buttons.py** → leitura dos inputs
- **display.py** → interface OLED  
- **ssd1306.py** → driver do display  

## Temporização

O sistema utiliza temporização baseado em ticks
"1 tick = 1 milisegundo"

```python
time.ticks_ms()
time.ticks_diff()
```

Intervalo de atualização:

```
3000 ticks = 3000 ms
```

# 3. Componentes Utilizados

## Placa

- ESP32 DevKit C V4

## Periféricos

### Display OLED SSD1306

Conexões:

```
GPIO21 → SDA
GPIO22 → SCL
```

Função:

- exibir humor  
- mostrar status  
- interface visual do pet

---

## Botões

```text
GPIO14 → Feed
GPIO27 → Play
GPIO26 → Sleep
```

Função:

- entrada do usuário

# Decisões Técnicas Relevantes

## Organização modular

Separação por responsabilidade para facilitar:

- manutenção  
- testes  
- escalabilidade

## Debounce

Implementado com:

```python
250ms debounce
```

para evitar múltiplas leituras de botão.

## Pipeline CI

Integração com:

- GitHub Actions  
- Wokwi CI

Validação automática de:

- build do filesystem  
- boot do firmware  
- execução da simulação

# 5. Resultados Obtidos

## Funcionalidades implementadas

- Simulação do cyber pet  
- Atualização automática dos estados  
- Interação por botões  
- Exibição em OLED  
- Execução no Wokwi  
- Build automatizado do filesystem  
- Integração com CI

## Oque o sistema faz

O sistema:

- degrada estados com o tempo  
- responde a ações do usuário  
- altera humor conforme condições  
- atualiza visualmente o display

# 6. Comentários Adicionais

## Dificuldades encontradas

Principais desafios:

- Configurar e utilizar o SSD1306, para usar a OLED
- ajustar integração Wokwi + GitHub Actions
- compatibilidade do OLED na simulação

## O que fazer para o futuro

TODO:

- persistência do estado  
- evolução do pet  
- sprites animados
- ampliar covertura de testes

## Principais aprendizados

Este projeto reforçou:

- modularização de firmware  
- integração hardware/software
- empacotamento para ESP32  
- testes de CI para embarcados
- uso de MicroPython em sistemas simulados

## Estrutura do Projeto

```
.
├── binaries
│   ├── bootloader.bin
│   ├── micropython.bin
│   └── partition-table.bin
├── diagram.json
├── Dockerfile
├── flasher_args.json
├── README.md
├── requirements.txt
├── src
│   ├── buttons.py
│   ├── display.py
│   ├── main.py
│   ├── pet.py
│   └── ssd1306.py
└── wokwi.toml

```

## Simulação

Executado com:

- ESP32 + MicroPython  
- Wokwi Simulator  
- SSD1306 OLED  
- Push Buttons

## Autor

Jose Dhonatan Fernandes de Almeida
GitHub: https://github.com/sudoinvers

## Agradecimentos
Agradeço ao time do Pnaat, pelo prazer de realizar esse projeto, e pelos ensinamentos que me foram dados para que conseguisse fazer. Agradeço também, ao pipeline de CI que me foi fornecido
