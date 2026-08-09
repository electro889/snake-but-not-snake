import turtle
import time
pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed(0)
pen.hideturtle()
dh = {}
pen.color("green")
d=time.time()
def turn_left():
  pen.left(90)
def turn_right():
  pen.right(90)
while True:
  pen.forward(1)
  pos = (round(pen.xcor()), round(pen.ycor()))
  screen.listen()
  screen.onkey(turn_left, "Left")
  screen.onkey(turn_right, "Right")
  if pos in dh or pen.xcor()>375 or pen.xcor()<-375 or pen.ycor()>325 or pen.ycor()<-325:
    pen.up()
    pen.goto(0,0)
    pen.down()
    pen.write(time.time()-d)
    screen.mainloop()
    hsajshdksadahkjdhkjdhkjasd
  dh[pos] = True