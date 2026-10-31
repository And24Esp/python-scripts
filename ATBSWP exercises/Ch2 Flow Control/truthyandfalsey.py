#exercices in chapter 2, part 1 of the book ABSWP

name = ''
while not name:
    print('Enter your name:')
    name = input()

print('How many guests will you have?')
numOfGuests = int(input())

if numOfGuests:
    print('Be sure to have enough room for all your guests.')

print('Done')
