# Import the needed libraries
from turtle import *
from colors import colors_list

# Initializing the turtle
speed(0)
hideturtle()

# Function to define a single flower side
def flower_petal(length):
    length /= 5
    for _ in range(5):
        right(72)
        forward(length)

# Function to create a single level of the flower
def create_flower(petal, length):
    cl_index = 0
    for _ in range(petal):
        if cl_index >= 124:
            cl_index = 0
        color(colors_list[cl_index])
        flower_petal(length)
        right(length / petal)
        length -= length / petal
        cl_index += 1


# Called to create the flower
create_flower(200, 1200)

# Called to keep the turtle screen open
mainloop()
