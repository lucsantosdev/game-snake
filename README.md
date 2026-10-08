# 🐍 Snake Game (Python: Tkinter + Pygame)
>A classic Snake Game built in Python, implemented in two versions: one with Tkinter and another with Pygame, focused on clean logic and responsive gameplay.

🌍 **Read this in other languages:** [Português](lang/README.pt-BR.md) | [Español](lang/README.es.md)

![Project Presentation](assets/preview.gif)

## 🎮 Project Overview

This project implements the core Snake experience on a 25x25 grid as a desktop app. The same game is developed in two different ways, so you can compare how each library handles windows, input, drawing and the game loop:

| | 🖼️ Tkinter version | 🕹️ Pygame version |
|---|---|---|
| 📁 Location | [`tkinter/snake.py`](tkinter/snake.py) | [`pygame/snake.py`](pygame/snake.py) |
| 📦 Dependencies | None (standard library) | `pygame` |
| 🎯 Controls | Arrow keys | Arrow keys or `W` `A` `S` `D` |
| 🐣 Starting position | Fixed (top-left area) | Random |
| 🧮 Score | ✅ Shown on game over | ❌ Not yet |
| 🧱 Wall collision | Game over | Snake and food reset automatically |
| 🪞 Self-collision | ✅ Game over | ❌ Not yet |
| 🔁 Restart | Restart button | Automatic |
| 🏃 Game loop | `window.after(100, draw)` | `while True` + `clock.tick(10)` |
| 🚧 Status | Complete | Initial version (in progress) |

## 🖼️ Tkinter Version

The original and most complete version, built only with Python's standard library.

- ⚡ Real-time movement with arrow key controls (reversing direction is blocked)
- 🍎 Food spawning and snake growth
- 💥 Collision detection (walls and self-collision)
- 🧮 Score tracking
- 🔁 Game-over screen with restart button
- 🪟 Window centered on screen with a fixed board size

### 🧠 Architecture Notes

- 🧩 A `Cell` class for board positions
- 🌐 Global game state variables (snake, food, score, velocity, game_over)
- 🏃 A `move()` function for game updates
- 🖌️ A `draw()` loop scheduled with `window.after(100, draw)` (10 updates per second)

## 🕹️ Pygame Version

A newer version that rebuilds the game using [Pygame](https://www.pygame.org/), a library made specifically for games. It is still an initial version and is being developed step by step.

- ⚡ Movement with arrow keys or `W` `A` `S` `D`
- 🍎 Food spawning and snake growth
- 🎲 Snake and food start at random positions
- 🧱 Leaving the board resets the snake and the food

### 🧠 Architecture Notes

- 🟩 `pygame.Rect` objects for the snake segments and the food
- 🔄 A classic `while True` game loop that handles events, updates and drawing
- ⏱️ `pygame.time.Clock` limits the game to 10 frames per second
- 📐 `window.get_rect().contains(...)` checks if the snake is inside the board

## 🧰 Tech Stack

- Python 3
- Tkinter (standard Python GUI library) 🖼️
- Pygame (game development library) 🕹️
- `random` (for food placement)

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Open the project folder.

### 🖼️ Tkinter version

No external dependencies are required:

```bash
python tkinter/snake.py
```

### 🕹️ Pygame version

Install Pygame first:

```bash
pip install pygame
```

Then run:

```bash
python pygame/snake.py
```

## 🎯 Controls

- ⬆️⬇️⬅️➡️ Arrow keys: move the snake (both versions)
- 🔤 `W` `A` `S` `D`: move the snake (Pygame version)
- 🔄 Restart button: shown after game over to start a new match (Tkinter version)

## 📜 Current Gameplay Rules

### 🖼️ Tkinter version

- 🐣 The snake starts near the top-left area of the board.
- 🍽️ Eating food increases score and grows the snake body.
- 🧱 Hitting a wall ends the game.
- 🪞 Hitting your own body ends the game.
- ♻️ After game over, use the restart button to reset state and play again.

### 🕹️ Pygame version

- 🎲 The snake and the food start at random positions.
- 🍽️ Eating food grows the snake body.
- 🧱 Leaving the board resets the snake and places new food.

## 🌟 Why This Project Is Valuable

- 📌 Demonstrates event-driven programming in Python
- 🔍 Shows practical game-loop and state-management patterns
- ⚖️ Compares two approaches (GUI toolkit vs. game library) for the same game
- 🧱 Serves as a solid base for learning GUI development and gameplay architecture

## 🌐 Connect with Me
Follow my journey and other projects on:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-lucsantosdev-blue?logo=linkedin)](https://www.linkedin.com/in/lucsantosdev)
[![GitHub](https://img.shields.io/badge/GitHub-lucsantosdev-181717?logo=github)](https://github.com/lucsantosdev)
[![Email](https://img.shields.io/badge/Gmail-lucsantosdev@gmail.com-181717?logo=gmail)](mailto:lucsantosdev@gmail.com)
[![YouTube](https://img.shields.io/badge/YouTube-lucsantosdev-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@lucsantosdev)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support-ff5e5b?logo=ko-fi)](https://ko-fi.com/lucsantosdev)

---

🧠 Je 9:23-24
