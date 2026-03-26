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

# Game Window
window = tkinter.Tk()
window.title("Snake Game by @lucsantosdev")
window.resizable(False, False)

# Customize the window size to fit the grid
canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()  

# Center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}") # format "(w)x(h)+(x)+(y)" 

# Initialize the Game
snake = Cell(5*CELL_SIZE, 5*CELL_SIZE) # Starting position of the snake's head on the single cell grid
food = Cell(10*CELL_SIZE, 10*CELL_SIZE) # Starting position of the food on the single cell grid

def draw():
    global snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + CELL_SIZE, snake.y + CELL_SIZE, fill="lime green")
    canvas.create_rectangle(food.x, food.y, food.x + CELL_SIZE, food.y + CELL_SIZE, fill="red")
    
    window.after(100, draw)  # Schedule the draw function to be called every 100 milliseconds

draw()  # Start the drawing loop



window.mainloop()