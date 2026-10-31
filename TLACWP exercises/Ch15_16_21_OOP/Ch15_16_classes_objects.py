from unit_tester import test

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):    # All we have done is renamed the method
        return "({0},{1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    #EXERCISES:
    def distance(self, p2):
        import math
        return math.sqrt( (p2.x-self.x)**2 + (p2.y-self.y)**2 )

    def reflect_x(self):
        return Point(-self.x,self.y)

    def slope_from_origin(self):
        return self.y / self.x    #Doens't work if x equals 0

    def get_line_to(self, p2):
        slope = (p2.y-self.y) / (p2.x-self.x)
        y_intercept = self.y - slope * self.x 
        return slope, y_intercept #Doens't work if (x2 - x1) equals 0

'''
#Tests class Point:
p = Point(3, 4)
q = Point(1,2)
r = Point(4,6)
print(q.distance(r))
print(q.reflect_x())
print(Point(4, 10).slope_from_origin())
print(Point(4, 11).get_line_to(Point(6, 15)))
'''

class SMS_store:
    """Instantiate SMS_store objects, similar to an inbox or outbox on phones"""
    
    def __init__(self, SMS_list=[]):
        self.SMS_list = SMS_list

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ Makes new SMS tuple, inserts it after other messages in the store. 
        When creating this message, its has_been_viewed status is set False."""
        self.SMS_list.append((False, from_number, time_arrived, text_of_SMS))
    
    def message_count(self):
        """Returns the number of sms messages in my_inbox"""
        return len(self.SMS_list)
    
    def get_unread_indexes(self):
        """# Returns list of indexes of all not-yet-viewed SMS messages"""
        index_list = []
        for i in range(len(self.SMS_list)):
            if self.SMS_list[i][0] == False:
                index_list.append(i)
        return index_list

    def get_message(self, i):
        """Return (from_number, time_arrived, text_of_sms) for message[i].
        Also change its state to "has been viewed". If there is no message 
        at position i, return None"""
        if i > (len(self.SMS_list)-1):
            return None
        self.SMS_list[i] = (True,) + self.SMS_list[i][1:] 
        return self.SMS_list[i][1:4]  

    def delete(self,i):
        """ Delete the message at index i"""
        del self.SMS_list[i]

    def clear(self):
        """ # Delete all messages from store object"""
        self.SMS_list = []

'''
#Tests class SMS_store:
my_inbox = SMS_store()
my_inbox.add_new_arrival('0995286757', '15:31', 'Hello from A')
my_inbox.add_new_arrival('0998137703', '16:24', 'Hello from Z')
print(my_inbox.SMS_list)    #Checkpoint
print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(1))
my_inbox.add_new_arrival('0999800846', '17:40', 'Hello baby R')
my_inbox.add_new_arrival('0998947220', '18:03', 'Hello from M')
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(2))
print(my_inbox.SMS_list)    #Checkpoint
print(my_inbox.get_unread_indexes())
my_inbox.delete(1)
print(my_inbox.SMS_list)    #Checkpoint
my_inbox.clear()
print(my_inbox.message_count())
'''

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """Returns the area of any instance"""
        return self.width * self.height
    
    def perimeter(self):
        """Find the perimeter of any rectangle instance"""
        return self.width * 2 + self.height * 2
    
    def flip(self):
        """Swaps the width and the height of any rectangle instance"""
        (self.width, self.height) = (self.height, self.width)
    
    def contains(self, coordenate):
        """Test if a Point falls within the rectangle object"""
        if coordenate.x >= self.corner.x and \
            coordenate.x < self.corner.x + self.width and \
            coordenate.y >= self.corner.y and \
            coordenate.y < self.corner.y + self.height:
            return True
        else:
            return False
    
    def top_right_corner(self):
        """Return coordinates of rectangle's top right corner"""
        new_X = self.corner.x + self.width
        return Point(new_X, self.corner.y)
    
    def bottom_left_corner(self):
        """Return coordinates of rectangle's bottom left corner"""
        new_Y = self.corner.y + self.height
        return Point(self.corner.x, new_Y)

    def bottom_right_corner(self):
        """Return coordinates of rectangle's bottom right corner"""
        new_X = self.corner.x + self.width
        new_Y = self.corner.y + self.height
        return Point(new_X, new_Y)

'''
box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
print("box: ", box)
print("bomb: ", bomb)
'''
'''
r = Rectangle(Point(10,5), 100, 50)
print(r)
r.grow(25, -10)
print(r)
r.move(-10, 10)
print(r)
'''
'''
r = Rectangle(Point(0, 0), 10, 5)
print(r.top_right_corner())
print(r.bottom_left_corner())
print(r.bottom_right_corner())
'''

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

'''
p1 = Point(3, 4)   #Different objects, differente memory adresses 
p2 = Point(3, 4)   #Different objects, differente memory adresses
print(same_coordinates(p1, p2))

#SAMENESS & COPYING:
print(p1 is p2)    #Evaluates to False 
print(p1 == p2)    #Evaluates to False, so == on Point objects test for SHALLOW equality (don't share reference)

l1 = [3,4]         #Different objects, differente memory adresses
l2 = [3,4]         #Different objects, differente memory adresses
print(l1 is l2)    #Evaluates to False
print(l1 == l2)    #Evaluates to True, so == on List objects test for DEEP equality (share values, but NOT reference)
'''
'''
r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
'''
'''
r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter() == 30)
'''
'''
r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)
'''
'''
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))
'''

def collide(rectangle1, rectangle2):
    """Determine whether two rectangles collide. WARNING: This function
    works properly when rectangle2 area is <= than rectangle1's"""  
    return rectangle1.contains(rectangle2.corner) or \
        rectangle1.contains(rectangle2.top_right_corner()) or \
        rectangle1.contains(rectangle2.bottom_left_corner()) or \
        rectangle1.contains(rectangle2.bottom_right_corner())


#Test cases validating if rectangle2 Corner is contained within rectangle1 Area:
test(collide(Rectangle(Point(0, 0), 10, 5),Rectangle(Point(9, 4), 10, 5))==True)
test(collide(Rectangle(Point(0, 0), 10, 5),Rectangle(Point(10, 4), 10, 5))==False)
test(collide(Rectangle(Point(0, 0), 10, 5),Rectangle(Point(0, 0), 2, 1))==True)
test(collide(Rectangle(Point(0, 0), 10, 5),Rectangle(Point(0, 5), 2, 1))==False)
test(collide(Rectangle(Point(3, 4), 7, 6),Rectangle(Point(0, 0), 2, 3))==False)
#Test cases validating if rectangle2 Area is contained within rectangle1 Area:
test(collide(Rectangle(Point(3, 4), 7, 6),Rectangle(Point(2, 3), 2, 3))==True)
test(collide(Rectangle(Point(3, 4), 7, 6),Rectangle(Point(1, 2), 2, 3))==True)
test(collide(Rectangle(Point(3, 4), 7, 6),Rectangle(Point(0, 0), 2, 3))==False)
test(collide(Rectangle(Point(3, 4), 7, 6),Rectangle(Point(2, 2), 2, 3))==True)
test(collide(Rectangle(Point(3, 5), 7, 6),Rectangle(Point(4, 2), 2, 3))==True)
test(collide(Rectangle(Point(3, 5), 7, 6),Rectangle(Point(9,11), 2, 3))==False)