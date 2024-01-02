from tkinter import *
import random

#all constants for our game
GAME_WIDTH = 700
GAME_HEIGHT = 700
FOOD_COLOR = "#FF0000"
SNAKE_COLOR = "#00FF00"
SPEED = 250# the lower thevalue the faster the game 
SNAKEPARTS = 3
BACKGROUND = "#000000"
SPACE_SIZE = 50

class Snake:
    def __init__(self):
        self.body_size = SNAKEPARTS
        self.cordinates = []
        self.squares = []
        
        #cordinates 
        
        for i in range(0, SNAKEPARTS):
            self.cordinates.append([0,0])
            
            
        #we have  list in list that is why we are using for x,y
        
        for x,y in self.cordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)
        
        
        

class Food:
    def __init__(self):
        #POSSIBLE MOVES ON X AXIS AT ANY GIVEN TIME
        x = random.randint(0, GAME_WIDTH/SPACE_SIZE-1) * SPACE_SIZE
        y = random.randint(0, GAME_HEIGHT/SPACE_SIZE-1) * SPACE_SIZE
        self.cordinates = [x,y]
        #creating the food object 
        # the tag makes it easy to delete this object
        
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")

def changedirection(newdirection):
    global direction
    
    if newdirection == 'left':
        if newdirection != 'right':
            direction = newdirection
            
            
    elif newdirection == 'right':
        if direction != 'left':
            direction = newdirection
            
    elif newdirection == 'down':
        if direction != 'up':
            direction = newdirection
            
            
    elif newdirection == 'up':
        if direction != 'down':
            direction = newdirection            
            
    
            
            

def nextturn(snake, food):
    x, y = snake.cordinates[0]
    
    if direction == "up":
        y -= SPACE_SIZE
        
    elif direction == "down":
        y += SPACE_SIZE
        
        
    elif direction == "left":
        x -= SPACE_SIZE
        
        
        
    elif direction == "right":
        x += SPACE_SIZE
        
        
    snake.cordinates.insert(0, (x,y))
    
    
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill = SNAKE_COLOR)
    snake.squares.insert(0, square)
    
    
    if x == food.cordinates[0] and y == food.cordinates[1]:
        global score
        score += 1
        
        label.config(text = "Score: {}".format(score))
        
        canvas.delete("food")
        
        
        food = Food()
        
    else:
        
        del snake.cordinates[-1]
        
        canvas.delete(snake.squares[-1])
        
        
        del snake.squares[-1]
        
        
    if checkcollision(snake):
        game_over()
        
    else:
           
        window.after(SPEED, nextturn, snake, food)
        
        
        
        

def checkcollision(snake):
    x,y = snake.cordinates[0]
    
    if x  < 0  or x >= GAME_WIDTH:
        
        return True
    elif y  < 0  or y >= GAME_WIDTH:
        
        return True
    
    
    for snake_part in snake.cordinates[1: ]:
        if x == snake_part[0] and y == snake_part[1]:
            return True
        
        
def game_over():
    canvas.delete(ALL)
    
    canvas.create_text((canvas.winfo_width()/2),(canvas.winfo_height()/2), font =('Arial', 70),text = "Game OVER", tag = "game")
    canvas.pack()



window = Tk()

window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text = "score: {}".format(score), font = ("Arial", 40))
label.pack()


canvas = Canvas(window, width = GAME_WIDTH, height = GAME_HEIGHT, bg = BACKGROUND)
canvas.pack()
#we want to center this window as it appears  

# window.update()

# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# y = int((screen_height/2)- (window_height/2))
# x = int((screen_width/2) - (window_width/2))

# window.geometry(f"{window_width}x{window_height} + {x} + {y}")


window.bind('<Left>', lambda event: changedirection('left'))
window.bind('<Right>', lambda event: changedirection('right'))
window.bind('<Up>', lambda event: changedirection('up'))
window.bind('<Down>', lambda event: changedirection('down'))
snake = Snake()
food = Food()
nextturn(snake, food)
window.mainloop()