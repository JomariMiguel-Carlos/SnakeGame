#import modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#create the display of the game
wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("yellow")

#set height and width
wn.setup(width=600, height=600)
wn.tracer(0)

#head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

#food in the game
food = turtle.Turtle()
colors = random.choice(['red','blue','pink'])
shapes = random.choice(['square', 'circle', 'triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

#status of the game
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0    High Score: 0", align="center",
          font=("Times New Roman", 24, "bold"))



