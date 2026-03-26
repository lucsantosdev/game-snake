import tkinter
import random

ROWS = 25
COLS = 25
CELL_SIZE = 25

WINDOW_WIDTH = CELL_SIZE * COLS
WINDOW_HEIGHT = CELL_SIZE * ROWS

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


window.mainloop()

#12min