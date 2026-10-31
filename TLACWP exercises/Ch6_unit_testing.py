# How to think like a computer scientist: chapter 6 exercises 

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
def test_suite(f):
    """ Run the suite of tests for code in this module (this file).
    """
    test(f(17) == 17)
    test(f(-17) == 17)
    test(f(0) == 0)
    test(f(3.14) == 3.14)
    test(f(-3.14) == 3.14)

def test_suite2(f):
    """ Run the suite of tests for code in this module (this file).
    """
    assert(f(17) == 17)
    assert(f(-17) == 17)
    assert(f(0) == 0)
    assert(f(3.14) == 3.14)
    assert(f(-3.14) == 3.14)
'''
'''
def absolute_value(x):
    if x < 0:
        return -x
    return x

def bad_absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

test_suite2(absolute_value)        # Here is the call to run the tests
test_suite(bad_absolute_value)
'''
'''
def turn_clockwise(cp):
    if cp == 'N':
        return 'E'
    elif cp == 'E':
        return 'S'
    elif cp == 'S':
        return 'W'
    elif cp == 'W':
        return 'N'

def test_suite_turn_clockwise(f):
    """ Run the suite of tests for code for the turn_clockwise function. """
    test(f("N") == "E")
    test(f("W") == "N")
    test(f("S") == "W")
    test(f(42) == None)
    test(f("rubbish") == None)

test_suite_turn_clockwise(turn_clockwise)
'''

def day_name(dnum):
    if dnum == 0:
        return 'Su'
    elif dnum == 1:
        return 'Mo'
    elif dnum == 2:
        return 'Tu'
    elif dnum == 3:
        return 'We'
    elif dnum == 4:
        return 'Th'
    elif dnum == 5:
        return 'Fr'
    elif dnum == 6:
        return 'Sa'

'''
def test_suite_day_name(f):
    """ Run the suite of tests for code for the day_name function. """
    test(day_name(3) == "We")
    test(day_name(6) == "Sa")
    test(day_name(42) == None)

# test_suite_day_name(day_name)
'''

def name_day(dnam):
    if dnam == 'Su':
        return 0
    elif dnam == 'Mo':
        return 1
    elif dnam == 'Tu':
        return 2
    elif dnam == 'We':
        return 3
    elif dnam == 'Th':
        return 4
    elif dnam == 'Fr':
        return 5
    elif dnam == 'Sa':
        return 6

'''
def test_suite_name_day(f):
    """ Run the suite of tests for code for the name_day function. """
    test(name_day("Fr") == 5)
    test(name_day("Su") == 0)
    test(name_day(day_name(3)) == 3)
    test(day_name(name_day("Th")) == "Th")
    test(name_day("Halloween") == None)

test_suite_name_day(name_day)
'''
'''
def day_back(dg,db):
    """If the day I go is dg and I come back after db, what day am I coming back (dback)"""
    dnam = name_day(dg)
    dback = (dnam + db) % 7
    return day_name(dback)

def test_suite_day_back(day_back):
    """ Run the suite of tests for code for the day_back function. """
    test(day_back("Mo", 4) ==  "Fr")
    test(day_back("Tu", 0) == "Tu")
    test(day_back("Tu", 14) == "Tu")
    test(day_back("Su", 100) == "Tu")
    test(day_back("Su", -1) == "Sa")
    test(day_back("Su", -10) == "Th")
    test(day_back("Tu", -100) == "Su")

test_suite_day_back(day_back)
'''
'''
def  days_in_month(month):
    if month == 'January' or month == 'March' or month == 'May' or month == 'July' \
        or month == 'August' or month == 'October' or month == 'December':
        return 31
    elif month == 'February':
        return 28
    elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
        return 30

def test_suite_days_in_month(days_in_month):
    """ Run the suite of tests for code for the days_in_month function. """
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month(2019) == None)

test_suite_days_in_month(days_in_month)
'''
'''
def to_secs(h,m,s):
    return int(h*60*60 + m*60 + s)

def test_suite_to_secs(to_secs):
    """ Run the suite of tests for code for the to_secs function. """
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)

test_suite_to_secs(to_secs)
'''
'''
def hours_in(s):
    return int(s/3600)

def minutes_in(s):
    return int(s/60%60)

def seconds_in(s):
    return int(s%60)

def test_suite_3vars():
    """ Run the suite of tests for code for the 3 prior functions. """
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

test_suite_3vars()
'''
'''
def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1

def test_suite_compare():
    """ Run the suite of tests for code for the compare function. """
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    
test_suite_compare()
'''
'''
def hypotenuse(a,b):
    h = (a**2 + b**2)**0.5
    return h

def test_suite_hypotenuse():
    """ Run the suite of tests for code for the hypotenuse function. """
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    
test_suite_hypotenuse()
'''
'''
def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def test_suite_slope():
    """ Run the suite of tests for code for the slope function. """
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    
#test_suite_slope()


def intercept(x1, y1, x2, y2):
    s = slope(x1, y1, x2, y2)
    b = y1 - s*x1
    return b

def test_suite_intercept():
    """ Run the suite of tests for code for the intercept function. """
test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)
    
test_suite_intercept()
'''

def is_even(n):
    return n % 2 == 0
'''
def test_suite_is_even():
    """ Run the suite of tests for code for the is_even function. """
test(is_even(2) == True)
test(is_even(7) == False)
test(is_even(0) == True)
test(is_even(-2) == True)
test(is_even(-5) == False)
    
test_suite_is_even()
'''
'''
def is_odd(n):
    return not is_even(n)

def test_suite_is_odd():
    """ Run the suite of tests for code for the is_odd function. """
test(is_odd(2) == False)
test(is_odd(7) == True)
test(is_odd(0) == False)
test(is_odd(-2) == False)
test(is_odd(-5) == True)
    
test_suite_is_odd()
'''

def is_factor(f,n):
    return n % f == 0
'''
def test_suite_is_factor():
    """ Run the suite of tests for code for the is_factor function. """
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))

test_suite_is_factor()
'''
'''
def is_multiple(m,n):
    return is_factor(n,m)

def test_suite_is_multiple():
    """ Run the suite of tests for code for the is_multiple function. """
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

test_suite_is_multiple()
'''
'''
def f2c(f):
    c = 5 / 9 * (f-32)
    return round(c)

def test_suite_f2c():
    """ Run the suite of tests for code for the f2c function. """
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)

test_suite_f2c()
'''

def c2f(c):
    f = 32 + (c*9/5)
    return round(f)

def test_suite_c2f():
    """ Run the suite of tests for code for the c2f function. """
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

test_suite_c2f()