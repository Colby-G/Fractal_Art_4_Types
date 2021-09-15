# Import the turtle module
from turtle import *

# Initializing the turtle
speed(0)
hideturtle()

# Function to define the tree
def tree(size, levels, angle):
    if levels == 0:
        dot(size, "dark green")
        return
    width(levels)
    color("saddle brown")
    forward(size)
    right(angle)
    tree(size * 0.8, levels - 1, angle)
    left(angle * 2)
    tree(size * 0.8, levels - 1, angle)
    right(angle)
    backward(size)


# Called to initiate the turtle cursor for creating the tree
left(90)
tree(90, 11, 22.5)

# Called to keep the turtle screen open
mainloop()
