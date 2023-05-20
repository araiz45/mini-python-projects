
import turtle
import os
from playsound import playsound

player_a_name = (input("Enter Player A Name : ") or "Player A")
player_b_name = (input("Enter Player B Name : ")or "Player B")

wind = turtle.Screen()
wind.title("Pong game by Aaraiz Baig")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(1)

# print("hello world")
# Score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# paddle_b.circle(radius=90)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0 | {} : 0".format(player_a_name, player_b_name), align="center", font= ["san-serif", 20, "bold"])

new_pen = turtle.Turtle()
new_pen.speed(0)
new_pen.color("white")
new_pen.penup()
new_pen.hideturtle()
new_pen.goto(0, 205)
new_pen.write("ehllo", align="center", font= ["san-serif", 20, "bold"])

# Paddle A up function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Paddle A down function
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)



# Paddle B up function
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Paddle B down function
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



#keyboard binding
wind.listen()
wind.onkeypress(paddle_a_up, "w")
wind.onkeypress(paddle_a_down, "s")
wind.onkeypress(paddle_b_up, "Up")
wind.onkeypress(paddle_b_down, "Down")
# Main game loop
while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{} : {} | {}: {}".format(player_a_name,score_a,player_b_name, score_b), align="center", font= ["san-serif", 20, "bold"])
        playsound("sucess.mp3")
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(" {}: {} | {} : {}".format(player_a_name ,score_a,player_b_name, score_b), align="center", font= ["san-serif", 20, "bold"])
        playsound("sucess.mp3")
    # paddle and ball collition
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        playsound('ball.mp3')

    # paddle and ball collition
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        playsound('ball.mp3')


    if score_a == 1 or score_b == 1:
        # wind.clear()
        wind.bye()
        if score_a > score_b:
            print("{} wins the match by {}".format(player_a_name, score_a))
        if score_b > score_a:
            print("{} wins the match by {}".format(player_b_name, score_a))
            
     



