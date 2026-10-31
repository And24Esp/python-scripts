'''
import turtle

turtle.setup(1000,500)               # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

# Direction handlers:
def goForward():
   tess.forward(30)

def goBackwards():
   tess.forward(-30)

def turnLeft():
   tess.left(45)

def turnRight():
   tess.right(45)

# Color handlers:
def RaisePen():
   tess.penup()

def PutDownPen():
   tess.pendown()

# Color handlers:
def Red():
   tess.color('red')

def Green():
   tess.color('lightgreen')

def Blue():
   tess.color('blue')

def Black():
   tess.color('black')

# Pen size handlers:
sz = 1

def BiggerSize():
    global sz 
    sz += 1
    if sz <= 20:
        tess.pensize(sz)
    else:
        sz -= 1

def SmallerSize():
    global sz 
    sz -= 1
    if sz >= 1:
        tess.pensize(sz)
    else:
        sz += 1

# Window handlers:

def smallWindow():
    turtle.setup(500,400)

def mediumWindow():
    turtle.setup(800,500)

def bigWindow():
    turtle.setup(1100,600)

def closeWindow():
    wn.bye()                        # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkeypress(goForward, "Up")
wn.onkeypress(goBackwards, "Down")
wn.onkeypress(turnLeft, "Left")
wn.onkeypress(turnRight, "Right")

wn.onkey(Red, "r")
wn.onkey(Green, "g")
wn.onkey(Blue, "b")
wn.onkey(Black, "k")

wn.onkey(BiggerSize, "+")
wn.onkey(SmallerSize, "-")

wn.onkey(RaisePen, "u")
wn.onkey(PutDownPen, "d")

wn.onkey(smallWindow, "1")
wn.onkey(mediumWindow, "2")
wn.onkey(bigWindow, "3")
wn.onkey(closeWindow, "q")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its handler will be called.
wn.listen()
wn.mainloop()
'''
'''
import turtle

turtle.setup(500,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

def h1(x, y):
   wn.title("Got click at coords {0}, {1}".format(x, y))
   tess.goto(x, y)

wn.onclick(h1)  # Wire up a click on the window.
wn.mainloop()
'''
'''
import turtle

turtle.setup(400,500)              # Determine the window size
wn = turtle.Screen()               # Get a reference to the window
wn.title("Handling mouse clicks!") # Change the window title
wn.bgcolor("lightgreen")           # Set the background color
tess = turtle.Turtle()             # Create two turtles
tess.color("purple")
alex = turtle.Turtle()             # Move them apart
alex.color("blue")
alex.forward(100)

def handler_for_tess(x, y):
    wn.title("Tess clicked at {0}, {1}".format(x, y))
    tess.left(42)
    tess.forward(30)

def handler_for_alex(x, y):
    wn.title("Alex clicked at {0}, {1}".format(x, y))
    alex.right(84)
    alex.forward(50)

tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.mainloop()
'''
'''
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

def h1():
    tess.forward(100)
    tess.left(56)

wn.ontimer(h1, 2000)
wn.mainloop()
'''
'''
import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer to get events!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")

def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 60)

h1()
wn.mainloop()
'''
'''
import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.penup()
    tess.right(90)
    tess.forward(100)
    tess.left(90)
    tess.pendown()
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 2000)
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine, 10000)
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 8000)

# Bind the event handler to the space key.
advance_state_machine()

wn.listen()                      # Listen for events
wn.mainloop()
'''

import turtle           # Tess and 2 other friends become traffic lights (traffic lights v2).

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess and 2 other friends become traffic lights!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
dona = turtle.Turtle()
rafa = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.penup()
    tess.forward(-50)
    tess.right(90)
    tess.forward(100)
    tess.left(90)
    tess.pendown()
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

# Position tess onto the place where the green light should be
tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# Position dona onto the place where the orange light should be
dona.penup()
dona.forward(-10)
dona.left(90)
dona.forward(20)
# Turn dona into a big black circle
dona.shape("circle")
dona.shapesize(3)
dona.fillcolor("black")

# Position rafa onto the place where the red light should be
rafa.penup()
rafa.forward(-10)
rafa.left(90)
rafa.forward(90)
# Turn rafa into a big black circle
rafa.shape("circle")
rafa.shapesize(3)
rafa.fillcolor("black")

# A traffic light is a kind of state machine with three states,
# Green, Green/Orange, Orange, Red.  We number these states  0, 1, 2, 3

# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        dona.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.fillcolor("black")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 2:     # Transition from state 2 to state 3
        dona.fillcolor("black")
        rafa.fillcolor("red")
        state_num = 3
        wn.ontimer(advance_state_machine, 3000)
    else:                    # Transition from state 3 to state 0
        rafa.fillcolor("black")
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)

advance_state_machine()

wn.mainloop()
