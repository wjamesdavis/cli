# Part 5, Objects

import turtle as t

"""
Line 1 is importing the `library` turtle (under the name t)
This is giving us all new functions that are specific to the turtle library

https://docs.python.org/3/library/turtle.html

If you are not feeling super confident with previous topics, 
come back to this later. 
"""

def demo():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break


def drawSquare(turt):
    for i in range(4):
        turt.forward(100)
        turt.left(90)

"""
Task - Write a function that draws a shape that isn't a square, and call that function in main
"""
