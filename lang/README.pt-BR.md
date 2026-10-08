# 🐍 Jogo da Cobrinha (Python: Tkinter + Pygame)
>Um clássico Jogo da Cobrinha (Snake) feito em Python, implementado em duas versões: uma com Tkinter e outra com Pygame, com foco em lógica limpa e jogabilidade responsiva.

🌍 **Leia em outros idiomas:** [English](../README.md) | [Español](README.es.md)

![Apresentação do Projeto](../assets/preview.gif)

## 🎮 Visão Geral do Projeto

Este projeto implementa a experiência principal do Snake em uma grade de 25x25 como um aplicativo desktop. O mesmo jogo é desenvolvido de duas formas diferentes, para que você possa comparar como cada biblioteca lida com janelas, entrada do teclado, desenho e o loop do jogo:

| | 🖼️ Versão Tkinter | 🕹️ Versão Pygame |
|---|---|---|
| 📁 Local | [`tkinter/snake.py`](../tkinter/snake.py) | [`pygame/snake.py`](../pygame/snake.py) |
| 📦 Dependências | Nenhuma (biblioteca padrão) | `pygame` |
| 🎯 Controles | Setas do teclado | Setas ou `W` `A` `S` `D` |
| 🐣 Posição inicial | Fixa (área superior esquerda) | Aleatória |
| 🧮 Pontuação | ✅ Exibida no fim de jogo | ❌ Ainda não |
| 🧱 Colisão com a parede | Fim de jogo | Cobra e comida reiniciam automaticamente |
| 🪞 Colisão com o próprio corpo | ✅ Fim de jogo | ❌ Ainda não |
| 🔁 Reiniciar | Botão de reiniciar | Automático |
| 🏃 Loop do jogo | `window.after(100, draw)` | `while True` + `clock.tick(10)` |
| 🚧 Status | Completa | Versão inicial (em desenvolvimento) |

## 🖼️ Versão Tkinter

A versão original e mais completa, construída apenas com a biblioteca padrão do Python.

- ⚡ Movimento em tempo real com as setas do teclado (inverter a direção é bloqueado)
- 🍎 Geração de comida e crescimento da cobra
- 💥 Detecção de colisão (paredes e o próprio corpo)
- 🧮 Contagem de pontos
- 🔁 Tela de fim de jogo com botão de reiniciar
- 🪟 Janela centralizada na tela com tamanho de tabuleiro fixo

### 🧠 Notas de Arquitetura

- 🧩 Uma classe `Cell` para as posições no tabuleiro
- 🌐 Variáveis globais de estado do jogo (snake, food, score, velocity, game_over)
- 🏃 Uma função `move()` para as atualizações do jogo
- 🖌️ Um loop `draw()` agendado com `window.after(100, draw)` (10 atualizações por segundo)

## 🕹️ Versão Pygame

Uma versão mais recente que reconstrói o jogo usando o [Pygame](https://www.pygame.org/), uma biblioteca feita especificamente para jogos. Ainda é uma versão inicial e está sendo desenvolvida passo a passo.

- ⚡ Movimento com as setas ou `W` `A` `S` `D`
- 🍎 Geração de comida e crescimento da cobra
- 🎲 Cobra e comida começam em posições aleatórias
- 🧱 Sair do tabuleiro reinicia a cobra e a comida

### 🧠 Notas de Arquitetura

- 🟩 Objetos `pygame.Rect` para os segmentos da cobra e para a comida
- 🔄 Um loop de jogo clássico `while True` que trata eventos, atualizações e desenho
- ⏱️ `pygame.time.Clock` limita o jogo a 10 quadros por segundo
- 📐 `window.get_rect().contains(...)` verifica se a cobra está dentro do tabuleiro

## 🧰 Tecnologias

- Python 3
- Tkinter (biblioteca gráfica padrão do Python) 🖼️
- Pygame (biblioteca para desenvolvimento de jogos) 🕹️
- `random` (para posicionar a comida)

## 🚀 Como Executar

1. Certifique-se de que o Python 3 está instalado.
2. Abra a pasta do projeto.

### 🖼️ Versão Tkinter

Nenhuma dependência externa é necessária:

```bash
python tkinter/snake.py
```

### 🕹️ Versão Pygame

Instale o Pygame primeiro:

```bash
pip install pygame
```

Depois execute:

```bash
python pygame/snake.py
```

## 🎯 Controles

- ⬆️⬇️⬅️➡️ Setas do teclado: movem a cobra (ambas as versões)
- 🔤 `W` `A` `S` `D`: movem a cobra (versão Pygame)
- 🔄 Botão de reiniciar: aparece após o fim de jogo para começar uma nova partida (versão Tkinter)

## 📜 Regras Atuais do Jogo

### 🖼️ Versão Tkinter

- 🐣 A cobra começa perto da área superior esquerda do tabuleiro.
- 🍽️ Comer a comida aumenta a pontuação e faz a cobra crescer.
- 🧱 Bater na parede encerra o jogo.
- 🪞 Bater no próprio corpo encerra o jogo.
- ♻️ Após o fim de jogo, use o botão de reiniciar para jogar novamente.

### 🕹️ Versão Pygame

- 🎲 A cobra e a comida começam em posições aleatórias.
- 🍽️ Comer a comida faz a cobra crescer.
- 🧱 Sair do tabuleiro reinicia a cobra e gera uma nova comida.

## 🌟 Por Que Este Projeto É Valioso

- 📌 Demonstra programação orientada a eventos em Python
- 🔍 Mostra padrões práticos de loop de jogo e gerenciamento de estado
- ⚖️ Compara duas abordagens (toolkit gráfico vs. biblioteca de jogos) para o mesmo jogo
- 🧱 Serve como uma base sólida para aprender desenvolvimento de interfaces gráficas e arquitetura de jogos

## 🌐 Conecte-se Comigo
Acompanhe minha jornada e outros projetos em:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-lucsantosdev-blue?logo=linkedin)](https://www.linkedin.com/in/lucsantosdev)
[![GitHub](https://img.shields.io/badge/GitHub-lucsantosdev-181717?logo=github)](https://github.com/lucsantosdev)
[![Email](https://img.shields.io/badge/Gmail-lucsantosdev@gmail.com-181717?logo=gmail)](mailto:lucsantosdev@gmail.com)
[![YouTube](https://img.shields.io/badge/YouTube-lucsantosdev-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@lucsantosdev)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi)](https://ko-fi.com/lucsantosdev)

---

🧠 Je 9:23-24
