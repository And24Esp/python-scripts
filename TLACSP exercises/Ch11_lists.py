import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

'''
def add_vectors(u,v):
    """ Takes two lists of numbers of the same length, and returns a new 
    list containing the sums of the corresponding elements of each"""
    new_list = []
    for i in range(len(u)):
        sum_elements = u[i] + v[i]
        new_list.append(sum_elements)
    return new_list

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
'''
'''
def scalar_mult(s, v):
    """Takes a number, s, and a list, v, and returns the scalar multiple of v by s"""
    new_list = []
    for i in range(len(v)):
        multiplied_elements = s * v[i]
        new_list.append(multiplied_elements)
    return new_list

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
'''
'''
def dot_product(u,v):
    """ Takes two lists of numbers of the same length, and returns 
    the sum of the products of the corresponding elements of each"""
    dotProduct = 0
    for i in range(len(u)):
        sum_elements = u[i] * v[i]
        dotProduct += sum_elements
    return dotProduct

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
'''

def replace(s, old, new):
    """Write a function replace(s, old, new) that replaces 
    all occurrences of old with new in a string s"""
    return new.join(s.split(old))

test(replace("Mississippi", "i", "I") == "MIssIssIppI")
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")
test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

'''
def swap(x, y):         #WORKING VERSION 
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)
    return (x,y)        #inclusion of return keyword

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
(a,b) = swap(a, b)      #assignment of swapped values
print("after swap function call: a:", a, "b:", b)
'''