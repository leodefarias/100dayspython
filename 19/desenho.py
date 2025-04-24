from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def spin_clockwise():
    tim.right(15)
def spin_counter_clockwise():
    tim.left(15)
def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=spin_clockwise)
screen.onkey(key='a', fun=spin_counter_clockwise)
screen.onkey(key='space', fun=clear)
screen.exitonclick()