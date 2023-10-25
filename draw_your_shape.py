from turtle import Turtle, Screen

tim = Turtle("triangle")

screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_backward, key="Down")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
