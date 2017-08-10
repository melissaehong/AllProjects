Optional Assignment: Python Turtle
Try drawing a simple picture using the Python module Turtle.

Turtle is a Python drawing module for kids. It uses Python's built-in ability to test GUI apps as you write the code. Even though it's for kids, you can do some complex drawing with it. Learning new technologies, languages, modules, plugins, and libraries is a very common practice for any programmer. When you learn about something new, make sure to try it, even if it's silly! Being curious is key to being a good developer!

Here is an example of what we can do using Turtle:

# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20
