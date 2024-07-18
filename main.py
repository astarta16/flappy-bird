
import turtle
import time

wn = turtle.Screen()
wn.title("Flappy Bird by @TokyoEdTech")
wn.bgcolor("blue")
wn.bgpic("background.gif")
wn.setup(width=500, height=800)
wn.tracer(0)

wn.register_shape("bird.gif")


pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))


player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("bird.gif")
player.goto(-200, 0)
player.dx = 0
player.dy = 1

pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(300, 250)
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1

pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -250)
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0

pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_top.goto(600, 280)
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1


pipe2_bottom = turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_bottom.goto(600, -220)
pipe2_bottom.dx = -2
pipe2_bottom.dy = 0


pipe3_top = turtle.Turtle()
pipe3_top.speed(0)
pipe3_top.penup()
pipe3_top.color("green")
pipe3_top.shape("square")
pipe3_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_top.goto(900, 320)
pipe3_top.dx = -2
pipe3_top.dy = 0
pipe3_top.value = 1


pipe3_bottom = turtle.Turtle()
pipe3_bottom.speed(0)
pipe3_bottom.penup()
pipe3_bottom.color("green")
pipe3_bottom.shape("square")
pipe3_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_bottom.goto(900, -180)
pipe3_bottom.dx = -2
pipe3_bottom.dy = 0

gravity = -0.3


def go_up():
    player.dy += 8
    
    if player.dy > 8:
        player.dy = 8

wn.listen()
wn.onkeypress(go_up, "space")

player.score = 0

pipes = [(pipe1_top, pipe1_bottom), (pipe2_top, pipe2_bottom), (pipe3_top, pipe3_bottom)]
