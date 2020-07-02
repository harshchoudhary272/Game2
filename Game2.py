import turtle

win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("black")
win.setup(width = 800,height = 600)
win.tracer(0)

#scoring/pointing

score_a = 0
score_b = 0

#paddle_a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle_b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2


# scoring

score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: 0   Player B: 0", align = "center", font =( "Courier", 24, "normal"))
#function to move the paddle_a

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#function to move the paddle_b

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# key bindings

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")    
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while True:
    win.update()

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
        score.clear()
        score.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font =( "Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font =( "Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    
