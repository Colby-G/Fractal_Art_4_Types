# Import the needed libraries
from turtle import *
import random

# Initializing the turtle
speed(0)
hideturtle()
colors = ["blue", "deep sky blue", "cyan", "spring green", "dark green", "lime", "olive", "yellow", "gold", "orange", "maroon", "orange red", "red", "light coral", "deep pink", "medium violet red", "purple", "magenta", "medium orchid", "dark violet", "medium slate blue"]

# Function to define a single flower side
def flower_petal(length):
    length /= 3
    for _ in range(5):
        right(72)
        forward(length)

# Function to create a single level of the flower
def create_flower(petal, length, increment):
    while length > 0:
        for _ in range(petal):
            color(random.choice(colors))
            flower_petal(length)
            right(360 / petal)
        length -= increment


# Called to create the flower
create_flower(8, 600, 72)

# Called to keep the turtle screen open
mainloop()
