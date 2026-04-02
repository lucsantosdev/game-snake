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
snake_body = [] # List to hold the snake's body segments
velocityX = 0
velocityY = 0
game_over = False
score = 0

def change_direction(e):
    global velocityX, velocityY, game_over
    
    if game_over:
        return  # Ignore input if the game is over
    
    if e.keysym == "Up" and velocityY != 1:  # Prevent the snake from reversing
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:  # Prevent the snake from reversing
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:  # Prevent the snake from reversing
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:  # Prevent the snake from reversing
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score
    if game_over:
        return  # Stop moving if the game is over
    
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True  # Set game over if the snake hits the wall
        return
    
    for cell in snake_body:
        if snake.x == cell.x and snake.y == cell.y:
            game_over = True  # Set game over if the snake collides with itself
            return
    
    # When occours the collision with food
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Cell(snake.x, snake.y))  # Add a new segment to the snake's body
        # Move the food to a new random position
        food.x = random.randint(0, COLS - 1) * CELL_SIZE
        food.y = random.randint(0, ROWS - 1) * CELL_SIZE
        score += 1
        
    # updating the snake's body segments
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

def draw():
    global snake, food, snake_body, game_over, score
    move()
    
    canvas.delete("all")
    
    # draw the food and the snake (in that order to ensure the snake is drawn on top of the food)
    canvas.create_rectangle(food.x, food.y, food.x + CELL_SIZE, food.y + CELL_SIZE, fill="red")
    canvas.create_rectangle(snake.x, snake.y, snake.x + CELL_SIZE, snake.y + CELL_SIZE, fill="lime green")
    
    for cell in snake_body:
        canvas.create_rectangle(cell.x, cell.y, cell.x + CELL_SIZE, cell.y + CELL_SIZE, fill="lime green")
        
    if game_over:
        canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))
        canvas.create_text(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 30, text=f"Score: {score}", fill="white", font=("Arial", 18))
    
    window.after(100, draw)  # Schedule the draw function to be called every 100 milliseconds/10 frames per second

draw()  # Start the drawing loop


window.bind("<KeyRelease>", change_direction)
window.mainloop()