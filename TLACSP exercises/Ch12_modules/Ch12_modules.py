'''
import calendar

#cal = calendar.TextCalendar()      # Create an instance
#cal.pryear(2020)                   # What happens here?

#d = calendar.LocaleTextCalendar(6, "FRENCH")
#d.pryear(2012)

#cal.prmonth(2020, 12)

#print(calendar.isleap(2020))
'''
'''
import copy

l= (7, [3, 0, 5, 11, 2])

c = copy.copy(l)

d= copy.deepcopy(l)

print(c is l)
print(d is l)
print(c is d)
'''

from unit_tester import test

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    s2 = ' '.join(s.split())
    return new.join(s2.split(old))

test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")
