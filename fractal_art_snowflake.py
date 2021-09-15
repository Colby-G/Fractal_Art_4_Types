# Import the turtle module
from turtle import *

# Initializing the turtle
speed(0)
hideturtle()

# Function to define a single snowflake side
def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    color("cyan")
    length /= 3
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

# Function to create the snowflake
def create_snowflake(sides, length):
    for _ in range(sides):
        snowflake_side(length, sides)
        right(360 / sides)


# Called to initiate the turtle cursor for creating the snowflake
create_snowflake(3, 200)

# Called to keep the turtle screen open
mainloop()
