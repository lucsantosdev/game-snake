# 🖼️ Construindo o Jogo da Cobrinha com Tkinter — Passo a Passo

> Um guia para quem está começando em programação (e curte jogos!). No final, você terá o seu próprio Snake funcionando, **sem instalar nada além do Python**.

**Nível:** iniciante (você já precisa saber o básico de Python: variáveis, `if`, `for`, listas, funções e um pouco de classes).
**Tempo estimado:** 2 a 3 horas.
**Arquivo final:** [`tkinter/snake.py`](../tkinter/snake.py)

---

## 📚 Índice

1. [O que vamos construir](#1--o-que-vamos-construir)
2. [Preparando o ambiente](#2--preparando-o-ambiente)
3. [Conceitos-chave antes de começar](#3--conceitos-chave-antes-de-começar)
4. [Passo 1 — Constantes e a classe Cell](#passo-1--constantes-e-a-classe-cell)
5. [Passo 2 — Criando a janela e o canvas](#passo-2--criando-a-janela-e-o-canvas)
6. [Passo 3 — Centralizando a janela](#passo-3--centralizando-a-janela)
7. [Passo 4 — O estado do jogo](#passo-4--o-estado-do-jogo)
8. [Passo 5 — Desenhando e o loop do jogo](#passo-5--desenhando-e-o-loop-do-jogo)
9. [Passo 6 — Lendo o teclado](#passo-6--lendo-o-teclado)
10. [Passo 7 — Movendo a cobra](#passo-7--movendo-a-cobra)
11. [Passo 8 — Comendo e crescendo](#passo-8--comendo-e-crescendo)
12. [Passo 9 — O corpo segue a cabeça](#passo-9--o-corpo-segue-a-cabeça)
13. [Passo 10 — Colisões e Game Over](#passo-10--colisões-e-game-over)
14. [Passo 11 — Tela de Game Over e pontuação](#passo-11--tela-de-game-over-e-pontuação)
15. [Passo 12 — Botão de reiniciar](#passo-12--botão-de-reiniciar)
16. [Código completo](#-código-completo)
17. [Desafios para você evoluir o jogo](#-desafios-para-você-evoluir-o-jogo)

---

## 1. 🎯 O que vamos construir

- Uma janela de **625 × 625 pixels**, dividida em uma **grade de 25 × 25 células**, centralizada na tela.
- Uma cobra verde controlada pelas **setas do teclado**.
- Uma comida vermelha. Ao comer, a cobra **cresce** e você ganha **1 ponto**.
- Se a cobra bater na **parede** ou em **si mesma**: *Game Over*, com a pontuação e um botão **Restart**.

---

## 2. 🛠️ Preparando o ambiente

1. Instale o **Python 3** (python.org). O **Tkinter já vem junto** com ele — não precisa instalar nada!
2. Crie uma pasta para o projeto e dentro dela um arquivo `snake.py`.

> 💡 Para testar se o Tkinter está funcionando, rode no terminal: `python -m tkinter`. Uma janelinha de teste deve aparecer.

---

## 3. 🧩 Conceitos-chave antes de começar

### O que é o Tkinter?

É a biblioteca padrão do Python para criar **janelas, botões e desenhos**. Ela foi pensada para programas com interface (como uma calculadora), e não especificamente para jogos. Por isso, vamos precisar construir nós mesmos algumas coisas que uma biblioteca de jogos daria pronta — e isso é ótimo para aprender!

### O loop de eventos (`mainloop`)

Em um programa com janela, o Python fica "esperando" coisas acontecerem (cliques, teclas, tempo passando). Isso é a **programação orientada a eventos**. Quem cuida disso é o `window.mainloop()`.

### Como fazer um jogo sem um `while True`?

Se você colocasse um `while True` aqui, a janela **travaria**, pois o Tkinter nunca teria chance de atualizar a tela. A solução é pedir ao Tkinter:

> "Daqui a 100 milissegundos, chame esta função de novo."

Isso é o `window.after(100, minha_funcao)`. Se a função se agenda novamente, vira um loop:

```
draw() ─► atualiza o jogo ─► desenha ─► window.after(100, draw) ─┐
  ▲                                                               │
  └───────────────────────────────────────────────────────────────┘
```

100 ms entre chamadas = **10 quadros por segundo**.

### O canvas e a grade

O **Canvas** é uma "folha de desenho" dentro da janela. A cada quadro **apagamos tudo e desenhamos de novo** (como numa animação em papel).

Nosso tabuleiro é uma grade; cada célula tem 25 pixels:

```
(0,0) ──────────────► x
  │   ┌──┬──┬──┬──┐
  │   │  │  │  │  │   cada quadrado = 25 × 25 pixels
  │   ├──┼──┼──┼──┤   y cresce para BAIXO!
  ▼   │  │  │  │  │
  y   └──┴──┴──┴──┘
```

---

## Passo 1 — Constantes e a classe Cell

Comece o arquivo com:

```python
import tkinter
import random

ROWS = 25
COLS = 25
CELL_SIZE = 25

WINDOW_WIDTH = CELL_SIZE * COLS
WINDOW_HEIGHT = CELL_SIZE * ROWS

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 🧠 Entendendo

- **Constantes** (MAIÚSCULAS): valores que não mudam. Se quiser um tabuleiro maior, basta mudar aqui.
- `WINDOW_WIDTH = 25 × 25 = 625` pixels. Idem para a altura.
- **A classe `Cell`** representa **uma posição** no tabuleiro, com `x` e `y` em pixels. Usaremos para a cabeça, para a comida e para cada pedaço do corpo.

> 💡 *Por que uma classe e não uma tupla `(x, y)`?* Porque queremos **alterar** a posição depois (`snake.x += 25`). Tuplas não podem ser alteradas; objetos podem.

---

## Passo 2 — Criando a janela e o canvas

```python
# Janela do jogo
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Canvas: a "folha de desenho"
canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                        borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()
```

### 🧠 Entendendo

- `tkinter.Tk()` cria a janela principal.
- `resizable(False, False)` impede o jogador de redimensionar (largura, altura), mantendo a grade certinha.
- `Canvas(...)` cria a área de desenho preta com o tamanho do tabuleiro. `borderwidth=0` e `highlightthickness=0` removem bordas que "roubariam" alguns pixels.
- `canvas.pack()` coloca o canvas dentro da janela.
- `window.update()` força o Tkinter a calcular o tamanho real da janela agora. Precisamos disso no próximo passo.

Para ver a janela, adicione **no fim do arquivo** (e deixe-a lá até o final do tutorial):

```python
window.mainloop()
```

▶️ **Teste:** uma janela preta de 625×625 deve aparecer.

---

## Passo 3 — Centralizando a janela

Por padrão, a janela aparece em um canto da tela. Vamos centralizá-la. Coloque **antes** do `window.mainloop()`:

```python
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
```

### 🧠 Entendendo

A conta é simples: o **centro da tela** menos **metade da janela** dá o canto superior esquerdo para a janela ficar no meio.

```
x = metade da largura da tela − metade da largura da janela
```

- `//` é a divisão inteira (sem casas decimais).
- `geometry("LxA+X+Y")` define tamanho **e** posição. Por exemplo: `"625x625+400+100"`.

---

## Passo 4 — O estado do jogo

O **estado** é o conjunto de variáveis que descreve "como o jogo está agora". Se você tirasse uma foto do jogo, o estado diria tudo. Adicione **antes** do `window.mainloop()`:

```python
# Inicializando o jogo
snake = Cell(5 * CELL_SIZE, 5 * CELL_SIZE)    # a cabeça
food = Cell(10 * CELL_SIZE, 10 * CELL_SIZE)   # a comida
snake_body = []                               # os pedaços do corpo
velocityX = 0
velocityY = 0
game_over = False
score = 0
restart_button = None
```

### 🧠 Entendendo

| Variável | Para que serve |
|----------|----------------|
| `snake` | Posição da **cabeça** (célula 5, 5 → pixel 125, 125) |
| `food` | Posição da comida |
| `snake_body` | Lista de `Cell` com o resto do corpo (começa vazia) |
| `velocityX`, `velocityY` | Direção do movimento: `-1`, `0` ou `1` |
| `game_over` | `True` quando o jogador perdeu |
| `score` | Pontos |
| `restart_button` | Guardará o botão (criaremos no Passo 12) |

**Detalhe importante:** a velocidade vale `-1`, `0` ou `1` (uma *direção*), e depois multiplicamos por `CELL_SIZE`. Assim:

| Direção | `velocityX` | `velocityY` |
|---------|:-----------:|:-----------:|
| Parada | 0 | 0 |
| Cima | 0 | -1 |
| Baixo | 0 | 1 |
| Esquerda | -1 | 0 |
| Direita | 1 | 0 |

> 🧠 A cobra é a **cabeça** (`snake`) + a **lista do corpo** (`snake_body`). Separar os dois deixa a lógica de movimento mais simples.

---

## Passo 5 — Desenhando e o loop do jogo

Agora criamos a função `draw`, que desenha o jogo e se agenda para o próximo quadro. Coloque **antes** do `window.mainloop()`:

```python
def draw():
    canvas.delete("all")  # apaga tudo o que estava desenhado

    # comida primeiro, cobra depois (a cobra fica por cima)
    canvas.create_rectangle(food.x, food.y, food.x + CELL_SIZE, food.y + CELL_SIZE, fill="red")
    canvas.create_rectangle(snake.x, snake.y, snake.x + CELL_SIZE, snake.y + CELL_SIZE, fill="lime green")

    for cell in snake_body:
        canvas.create_rectangle(cell.x, cell.y, cell.x + CELL_SIZE, cell.y + CELL_SIZE, fill="lime green")

    window.after(100, draw)  # chama draw de novo daqui a 100 ms


draw()  # dispara o primeiro quadro
```

### 🧠 Entendendo

- `canvas.delete("all")` limpa a folha. A cada quadro redesenhamos tudo do zero.
- `create_rectangle(x1, y1, x2, y2, fill=cor)` desenha um retângulo pelos **dois cantos opostos**: o superior esquerdo `(x, y)` e o inferior direito `(x + 25, y + 25)`.
- A **ordem do desenho** importa: o que é desenhado depois fica por cima.
- A última linha de `draw` agenda a si mesma: **esse é o nosso game loop**.
- `draw()` fora da função "dá a partida" no primeiro quadro.

▶️ **Teste:** você deve ver um quadrado verde e um vermelho no fundo preto.

---

## Passo 6 — Lendo o teclado

Crie a função que muda a direção, **antes** do `window.mainloop()`:

```python
def change_direction(e):
    global velocityX, velocityY, game_over

    if game_over:
        return  # se acabou, ignora o teclado

    if e.keysym == "Up" and velocityY != 1:         # não pode ir pra cima se está indo pra baixo
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0
```

E conecte a função ao teclado (também antes do `mainloop`):

```python
window.bind("<KeyRelease>", change_direction)
```

### 🧠 Entendendo

- **`global`:** dentro de uma função, se você atribuir valor a uma variável criada fora dela, precisa declará-la como `global`. Sem isso, o Python criaria uma variável nova e local, e o jogo não mudaria nada.
- `window.bind("<KeyRelease>", função)`: "quando uma tecla for solta, chame esta função". O Tkinter entrega um objeto de evento `e`, e `e.keysym` guarda o nome da tecla (`"Up"`, `"Down"`, `"Left"`, `"Right"`).
- **Evitando a marcha à ré:** se a cobra vai para baixo (`velocityY == 1`) e o jogador aperta cima, ela bateria no próprio pescoço. A condição `velocityY != 1` bloqueia isso. Faça o mesmo raciocínio para as outras três direções.

Por enquanto, nada se move: só mudamos as variáveis de velocidade. O movimento vem a seguir.

---

## Passo 7 — Movendo a cobra

Crie a função `move`, que **atualiza** o estado do jogo a cada quadro:

```python
def move():
    global snake, food, snake_body, game_over, score
    if game_over:
        return  # jogo acabou: nada se move

    snake.x += velocityX * CELL_SIZE
    snake.y += velocityY * CELL_SIZE
```

Agora faça o `draw` chamá-la. Na primeira linha da função `draw`:

```python
def draw():
    move()                # <-- NOVO: atualiza o jogo antes de desenhar
    canvas.delete("all")
    ...
```

### 🧠 Entendendo

Separamos duas responsabilidades:

- `move()` → **lógica** (muda o estado);
- `draw()` → **visual** (só mostra o estado).

A cada quadro: atualiza, depois desenha. Misturar as duas é tentador, mas deixa o código confuso.

O movimento é `velocidade × tamanho da célula`: se `velocityX = 1`, a cabeça anda `25` pixels para a direita — exatamente uma célula.

▶️ **Teste:** aperte uma seta (e solte!). A cobrinha deve andar. Ela vai sair da tela por enquanto.

---

## Passo 8 — Comendo e crescendo

Dentro de `move()`, **antes** das linhas que mudam `snake.x` e `snake.y`, adicione:

```python
    # quando a cabeça está em cima da comida
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Cell(snake.x, snake.y))  # cresce: novo pedaço no corpo
        food.x = random.randint(0, COLS - 1) * CELL_SIZE   # comida em novo lugar
        food.y = random.randint(0, ROWS - 1) * CELL_SIZE
        score += 1
```

### 🧠 Entendendo

- Como tudo está alinhado na grade, **mesma posição = mesma célula**. Se `x` e `y` da cabeça e da comida são iguais, a cobra comeu.
- Quando come: adicionamos um `Cell` ao corpo, sorteamos nova posição para a comida e somamos 1 ponto.
- **Por que `random.randint(0, 24) * 25`?** Sorteamos o número da **célula** (0 a 24) e convertemos em pixels. Assim a comida sempre cai certinho na grade (e nunca fora dela).

▶️ **Teste:** coma a comida. Ela muda de lugar. (O corpo ainda não aparece direito: vem no próximo passo.)

---

## Passo 9 — O corpo segue a cabeça

Esta é a lógica mais interessante do jogo.

A ideia: **cada pedaço do corpo vai para onde estava o pedaço da frente.** E o primeiro pedaço do corpo vai para onde estava a cabeça. Fazemos isso **da cauda para a frente**:

```
Cabeça: H      Corpo: [B0, B1, B2]

1) B2 ← posição de B1
2) B1 ← posição de B0
3) B0 ← posição da cabeça H
4) só então a cabeça H anda para a próxima casa
```

Em `move()`, **depois** do bloco de comer e **antes** de mover a cabeça:

```python
    # atualiza os pedaços do corpo, da cauda para a frente
    for i in range(len(snake_body) - 1, -1, -1):
        cell = snake_body[i]
        if i == 0:
            cell.x = snake.x      # o 1º pedaço vai para onde a cabeça estava
            cell.y = snake.y
        else:
            prev_cell = snake_body[i - 1]
            cell.x = prev_cell.x  # os demais copiam o pedaço da frente
            cell.y = prev_cell.y
```

O `move()` completo fica assim até aqui:

```python
def move():
    global snake, food, snake_body, game_over, score
    if game_over:
        return

    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Cell(snake.x, snake.y))
        food.x = random.randint(0, COLS - 1) * CELL_SIZE
        food.y = random.randint(0, ROWS - 1) * CELL_SIZE
        score += 1

    for i in range(len(snake_body) - 1, -1, -1):
        cell = snake_body[i]
        if i == 0:
            cell.x = snake.x
            cell.y = snake.y
        else:
            prev_cell = snake_body[i - 1]
            cell.x = prev_cell.x
            cell.y = prev_cell.y

    snake.x += velocityX * CELL_SIZE
    snake.y += velocityY * CELL_SIZE
```

### 🧠 Entendendo

- `range(len(snake_body) - 1, -1, -1)` conta **de trás para frente**: do último índice até `0`.
- **Por que de trás para frente?** Se copiássemos da frente para trás, o pedaço `B1` copiaria `B0` — mas `B0` já teria sido movido, e todos os pedaços acabariam empilhados na mesma casa.
- **A ordem dentro de `move()` importa:** (1) checar a comida, (2) mover o corpo, (3) mover a cabeça. O corpo precisa "enxergar" a posição **antiga** da cabeça antes de ela andar.

▶️ **Teste:** coma algumas comidas e veja o rabinho te seguindo! 🐍

---

## Passo 10 — Colisões e Game Over

Duas formas de perder: **bater na parede** ou **bater em si mesma**. No início de `move()`, logo depois do `if game_over: return`, adicione:

```python
    # bateu na parede?
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return

    # bateu no próprio corpo?
    for cell in snake_body:
        if snake.x == cell.x and snake.y == cell.y:
            game_over = True
            return
```

### 🧠 Entendendo

- **Parede:** a cabeça está fora se `x` ou `y` for menor que `0` ou maior/igual ao tamanho da janela. Usamos `>=` porque as posições válidas vão de `0` até `WINDOW - 25`.
- **Si mesma:** percorremos o corpo e vemos se algum pedaço está na mesma célula que a cabeça.
- `game_over = True` + `return`: marcamos o fim e saímos de `move()` na hora. Como `move()` começa com `if game_over: return`, a cobra **para de andar** nos quadros seguintes.

> 🔎 **Detalhe curioso:** a checagem acontece no começo do quadro, *antes* de mover. Por isso o Game Over só é detectado no quadro seguinte ao movimento que levou a cabeça para fora. Na prática, ninguém percebe, pois são 100 ms.

▶️ **Teste:** bata na parede. A cobra deve parar.

---

## Passo 11 — Tela de Game Over e pontuação

Agora vamos mostrar uma mensagem. No `draw()`, **depois** do `for` que desenha o corpo e **antes** do `window.after`, adicione:

```python
    if game_over:
        canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
                           text="Game Over", fill="white", font=("Arial", 24))
        canvas.create_text(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 30,
                           text=f"Score: {score}", fill="white", font=("Arial", 18))
```

### 🧠 Entendendo

- `create_text(x, y, text=..., fill=cor, font=(fonte, tamanho))` escreve texto no canvas, centralizado no ponto `(x, y)`.
- Usamos o centro da janela (`WINDOW_WIDTH // 2`, `WINDOW_HEIGHT // 2`) para o "Game Over" e `+ 30` pixels abaixo para o placar.
- `f"Score: {score}"` é uma **f-string**: o valor da variável é inserido dentro do texto.

▶️ **Teste:** coma alguns pontos e perca de propósito. Aparecem "Game Over" e o placar.

---

## Passo 12 — Botão de reiniciar

Falta permitir jogar de novo.

### 12.1 A função que reinicia

Crie **antes** do `draw()`:

```python
def restart_game():
    global snake, food, snake_body, velocityX, velocityY, game_over, score

    snake.x = 5 * CELL_SIZE
    snake.y = 5 * CELL_SIZE
    food.x = random.randint(0, COLS - 1) * CELL_SIZE
    food.y = random.randint(0, ROWS - 1) * CELL_SIZE
    snake_body.clear()
    velocityX = 0
    velocityY = 0
    game_over = False
    score = 0

    restart_button.place_forget()  # esconde o botão
```

### 12.2 O botão

Crie o botão **depois** das funções e **antes** da chamada `draw()`:

```python
restart_button = tkinter.Button(window, text="Restart", command=restart_game,
                                font=("Arial", 12), padx=10, pady=4)
```

### 12.3 Mostrar e esconder o botão

No `draw()`, complete o bloco do Game Over:

```python
    if game_over:
        canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
                           text="Game Over", fill="white", font=("Arial", 24))
        canvas.create_text(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 30,
                           text=f"Score: {score}", fill="white", font=("Arial", 18))
        restart_button.place(x=WINDOW_WIDTH // 2, y=(WINDOW_HEIGHT // 2) + 70, anchor="center")
    else:
        restart_button.place_forget()
```

### 🧠 Entendendo

- **Reiniciar = voltar o estado ao inicial.** Por isso é importante que todo o estado do jogo esteja em variáveis bem definidas (Passo 4): basta resetá-las.
- `Button(..., command=restart_game)` — quando o botão for clicado, o Tkinter chama a função. Repare: passamos `restart_game` **sem parênteses**. Com parênteses, ela seria executada na hora de criar o botão!
- `place(x, y, anchor="center")` posiciona o botão no pixel indicado, usando o centro dele como referência. `place_forget()` o esconde.
- Usamos `snake_body.clear()` (e não `snake_body = []`) para esvaziar a mesma lista que o resto do código usa.

▶️ **Teste:** perca, clique em **Restart** e jogue de novo. 🎉

---

## ✅ Código completo

A ordem final do arquivo é: **constantes → classe → janela → estado → funções → botão → `draw()` → `bind` → `mainloop`**.

```python
import tkinter
import random

ROWS = 25
COLS = 25
CELL_SIZE = 25

WINDOW_WIDTH = CELL_SIZE * COLS
WINDOW_HEIGHT = CELL_SIZE * ROWS

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Janela do jogo
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                        borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

# Centralizar a janela
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Estado do jogo
snake = Cell(5 * CELL_SIZE, 5 * CELL_SIZE)
food = Cell(10 * CELL_SIZE, 10 * CELL_SIZE)
snake_body = []
velocityX = 0
velocityY = 0
game_over = False
score = 0
restart_button = None

def change_direction(e):
    global velocityX, velocityY, game_over

    if game_over:
        return

    if e.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score
    if game_over:
        return

    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return

    for cell in snake_body:
        if snake.x == cell.x and snake.y == cell.y:
            game_over = True
            return

    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Cell(snake.x, snake.y))
        food.x = random.randint(0, COLS - 1) * CELL_SIZE
        food.y = random.randint(0, ROWS - 1) * CELL_SIZE
        score += 1

    for i in range(len(snake_body) - 1, -1, -1):
        cell = snake_body[i]
        if i == 0:
            cell.x = snake.x
            cell.y = snake.y
        else:
            prev_cell = snake_body[i - 1]
            cell.x = prev_cell.x
            cell.y = prev_cell.y

    snake.x += velocityX * CELL_SIZE
    snake.y += velocityY * CELL_SIZE

def restart_game():
    global snake, food, snake_body, velocityX, velocityY, game_over, score

    snake.x = 5 * CELL_SIZE
    snake.y = 5 * CELL_SIZE
    food.x = random.randint(0, COLS - 1) * CELL_SIZE
    food.y = random.randint(0, ROWS - 1) * CELL_SIZE
    snake_body.clear()
    velocityX = 0
    velocityY = 0
    game_over = False
    score = 0

    restart_button.place_forget()

def draw():
    move()

    canvas.delete("all")

    canvas.create_rectangle(food.x, food.y, food.x + CELL_SIZE, food.y + CELL_SIZE, fill="red")
    canvas.create_rectangle(snake.x, snake.y, snake.x + CELL_SIZE, snake.y + CELL_SIZE, fill="lime green")

    for cell in snake_body:
        canvas.create_rectangle(cell.x, cell.y, cell.x + CELL_SIZE, cell.y + CELL_SIZE, fill="lime green")

    if game_over:
        canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
                           text="Game Over", fill="white", font=("Arial", 24))
        canvas.create_text(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 30,
                           text=f"Score: {score}", fill="white", font=("Arial", 18))
        restart_button.place(x=WINDOW_WIDTH // 2, y=(WINDOW_HEIGHT // 2) + 70, anchor="center")
    else:
        restart_button.place_forget()

    window.after(100, draw)

restart_button = tkinter.Button(window, text="Restart", command=restart_game,
                                font=("Arial", 12), padx=10, pady=4)

draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()
```

> 📌 **Dica de organização:** as funções `change_direction`, `move`, `restart_game` e `draw` podem ficar em qualquer ordem entre si, desde que o `draw()` (a chamada que dá a partida) e o `restart_button` sejam criados **depois** de todas elas.

---

## 🏆 Desafios para você evoluir o jogo

Do mais fácil ao mais difícil:

1. **🎨 Cores:** mude as cores da cobra, da comida e do fundo.
2. **⚡ Velocidade:** troque o `100` do `window.after(100, draw)` por outro valor. Menor = mais rápido.
3. **🏷️ Placar durante o jogo:** mostre o `score` no canto da tela enquanto joga (e não só no Game Over). *Dica:* use `canvas.create_text` no `draw()`.
4. **🍽️ Comida em lugar válido:** hoje a comida pode nascer em cima da cobra. Sorteie de novo se isso acontecer.
5. **📈 Dificuldade progressiva:** deixe o jogo um pouco mais rápido a cada 5 pontos. *Dica:* faça o tempo do `after` ser uma variável.
6. **🏅 Recorde:** guarde a maior pontuação (`high_score`) e mostre no Game Over.
7. **🔀 Mudança de direção segura:** se você apertar duas teclas muito rápido dentro do mesmo quadro, ainda é possível fazer a cobra se virar sobre si mesma. Consegue descobrir como e corrigir? *Dica:* pense em guardar a "próxima direção" e só aplicá-la no `move()`.

Bom jogo e bons estudos! 🐍
