# from turtle import *
# tommy = Turtle()
# print(tommy.shape)
# tommy.shape('turtle')
# tommy.color('red')
# tommy.forward(100)

# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Pokemon Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)