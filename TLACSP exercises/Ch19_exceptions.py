'''
filename = input("Enter a file name: ")

try:
    f = open(filename, "r")
except:
    print("There is no file named", filename)
'''
'''
def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age

get_age()
'''
'''
import sys

sys.setrecursionlimit(500)

def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")

recursion_depth(0)
'''
'''
import turtle
import time

def show_poly():
    try:
        win = turtle.Screen()   # Grab/create a resource, e.g. a window
        tess = turtle.Turtle()

        # This dialog could be cancelled,
        #   or the conversion to int might fail, or n might be zero.
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):      # Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)           # Make program wait a few seconds
    finally:
        win.bye()               # Close the turtle's window

show_poly()
show_poly()
show_poly()
'''

def readposint():
    
    try:
        x = int(input('please write a positive integer: '))
    except:
        raise TypeError('That was not an integer, you freak.') 
    
    if x < 0:
        raise ValueError('{0} is a negative integer, dumbass.'.format(x))
    #if x == '':  (this case is already handled in the try/except block).
    #    raise ValueError('{0} please type a freakin numba'.format(x)) 
    if x == 666:
        raise UserWarning('{0}??? Are u the facking devil???'.format(x))
    
    print('Good boy.')
    
readposint()
