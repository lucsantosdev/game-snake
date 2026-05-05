# 🐍 Snake Game (Python + Tkinter)

A classic Snake game built in pure Python using Tkinter, focused on clean logic and responsive gameplay.

## 🎮 Project Overview

This project is a desktop app who implements the core Snake experience on a 25x25 grid:

- ⚡ Real-time movement with arrow key controls
- 🍎 Food spawning and snake growth
- 💥 Collision detection (walls and self-collision)
- 🧮 Score tracking
- 🔁 Game-over state with restart button

The game runs in a desktop window, centered on screen, with a fixed board size and a smooth update loop.

## 🧰 Tech Stack

- Python 3
- Tkinter (standard Python GUI library) 🖼️
- `random` (for food placement)

No external dependencies are required.

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Open the project folder.
3. Run:

```bash
python snake.py
```

## 🎯 Controls

- ⬆️⬇️⬅️➡️ Arrow keys: move the snake
- 🔄 Restart button: shown after game over to start a new match

## 📜 Current Gameplay Rules

- 🐣 The snake starts near the top-left area of the board.
- 🍽️ Eating food increases score and grows the snake body.
- 🧱 Hitting a wall ends the game.
- 🪞 Hitting your own body ends the game.
- ♻️ After game over, use the restart button to reset state and play again.

## 🧠 Architecture Notes

The game is intentionally simple and structured around:

- 🧩 A `Cell` class for board positions
- 🌐 Global game state variables (snake, food, score, velocity, game_over)
- 🏃 A `move()` function for game updates
- 🖌️ A `draw()` loop scheduled with `window.after(100, draw)`

This makes the project beginner-friendly and easy to extend.

## 🌟 Why This Project Is Valuable

- 📌 Demonstrates event-driven programming in Python
- 🔍 Shows practical game-loop and state-management patterns
- 🧱 Serves as a solid base for learning GUI development and gameplay architecture

## 🌐 Connect with Me
Follow my journey and other projects on:
- **LinkedIn:** [lucsantosdev](https://www.linkedin.com/in/lucsantosdev)
- **GitHub:** [lucsantosdev](https://github.com/lucsantosdev)
- **Email:** [lucsantosdev@gmail.com](mailto:lucsantosdev@gmail.com)
- **Support me:** [Ko-Fi](https://ko-fi.com/lucsantosdev)


---

🧠 Je 9:23-24

