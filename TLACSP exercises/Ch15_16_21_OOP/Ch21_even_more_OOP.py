from unit_tester import test

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """
        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return '{0}:{1}:{2}'.format(self.hours, self.minutes, self.seconds)

    def increment(self, seconds):
        self.__init__(0, 0, self.to_seconds() + seconds)    #Exercise 4
        """
        # Another interesting approach:
        incremented_obj = MyTime(0, 0, self.to_seconds() + seconds) #Exercise 4
        self.__dict__.update(incremented_obj.__dict__)  #Exercise 4        
        
        # the reason/s behind the 2 prior approaches are detailed on the following link:
        # https://stackoverflow.com/questions/1216356/is-it-safe-to-replace-a-self-object-by-another-object-of-the-same-type-in-a-meth
        
        #Method before modification made for exercise 4 (chapter 21 theory section):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        """

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __gt__(self, time2):     #Modification in name due to exercise 3
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def between(self, other1, other2):
        """Returns True if obj falls between other1 & other2"""
        return self.to_seconds() >= other1.to_seconds() and \
        self.to_seconds() <= other2.to_seconds()
    

tim1 = MyTime(11, 59, 30)

#print(tim1)
'''
#PURE FUNCTION example for adding time:
def add_time(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds
    sum_t = MyTime(h, m, s)
    return sum_t

current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
#print(done_time)
'''

#MODIFIER FUNCTION example for incrementing time:
def increment(t, seconds):
    t.seconds += seconds

    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes += 1

    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1
    
#increment(bread_time,5000)
#print(bread_time)

#current_time.increment(500)
#print(current_time)

#Improved PURE FUNCTION example for adding time:
def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)

current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = add_time(current_time, bread_time)
#print(done_time)

if current_time > done_time:   #overload operator implemented (exercise 3)
    print("The bread will be done before it starts!")

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t2 - t1
#print(t3)

#Exercise 1:
def between(obj1, obj2, obj3):
    """Returns True if obj1 falls between obj2 & obj3"""
    return obj1.to_seconds() >= obj2.to_seconds() and \
    obj1.to_seconds() <= obj3.to_seconds()

t4 = MyTime(4, 00, 40)
'''
test(between(t2, t1, t4) == True)
test(between(t4, t1, t2) == False)
test(t2.between(t1, t4) == True)    #test for exercise 2
test(t4.between(t1, t2) == False)   #test for exercise 2
'''

#Test cases for exercise 4 (exercises 5 and 6):
print(t4)
t4.increment(3666)
print(t4)
t4.increment(-3666)
print(t4)
t4.increment(-20000)
print(t4)

