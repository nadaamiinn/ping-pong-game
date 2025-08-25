import turtle
import random
import pygame
import time


wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("#1B2631")
wind.setup(width=800, height=600)
wind.tracer(0)

pygame.init()
success_sound = pygame.mixer.Sound("D:\projects\Game_Project\pythonProject\success.wav")

# Paddle 1 (left)
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("#3525DC")
madrab1.shapesize(stretch_wid=6, stretch_len=0.5)
madrab1.penup()
madrab1.goto(-370, 0)

# Paddle 2 (right) - AI Controlled
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("#EE2D2D")
madrab2.shapesize(stretch_wid=6, stretch_len=0.5)
madrab2.penup()
madrab2.goto(370, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#F4D03F")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

#Center Line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_wid=25, stretch_len=0.1)
center_line.penup()
center_line.goto(0, 0)

# score variables
score1_value = 0
score2_value = 0

# player 1 score display
score1_display = turtle.Turtle()
score1_display.speed(0)
score1_display.color("#3498DB")
score1_display.penup()
score1_display.hideturtle()
score1_display.goto(-225, 260)
score1_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# player 2 score display
score2_display = turtle.Turtle()
score2_display.speed(0)
score2_display.color("#CB4335")
score2_display.penup()
score2_display.hideturtle()
score2_display.goto(225, 260)
score2_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move the left paddle
def madrab1_up():
    y = madrab1.ycor()
    if y < 250:
        y += 40
    madrab1.sety(y)
def madrab1_down():
    y = madrab1.ycor()
    if y > -240:
        y -= 40
    madrab1.sety(y)

# Keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "Up")
wind.onkeypress(madrab1_down, "Down")

#minmax search
def minimax(ball_y, madrab2_y):
    if ball_y > madrab2_y:
        return 1
    elif ball_y < madrab2_y:
        return -1
    else:
        return 0

# AI function to control the second paddle using Minimax
def ai_move():
    decision = minimax(ball.ycor(), madrab2.ycor())
    if decision == 1:
        madrab2.sety(madrab2.ycor() + 5)
    elif decision == -1:
        madrab2.sety(madrab2.ycor()-5)

# Main game loop
while True:
    wind.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1_value += 1
        score1_display.clear()
        score1_display.write("Score: {}".format(score1_value), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2_value += 1
        score2_display.clear()
        score2_display.write("Score: {}".format(score2_value), align="center", font=("Courier", 24, "normal"))
    # Check if the game is over
    if score1_value == 5 or score2_value == 5:
        winner = "BLUE" if score1_value == 5 else "RED"
        
        over_display = turtle.Turtle()
        over_display.speed(0)
        over_display.color("blue" if winner == "BLUE" else "red")
        over_display.penup()
        over_display.hideturtle()
        over_display.goto(0, 0)
        over_display.write(f"{winner} Wins!", align="center", font=("Courier", 36, "bold"))
        
        success_sound.play()      
        wind.update()             
        time.sleep(2)          
        break                    


    # Paddle collision with ball
    if (340 < ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
    
    # AI Move
    ai_move()

turtle.done() #keep the Turtle graphics window open.