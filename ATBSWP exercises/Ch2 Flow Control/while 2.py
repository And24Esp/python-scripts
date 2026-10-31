#exercices in chapter 2, part 1 of the book ABSWP

name = ''

while name != 'your name1':
    print('Please type your name')
    name = input() 
print('End of 1st block')

print()

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name2':
        break
print('End of 2nd block')
