
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

def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

def test_suite_mysum():
    """ Run the suite of tests for code for the mysum function. """
    test(mysum([1, 2, 3, 4]) == 10)
    test(mysum([1.25, 2.5, 1.75]) == 5.5)
    test(mysum([1, -2, 3]) == 2)
    test(mysum([ ]) == 0)
    test(mysum(range(11)) == 55)  # 11 is not included in the list.
    
test_suite_mysum()
'''
'''
def seq3np1(n):
    """ Print the Collatz conjecture sequence from n,
        terminating when it reaches 1.
    """ 
    while n != 1:
        count = count + 1
        print(n, end=", ")
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n, end=".\n")

seq3np1(998)
'''
'''
def num_digits(n):
    count = 0
    if n == 0:
        count = 1
    while n != 0:
        count = count + 1
        n = int(n/10)
    return count

test(num_digits(0) == 1)
test(num_digits(-12345) == 5)
test(num_digits(54321) == 5)
test(num_digits(-246) == 3)
'''
'''
def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        lastDigit = n % 10
        if lastDigit == 0 or lastDigit == 5:
            count += 1              #using abreviated assigment / variable updating
        n = n // 10
    return count

test(num_zero_and_five_digits(1055030250) == 7)
'''
'''
def num_even_digits(n):
    count = 0
    if n == 0:
        count = 1
    while n > 0:
        lastDigit = n % 10
        if lastDigit % 2 == 0:
            count += 1              #using abreviated assigment / variable updating
        n = n // 10
    return count

test(num_even_digits(123456) == 3)
test(num_even_digits(2468) == 4)
test(num_even_digits(1357) == 0)
test(num_even_digits(0) == 1)
'''
'''
for x in range(13):   # Generate numbers 0 to 12
    print(x, "\t", 2**x)
'''
'''
def print_multiples(n):
    for i in range(1, 8):
        print(n * i, end="\t")
    print()

def print_mult_table():
    for i in range(1, 8):
        print_multiples(i)

print_mult_table()
'''
'''
def print_multiplication_table(nrc):
    #Create a multiplication table of nrc (integer) rows & colums
    for j in range(1, nrc+1):
        for i in range(1, nrc+1):
           print(j * i, end="\t")
        print()

print_multiplication_table(15)
'''
'''
for j in range(1):
    for i in [12, 16, 17, 24, 29]:
        if i % 2 == 1:  # If the number is odd
            break        #  ... immediately exit the loop
        print(i)

print("done")
'''
'''
total = 0
while 5:
    response = input("Enter the next number. (Leave blank to end)")
    if response == "":
        break
    total += int(response)
print("The total of the numbers you entered is ", total)
'''
'''
import random               
number = random.randint(1,1000)

guesses = 0

guesses = 0
msg = ""

while True:
    guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
    guesses += 1
    if guess > number:
        msg += str(guess) + " is too high.\n"
    elif guess < number:
        msg += str(guess) + " is too low.\n"
    else:
        break
    
input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))
'''
'''
for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 1:      # If the number is odd
       continue         # Don't process it
    print(i)
print("done")
'''
'''
def mult_table_v2(n):
    for j in range(1,n+1):
        for i in range(1,j+1):
            print(j*i, end='\t')
        print()

mult_table_v2(8)
'''
'''
celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937),
                                ("Justin Bieber", 1994)]

for (nm, yr) in celebs:
   if yr < 1980:
        print(nm)
'''
'''
students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
'''
'''
for (nm,cl) in students:
    print(nm, ' takes ', len(cl), ' courses')
'''
'''
studens_CS=0
for (nm,cl) in students:
    for i in cl:
        if i == 'CompSci':
            studens_CS += 1
print('There are', studens_CS, 'students enrolled in \
Computer Science.')
'''
'''
n = float(input('What number you want to calculate its square root?'))
approx = float(input('What is your approximate answer?'))
counter = 0
while True:
    counter +=1
    better = (approx + n/approx)/2              #Newton's square root method/algorithm of approximation
    if abs (better - approx) < 0.0000001:       
        print(better)
        break
    else:
        approx = better
        print(better)
print('\n Number of required iterations:', counter)
input('\n press Enter to exit')
'''