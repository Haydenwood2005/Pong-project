# simple pong game in python

import turtle #adds graphics and window for basic games

#opening windows screen/ black box terminal for game
window = turtle.Screen() #variable name for thee window that opens. turtle screen is the import 
window.title("Pong by Hayden Wood") #title at the top of the window when file is ran
window.bgcolor("black") #colour of the window when opened
window.setup(width=800, height=600) #size and dimensions of the window when opened
window.tracer(0) #this turns off automatic updates so the screen doesnt keep refreshing itself



##items in window

#wall

wall = turtle.Turtle()
wall.speed(0) 
wall.shape("square")
wall.shapesize(5, 1)
wall.color("white")
wall.penup()
wall.goto(-350, 0)


#wall2

wall2 = turtle.Turtle()
wall2.speed(0) 
wall2.shape("square")
wall2.shapesize(5, 1)
wall2.color("white")
wall2.penup()
wall2.goto(+350, 0)


#ball

ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


##moving wall and wall2








##main game loop so stays open

while True: #keep at bottom so all code is updated in window
        window.update()
