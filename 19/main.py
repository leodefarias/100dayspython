from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Faça a sua aposta!", prompt='Qual tartaruga vai ganhar a corrida?')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'Você venceu! A tartaruga vencedora é {winning_color}!')
            else:
                print(f'Você perdeu! A tartaruga vencedora é {winning_color}')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()