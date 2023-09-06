# num1=float(input("please enter the first number"))
# operator=input("please enter the operator ")
# num2=float(input("please enter the second number"))
# if operator =="+":
#  print(num1+num2)
# elif operator =="-":
#   print(num1-num2)

import random
import curses

screen = curses.initscr() 
# hon beredel scrren object lal screen kela
curses.curs_set(0)
#python curses documentation
screen_height, screen_width = screen.getmaxyx()  #window.gemaxyz() return a tuple (y,x)

window = curses.newwin(screen_height, screen_width, 0,0)  # ENU HA YE3TENE WINDOW NEW

window.keypad(1) #allow window to receive input from the keyboard

#set the delay for updating the screen
window.timeout(100)
#snake enu nshn ybalech mn hmahal mo3ayan tol w 3ard masaln 3 ases bde echtghl
snk_x = screen_width // 4  #integer division  #hayde lal toul

snk_y = screen_height // 2  #hayde lal 3ard

#define the initial position of the snake body
snake = [[snk_x, snk_y], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
#create the food in the middle of window
food = [screen_height // 2, screen_width // 2]

window.addch(food[0], food[1], curses.ACS_PI)  #letter pi mnchn toul

#set initial movement direction to right
#key-right huwe right arrow
#key left huwe left arrow
key = curses.KEY_RIGHT
#create game loop that loops forever until player loses or quits the game
while True:
  next_key = window.getch  #getch() ye3ne yesta2bel  get a character
  #if user dosnt input anthing key remains same ,else
  key = key if next_key == -1 else next_key
#   if next_key ==-1
#     key =key
# else:key =next_key

if snake[0][0] in [0, screen_height] or snake[0][1] in [
    0, screen_width
] or snake[0] in snake[1:]:
  curses.endwin()  #closing the window
  quit()  #exit thee prg

new_head = [snake[0][0], snake[0][1]]

if key == curses.KEY_DOWN:
  new_head[0] += 1
if key == curses.KEY_UP:
  new_head[0] -= 1

if key == curses.KEY_RIGHT:
  new_head[1] += 1
if key == curses.KEY_LEFT:
  new_head[1] -= 1
#insert the new head to the first position of snake list

snake.insert(0, new_head)
#check if snake at the food

if snake[0] == food:
  food = None  #remove food if snake at it
  while food is None:
    new_food = [
        random.randint(1, screen_height - 1),  # --.. 1,599
        random.randint(1, screen_width - 1)  # --.. 1,599
    ]
    food = new_food if new_food not in snake else None
  window.addch(food[0], food[1], curses.ACS_PI)
else:
  tail = snake.pop()  #pop btrj3 ekher imi le mawjode bel liste
  window.addch(tail[0], tail[1], '')

window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)