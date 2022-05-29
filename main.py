import turtle

wn = turtle.Screen()
wn.title("Pong - @DanielBankss")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score System
score_a = 0
score_b = 0

gameWon = False

# Paddle
class Paddle:
    def __init__(self, startX):
        self.startX = startX

    def setup(self):
        pad = turtle.Turtle()
        pad.speed(0)
        pad.shape("square")
        pad.color("white")
        pad.shapesize(stretch_wid=5, stretch_len=1)
        pad.penup()
        pad.goto(self.startX, 0)
        return pad


# ----- Game Objects -----
# Paddle A
paddle_a = Paddle(-350).setup()

# Paddle B
paddle_b = Paddle(350).setup()

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Game Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# -------------------------------------- #
# ----- Keyboard Bindings ----- #
wn.listen()

# Paddle A Keybinds
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# Paddle B Keybinds
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# -------------------------------------- #

# Game Loop
while not gameWon:
    wn.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking Borders

    # Top
    if paddle_a.ycor() > 240:
        paddle_a.sety(240)
    elif paddle_a.ycor() < -240:
        paddle_a.sety(-240)

    if paddle_b.ycor() > 240:
        paddle_b.sety(240)
    elif paddle_b.ycor() < -240:
        paddle_b.sety(-240)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()

        if score_a >= 10:
            gameWon = True
            pen.write(f"Player A has won the game!", align="center", font=("Courier", 24, "normal"))
            wn.exitonclick()
        else:
            pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()

        if score_b >= 10:
            gameWon = True
            pen.write(f"Player B has won the game!", align="center", font=("Courier", 24, "normal"))
            wn.exitonclick()
        else:
            pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    # Paddle - Ball Collisions
    if 340 < ball.xcor() < 350 and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1