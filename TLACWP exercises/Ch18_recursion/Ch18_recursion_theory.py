from unit_tester import test
'''
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
        t.right(60)
        koch(t, order-1, size/3)
        t.left(120)
        koch(t, order-1, size/3)
        t.right(60)
        koch(t, order-1, size/3)
    #return count

#print(koch(t, 2, 300))
koch(t, 3, 300)
w.mainloop()
'''
'''
def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

test(r_max([2, 9, [1, 13], 8, 6]) == 13)
test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
test(r_max(["joe", ["sam", "ben"]]) == "sam")
'''
'''
def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)

recursion_depth(0)
'''
'''
def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

print(fib(3))
'''

import os

def get_dirlist(path):
    """Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names."""
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")

print_files('C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\02 Computer Science')
#print_files('C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\03 Computer \
#Science\\Data science\\IBM DS Professional Certificate')

'''
import pygame, math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 1024
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.29       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos)
   pygame.draw.circle(main_surface, color, (int(posn[0]), int(posn[1])), 3)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (255, 0, 0)
          color2 = (0, 0, 255)
      else:
          color1 = color
          color2 = color

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1)
      draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1)


def gameloop():

    theta = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta += 0.01

        # Draw everything
        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(120)

gameloop()
pygame.quit()
'''
'''
# ADDITIONAL: Interesting approach for creating a Sierpinski triangle fractal
# http://bopace.github.io/python/2016/06/09/python-turtle-sierpinski/
import turtle

# function to have the turtle draw a triangle, the basic unit of our fractal
def draw_triangle(vertices,color,my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0],vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0],vertices[1][1])
    my_turtle.goto(vertices[2][0],vertices[2][1])
    my_turtle.goto(vertices[0][0],vertices[0][1])
    my_turtle.end_fill()
    
# the same midpoint function we wrote for the chaos game
def midpoint(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]
    
# recursive function that draws the different "levels" of the fractal
def draw_fractal(vertices,level,my_turtle):
    # the different colors we'll use to draw the fractals
    # in RGB format
    colors = [(0,150,189),(4,150,116),(216,95,30),(193,33,57),(129,41,199),
                (102,205,135),(51,187,204)]
    draw_triangle(vertices,colors[level],my_turtle)
    # call function recursively to draw all levels of fractal
    if level > 0:
        # draw first segment of fractal
        # the vertices being passed in are the bottom corner of the first
        # section, the bottom corner of the second section, and the bottom
        # corner of the third secion.
        draw_fractal([vertices[0],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, my_turtle)
        draw_fractal([vertices[1],
                      midpoint(vertices[0], vertices[1]),
                      midpoint(vertices[1], vertices[2])],
                      level - 1, my_turtle)
        draw_fractal([vertices[2],
                      midpoint(vertices[2], vertices[1]),
                      midpoint(vertices[0], vertices[2])],
                      level - 1, my_turtle)

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
screen = turtle.Screen()
screen.colormode(255) # to use the RGB codes for the colors
vertices = [[-200, -100], [0, 200], [200, -100]]
level = 2 # how many recursions deep do we want to draw the fractal
draw_fractal(vertices, level, my_turtle)
screen.exitonclick()
'''