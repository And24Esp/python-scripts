import turtle

def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(name, colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    name = turtle.Turtle()
    name.color(colr,'red')
    name.pensize(sz)
    return name

def draw_poly(turtleName, n, sz):
  for i in range(n):
    turtleName.forward(sz)
    turtleName.left(360/n)

def draw_equitriangle(turtleName, sz):
  draw_poly(turtleName, 3, sz)

def draw_squares(turtleName, diameter):
  for i in range(4):
    for i in range(3):
      turtleName.forward(diameter/2)
      turtleName.right(90)
    turtleName.forward(diameter/2)

def draw_star(turtleName):
  '''
  Draw a 5 point, 100 unit of length star
  '''
  for i in range(5):
    turtleName.forward(100)
    turtleName.right(720/5)

def draw_bar(turtleName, height):
    """ Get turtleName to draw one bar, of height. """
    if height >= 0:
      turtleName.begin_fill()
      turtleName.left(90)
      turtleName.forward(height)    
      turtleName.write('    ' + str(height))
      turtleName.right(90)
      turtleName.forward(40)         
      turtleName.right(90)
      turtleName.forward(height)     
      turtleName.left(90)            
      turtleName.end_fill()
      turtleName.penup()
      turtleName.forward(10)        
      turtleName.pendown()
    if height < 0:
      turtleName.begin_fill()
      turtleName.right(90)
      turtleName.forward(-height)     
      turtleName.penup()
      turtleName.forward(17)
      turtleName.write('    ' + str(height))
      turtleName.forward(-17)
      turtleName.pendown()
      turtleName.left(90)
      turtleName.forward(40)         
      turtleName.left(90)
      turtleName.forward(-height)     
      turtleName.right(90)            
      turtleName.end_fill()
      turtleName.penup()
      turtleName.forward(10)         
      turtleName.pendown()        

wn = make_window("lightgreen", "Animated Bar Chart")

donatello = make_turtle('donatello','blue', 3)
donatello.penup()
donatello.forward(-200)
donatello.pendown()
'''
for i in range(5):
  draw_star(donatello)
  donatello.penup()
  donatello.forward(350)
  donatello.right(144)
  donatello.down()
'''

xs = [48, 117, 200, -24, 160, 0, -160, 220]

for bar in xs:
    if bar >= 200:
      donatello.color('blue','red')
      draw_bar(donatello, bar)
    elif bar >= 100 and bar < 200:
      donatello.color('blue','yellow')
      draw_bar(donatello, bar)
    elif bar < 100:
      donatello.color('blue','green')
      draw_bar(donatello, bar)


wn.mainloop()