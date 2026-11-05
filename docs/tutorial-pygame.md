# 🕹️ Construindo o Jogo da Cobrinha com Pygame — Passo a Passo

> Um guia para quem está começando em programação (e curte jogos!). No final, você terá o seu próprio Snake funcionando.

**Nível:** iniciante (você já precisa saber o básico de Python: variáveis, `if`, `for`, `while`, listas e funções).
**Tempo estimado:** 1 a 2 horas.
**Arquivo final:** [`pygame/snake.py`](../pygame/snake.py)

---

## 📚 Índice

1. [O que vamos construir](#1--o-que-vamos-construir)
2. [Preparando o ambiente](#2--preparando-o-ambiente)
3. [Como todo jogo funciona: o game loop](#3--como-todo-jogo-funciona-o-game-loop)
4. [Passo 1 — Importações e constantes](#passo-1--importações-e-constantes)
5. [Passo 2 — Criando a janela](#passo-2--criando-a-janela)
6. [Passo 3 — O game loop e o botão de fechar](#passo-3--o-game-loop-e-o-botão-de-fechar)
7. [Passo 4 — Desenhando a comida e a cobra](#passo-4--desenhando-a-comida-e-a-cobra)
8. [Passo 5 — Posições aleatórias alinhadas à grade](#passo-5--posições-aleatórias-alinhadas-à-grade)
9. [Passo 6 — Lendo o teclado](#passo-6--lendo-o-teclado)
10. [Passo 7 — Movendo a cabeça](#passo-7--movendo-a-cabeça)
11. [Passo 8 — O corpo segue a cabeça](#passo-8--o-corpo-segue-a-cabeça)
12. [Passo 9 — Comendo e crescendo](#passo-9--comendo-e-crescendo)
13. [Passo 10 — Limites do tabuleiro](#passo-10--limites-do-tabuleiro)
14. [Código completo](#-código-completo)
15. [Desafios para você evoluir o jogo](#-desafios-para-você-evoluir-o-jogo)

---

## 1. 🎯 O que vamos construir

Um jogo da cobrinha clássico:

- Uma janela de **625 × 625 pixels**, dividida em uma **grade de 25 × 25 quadradinhos**.
- Uma cobra verde que se move sozinha e é controlada pelo teclado.
- Uma comida vermelha. Quando a cobra come, ela **cresce**.
- Se a cobra bater na borda, o jogo **recomeça**.

---

## 2. 🛠️ Preparando o ambiente

1. Instale o **Python 3** (site oficial: python.org).
2. Abra o terminal e instale o Pygame:

```bash
pip install pygame
```

3. Crie uma pasta para o projeto e, dentro dela, um arquivo chamado `snake.py`.

> 💡 **O que é o Pygame?** É uma biblioteca (um "pacote de ferramentas") feita para criar jogos em Python. Ela já sabe abrir janelas, desenhar formas, ler teclado e controlar o tempo. Sem ela, teríamos que fazer tudo isso do zero.

---

## 3. 🔄 Como todo jogo funciona: o game loop

Antes de escrever código, entenda a ideia mais importante deste tutorial.

Um jogo é como um **filme**: várias imagens (quadros ou *frames*) passando tão rápido que parece movimento. A cada quadro, o jogo repete **sempre os mesmos 3 passos**:

```
┌─────────────────────────────────────────┐
│ 1. ENTRADA   → o jogador apertou algo?  │
│ 2. ATUALIZAR → mover coisas, checar     │
│                colisões, mudar pontos   │
│ 3. DESENHAR  → pintar tudo na tela      │
└─────────────────────────────────────────┘
          ↑ e volta pro começo ↓
```

Isso é o **game loop** (laço do jogo). Em Python, ele vira um `while True:`. Tudo que fizermos daqui para frente vai se encaixar em um desses três passos.

---

## Passo 1 — Importações e constantes

Comece o arquivo `snake.py` com:

```python
import pygame
from sys import exit  # serve para encerrar o programa
import random

ROWS = 25
COLUMNS = ROWS
CELL_SIZE = 25
GAME_WIDTH = CELL_SIZE * COLUMNS
GAME_HEIGHT = CELL_SIZE * ROWS
```

### 🧠 Entendendo

- `import pygame` — traz a biblioteca para o nosso código.
- `random` — vai sortear posições para a comida.
- **Constantes** (nomes em MAIÚSCULAS) são valores que não mudam. Usamos constantes para **não espalhar números mágicos** pelo código. Se um dia você quiser um tabuleiro maior, muda em um lugar só.

### 📐 A ideia da grade

Nosso tabuleiro tem 25 linhas × 25 colunas, e cada quadradinho (célula) tem 25 pixels de lado:

```
largura da janela = 25 colunas × 25 pixels = 625 pixels
altura da janela  = 25 linhas  × 25 pixels = 625 pixels
```

Tudo no jogo (cobra e comida) terá exatamente o tamanho de **uma célula**.

---

## Passo 2 — Criando a janela

Logo abaixo das constantes:

```python
pygame.init()  # liga todos os módulos do pygame
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))  # cria a janela
pygame.display.set_caption("Snake Game (pygame version)")    # título da janela
clock = pygame.time.Clock()  # relógio, para controlar a velocidade do jogo
```

### 🧠 Entendendo

- `pygame.init()` precisa ser chamado **uma vez** antes de usar o pygame.
- `set_mode((largura, altura))` cria a janela e devolve um objeto (`window`) que representa a **tela onde vamos desenhar**.
- Repare nos **parênteses duplos**: `set_mode(( ... ))`. O de dentro cria uma **tupla** `(largura, altura)`, que é um único valor com dois números.
- `clock` será usado para o jogo não rodar rápido demais (veremos no Passo 4).

---

## Passo 3 — O game loop e o botão de fechar

Agora o coração do jogo. No final do arquivo:

```python
# game loop
while True:
    for event in pygame.event.get():  # pega todos os eventos (teclas, mouse, etc.)
        if event.type == pygame.QUIT:  # o jogador clicou no X da janela
            pygame.quit()  # desliga o pygame
            exit()         # encerra o programa
```

### 🧠 Entendendo

- `while True:` repete para sempre — é o nosso game loop.
- `pygame.event.get()` devolve uma **lista de eventos** que aconteceram desde o último quadro (uma tecla apertada, o mouse se movendo, o clique no X...).
- Percorremos essa lista com um `for`. Se algum evento for do tipo `QUIT`, fechamos tudo.

▶️ **Teste:** rode `python snake.py`. Vai aparecer uma janela (provavelmente preta ou vazia) e ela fecha quando você clica no X. Se funcionou, o esqueleto está pronto! 🎉

> ⚠️ Sem esse tratamento do `QUIT`, a janela não fecha — o loop nunca termina.

---

## Passo 4 — Desenhando a comida e a cobra

### 4.1 Os objetos do jogo

O Pygame tem um tipo chamado `pygame.Rect` (retângulo): guarda posição `(x, y)` e tamanho `(largura, altura)`. Vamos usá-lo para **tudo**: comida e cada pedaço da cobra.

Coloque **antes** do `while True:` (por enquanto, posições fixas):

```python
food = pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE)  # x, y, largura, altura
snake = []  # lista com os pedaços da cobra
snake.append(pygame.Rect(300, 300, CELL_SIZE, CELL_SIZE))  # a cabeça
```

> 💡 A cobra é uma **lista de retângulos**. O item de índice `0` é sempre a **cabeça**; os outros são o corpo.

### 4.2 Pintando na tela

Dentro do `while True:`, **depois** do `for event...`, adicione:

```python
    window.fill("black")                      # pinta o fundo de preto
    pygame.draw.rect(window, "red", food)     # desenha a comida em vermelho

    for snake_part in snake:                  # desenha cada pedaço da cobra
        pygame.draw.rect(window, "green", snake_part)

    pygame.display.update()  # mostra na tela o que desenhamos
    clock.tick(10)           # limita a 10 quadros por segundo
```

### 🧠 Entendendo

- **A ordem importa!** Primeiro limpamos a tela (`fill`), depois desenhamos por cima. É como pintar um quadro: o que vem depois cobre o que veio antes.
- Desenhar não mostra nada imediatamente. O Pygame desenha numa "tela escondida" e só quando chamamos `display.update()` ela aparece. Isso evita que a imagem fique piscando.
- `clock.tick(10)` faz o loop esperar o tempo necessário para rodar **no máximo 10 vezes por segundo**. Isso define a velocidade da cobra: 10 quadros por segundo = 10 movimentos por segundo. Quer um jogo mais rápido? Aumente esse número.

▶️ **Teste:** você deve ver um quadradinho verde (cobra) e um vermelho (comida) em um fundo preto.

---

## Passo 5 — Posições aleatórias alinhadas à grade

Posições fixas são chatas. Queremos que a comida (e a cobra) nasçam em lugares aleatórios — **mas sempre dentro da grade**.

Crie uma função **antes** de criar `food` e `snake`:

```python
def get_random(limit):
    return random.randint(0, limit - 1) * CELL_SIZE
```

E use-a nas posições:

```python
food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)
snake = []
snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE))
```

### 🧠 Entendendo

Por que `* CELL_SIZE`? Imagine que a comida pudesse nascer em `x = 137`. Ela ficaria "no meio" de duas células e a cobra nunca conseguiria encaixar nela.

Por isso sorteamos o **número da célula** e depois convertemos para pixels:

```
random.randint(0, 24)  →  por exemplo, 7   (coluna 7)
7 * 25                 →  175 pixels       (posição real na tela)
```

Assim, `x` e `y` são sempre múltiplos de 25: **a grade fica perfeita**.

▶️ **Teste:** rode várias vezes. Cobra e comida devem nascer em lugares diferentes a cada execução.

---

## Passo 6 — Lendo o teclado

A cobra se move **sozinha**, sempre na mesma direção, até apertarmos outra tecla. Então precisamos guardar a **velocidade** (para onde ela está indo).

Antes do `while True:`:

```python
snake_velocity = (0, 0)  # (movimento em x, movimento em y). Começa parada.
```

Dentro do `for event...`, logo depois do bloco do `QUIT`:

```python
        if event.type == pygame.KEYDOWN:  # o jogador apertou uma tecla
            if event.key in (pygame.K_UP, pygame.K_w):
                snake_velocity = (0, -CELL_SIZE)   # para cima
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                snake_velocity = (0, CELL_SIZE)    # para baixo
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                snake_velocity = (-CELL_SIZE, 0)   # para a esquerda
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                snake_velocity = (CELL_SIZE, 0)    # para a direita
```

### 🧠 Entendendo

Na tela, o sistema de coordenadas é diferente do que você aprendeu na matemática:

```
(0,0) ──────────► x (cresce para a direita)
  │
  │
  ▼
  y (cresce para BAIXO!)
```

Por isso:

| Direção | Velocidade `(x, y)` |
|---------|--------------------|
| Cima | `(0, -25)` (y diminui) |
| Baixo | `(0, 25)` (y aumenta) |
| Esquerda | `(-25, 0)` |
| Direita | `(25, 0)` |

Cada movimento é de **uma célula inteira** (25 pixels), e não de 1 pixel. Assim a cobra "pula" de casa em casa, como no Snake clássico.

`event.key in (pygame.K_UP, pygame.K_w)` pergunta: "a tecla é a seta para cima **ou** a tecla W?". Assim o jogo aceita setas e WASD.

---

## Passo 7 — Movendo a cabeça

Agora usamos a velocidade para mover. É o passo de **atualizar**. No `while True:`, **depois** do `for event...` e **antes** do `window.fill(...)`:

```python
    # mover a cabeça
    snake[0].move_ip(snake_velocity)
```

### 🧠 Entendendo

- `snake[0]` é a cabeça.
- `move_ip((dx, dy))` desloca o retângulo **"in place"** (direto nele mesmo): `x += dx` e `y += dy`.

▶️ **Teste:** aperte uma seta. O quadradinho verde deve andar sozinho. Se sair da tela ele some — vamos resolver isso no Passo 10.

---

## Passo 8 — O corpo segue a cabeça

Agora o desafio mais bonito do jogo: como o corpo acompanha a cabeça?

A ideia: **cada pedaço vai para onde o pedaço da frente estava**. Fazemos isso da **cauda para a cabeça**:

```
Antes do movimento:      [cabeça][corpo1][corpo2][cauda]
                            A       B       C       D

1) cauda (D) ← posição de C
2) corpo2 (C) ← posição de B
3) corpo1 (B) ← posição de A
4) a cabeça (A) anda para a nova casa
```

Substitua o bloco de mover a cabeça por:

```python
    # mover a cobra
    for i in range(len(snake) - 1, 0, -1):  # do último pedaço até o índice 1
        snake[i] = snake[i - 1].copy()      # cada pedaço copia o da frente
    snake[0].move_ip(snake_velocity)        # por último, move a cabeça
```

### 🧠 Entendendo

- `range(len(snake) - 1, 0, -1)` conta **de trás para frente**. Se a cobra tem 4 pedaços (índices 0 a 3), gera `3, 2, 1`. O índice `0` (cabeça) fica de fora, pois ela é movida separadamente.
- `.copy()` cria um retângulo **novo** com os mesmos valores. Se não copiássemos, dois itens da lista apontariam para o **mesmo objeto** e se moveriam juntos (um bug clássico!).
- **Por que de trás para frente?** Se fôssemos da cabeça para a cauda, o `corpo1` copiaria a cabeça e depois o `corpo2` copiaria um `corpo1` que já mudou — todos acabariam empilhados na mesma casa.

Por enquanto a cobra só tem a cabeça, então esse `for` ainda não faz nada. Ele ganha sentido no próximo passo.

---

## Passo 9 — Comendo e crescendo

Vamos detectar quando a cabeça encosta na comida. Adicione **depois** do movimento da cobra:

```python
    if snake[0].center == food.center:  # a cabeça está em cima da comida?
        snake.append(food)              # a comida vira um novo pedaço da cobra
        food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)  # nova comida
```

### 🧠 Entendendo

- `.center` devolve o ponto central do retângulo. Como tudo está alinhado na grade, dois retângulos com o mesmo centro estão **exatamente na mesma célula**. É assim que detectamos a colisão.
- **O truque do crescimento:** em vez de criar um pedaço novo, reaproveitamos o retângulo da comida e o colocamos no final da lista (`append`). Ele aparece na posição onde a comida estava — que é onde a cabeça está agora. No próximo quadro, o laço do Passo 8 faz o novo pedaço ir para o lugar certo atrás da cobra.
- Em seguida criamos uma **nova** comida em outro lugar aleatório.

▶️ **Teste:** pegue a comida. A cobra cresce e uma nova comida aparece! 🍎

---

## Passo 10 — Limites do tabuleiro

Falta tratar o que acontece quando a cobra sai da janela. No nosso caso, o jogo vai recomeçar. Adicione, ainda no passo de atualização (antes do `window.fill`):

```python
    # a cabeça saiu da janela?
    if not window.get_rect().contains(snake[0]):
        snake.clear()  # esvazia a lista (a cobra "morre")
        snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE))  # nova cabeça
        food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)         # nova comida
```

### 🧠 Entendendo

- `window.get_rect()` é o retângulo da janela inteira.
- `.contains(snake[0])` é `True` quando a cabeça está **totalmente dentro** da janela. Com o `not`, o `if` roda quando ela está **fora**.
- Para "reiniciar", recriamos do zero a cobra e a comida.

▶️ **Teste:** leve a cobra até a borda. Ela deve reaparecer em outro lugar com uma comida nova.

---

## ✅ Código completo

Conferiu tudo? Seu `snake.py` deve estar parecido com este (comentários resumidos):

```python
import pygame
from sys import exit
import random

ROWS = 25
COLUMNS = ROWS
CELL_SIZE = 25
GAME_WIDTH = CELL_SIZE * COLUMNS
GAME_HEIGHT = CELL_SIZE * ROWS

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake Game (pygame version)")
clock = pygame.time.Clock()

def get_random(limit):
    return random.randint(0, limit - 1) * CELL_SIZE

food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)
snake = []
snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE))
snake_velocity = (0, 0)

# game loop
while True:
    # 1) ENTRADA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                snake_velocity = (0, -CELL_SIZE)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                snake_velocity = (0, CELL_SIZE)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                snake_velocity = (-CELL_SIZE, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                snake_velocity = (CELL_SIZE, 0)

    # 2) ATUALIZAR
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1].copy()
    snake[0].move_ip(snake_velocity)

    if snake[0].center == food.center:
        snake.append(food)
        food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)

    if not window.get_rect().contains(snake[0]):
        snake.clear()
        snake.append(pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE))
        food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), CELL_SIZE, CELL_SIZE)

    # 3) DESENHAR
    window.fill("black")
    pygame.draw.rect(window, "red", food)
    for snake_part in snake:
        pygame.draw.rect(window, "green", snake_part)
    pygame.display.update()
    clock.tick(10)
```

Repare como o `while True` tem exatamente os **3 passos do game loop**: entrada, atualizar e desenhar. 🎯

---

## 🏆 Desafios para você evoluir o jogo

Esta versão é a base. Agora é com você! Do mais fácil ao mais difícil:

1. **🎨 Cores:** troque as cores da cobra e da comida (o Pygame aceita nomes como `"blue"`, `"yellow"` ou tuplas RGB como `(255, 128, 0)`).
2. **⚡ Velocidade:** mude o valor do `clock.tick()` e veja como o jogo muda.
3. **🧮 Pontuação:** crie uma variável `score = 0`, some `1` a cada comida e mostre na tela. *Dica:* pesquise `pygame.font.SysFont` e `window.blit`.
4. **🚫 Sem marcha à ré:** hoje, se a cobra vai para a direita e você aperta esquerda, ela vira na hora. Impeça a direção oposta à atual.
5. **🪞 Colisão com o próprio corpo:** se a cabeça tocar em qualquer pedaço do corpo, reinicie o jogo. *Dica:* percorra `snake[1:]` e compare com `snake[0]`.
6. **🍽️ Comida em lugar válido:** hoje a comida pode nascer em cima da cobra. Sorteie de novo se isso acontecer.
7. **💀 Tela de Game Over:** em vez de reiniciar na hora, mostre uma mensagem e espere o jogador apertar uma tecla.

Bom jogo e bons estudos! 🐍
