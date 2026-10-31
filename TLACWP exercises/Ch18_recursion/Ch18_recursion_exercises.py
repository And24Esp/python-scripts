from unit_tester import test
'''
#Exercise 1:
import turtle

w = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.forward(-300)
t.pendown()

#count = 0

def koch(t, order, size):
    """Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction."""
    global count
    #count += 1
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
    #return count

koch(t, 2, 300)
t.right(120)
koch(t, 2, 300)
t.right(120)
koch(t, 2, 300)
t.right(120)

w.mainloop()
'''
'''
#Exercise 2a:
import turtle

w = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.forward(-300)
t.pendown()

#count = 0

def cesaro(t, order, size):
    """Make turtle t draw a cesaro fractal of 'order' and 'size'.
       Leave the turtle facing the same direction."""
    global count
    #count += 1
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        cesaro(t, order-1, size/3)   # Go 1/3 of the way
        t.right(85)
        cesaro(t, order-1, size/3)
        t.left(170)
        cesaro(t, order-1, size/3)
        t.right(85)
        cesaro(t, order-1, size/3)
    #return count

cesaro(t, 3, 400)

w.mainloop()
'''
'''
#Exercise 2b (not so satisfied with the solution I provided):
import turtle

w = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.forward(0)
t.pendown()

def cesaro_square(t, order, size):
    """Make turtle t draw a cesaro_square fractal of 'order' and 'size'.
       Leave the turtle facing the same direction."""
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        for j in range(4):
            for i in range(4):
                cesaro_square(t, order-1, size/3)   # Go 1/3 of the way
                t.right(85)
                cesaro_square(t, order-1, size/3)
                t.left(170)
                cesaro_square(t, order-1, size/3)
                t.right(85)
                cesaro_square(t, order-1, size/3)
                t.right(89)     #next square's corner
            t.left(266)

cesaro_square(t,1, 300)
w.mainloop()
'''
'''
#Exercise 3 & 4
#Ex3 is complete, Ex4 is completed at a 10% more or less (only "depth 0" is done)
import turtle

w = turtle.Screen()
#w.bgcolor('black')
t = turtle.Turtle()
t.penup()
t.forward(-150)
t.pendown()

def Sierpinski_triangle(t, order, size, colorChangeDepth=-1):
    """Make turtle draw a Sierpinski triangle fractal of n order & size"""
    if order == 0:
        t.left(60)
        t.forward(size)
        t.left(-120)
        t.forward(size)
        t.left(-120)
        t.forward(size)
        t.left(180)
    else:
        #t.color('red')  # not requiered for Ex3
        Sierpinski_triangle(t, order-1, size/2)
        t.penup()   # not requiered for Ex3
        t.left(60)
        t.forward(size/2)
        t.left(-60)
        t.pendown() # not requiered for Ex3
        #t.color('magenta')  # not requiered for Ex3
        Sierpinski_triangle(t, order-1, size/2)
        t.penup() # not requiered for Ex3
        t.left(-60)
        t.forward(size/2)
        t.left(60)
        t.pendown() # not requiered for Ex3
        #t.color('blue') # not requiered for Ex3
        Sierpinski_triangle(t, order-1, size/2)
        t.penup() # not requiered for Ex3
        t.left(180)
        t.forward(size/2)
        t.left(-180)    #Finally works! :)
        t.pendown() # not requiered for Ex3

Sierpinski_triangle(t, 4, 300)

w.mainloop()
'''
'''
# Exercise 5
def recursive_min(recursive_list):
    """ Find the minnimum in a recursive structure of lists within 
    other lists. Precondition: No lists or sublists are empty"""
    smallest = None
    first_time = True
    for e in recursive_list:
        if type(e) == type([]):
            val = recursive_min(e)
        else:
            val = e

        if first_time or val < smallest:
            smallest = val
            first_time = False
    return smallest

test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
'''
'''
# Exercise 6:
def count(target, nested_list):
    
    counter = 0

    def count(target, nested_list):
        nonlocal counter
        for e in nested_list:
            if type(e) == type([]):
                count(target,e)
            if e == target:
                counter += 1
        return counter

    return count(target, nested_list)

test(count(2, []) == 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
test(count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
'''
'''
# Exercise 7:
def flatten(nested_list):
    flat_list = []
    def flatten2(nested_list):
        nonlocal flat_list
        for d in nested_list:
            if type(d) == type(1) or type(d) == type('a'):
                flat_list.append(d)
            else:
                flatten2(d)
        return flat_list
    return flatten2(nested_list)

test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
              ["this","a","thing","a","is","a","easy"])
test(flatten([]) == [])
'''
'''
#Exercise 8:
def fib(n):
    """ Fibonacci function that doesn't use recursion"""
    fib_minus_2 = 0
    fib_minus_1 = 1
    total = 0
    for i in range(1,n):
        total = fib_minus_1 + fib_minus_2
        fib_minus_2 = fib_minus_1
        fib_minus_1 = total
    return total

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
test(fib(200) == 280571172992510140037611932413038677189525)
'''
'''
#Exercise 9:
import sys
print(sys.getrecursionlimit())  #this one starts with "get"
sys.setrecursionlimit(500)     #this one starts with "set"

def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)

recursion_depth(0)
'''
'''
#Exercise 10:
import os

def get_dirlist(path):
    """Return a sorted list of all entries in path."""
    
    path_list = []

    def get_dirlist2(path):
        nonlocal path_list
        dirlist = os.listdir(path)
        for f in dirlist:
            fullname = os.path.join(path, f)   # Turn name into full pathname
            if os.path.isdir(fullname):
                get_dirlist2(fullname)
            else:
                path_list.append(fullname)

    get_dirlist2(path)

    return path_list

print("\n".join(get_dirlist('C:\\Users\\ecues\\OneDrive\\Documentos\\03 \
Academico\\03 Computer Science\\Statistics')))  #Added .join for readability purposes.
#print(get_dirlist('C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\03 \
#Computer Science\\Data science\\IBM DS Professional Certificate'))
'''
