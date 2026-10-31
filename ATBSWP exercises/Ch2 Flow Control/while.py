#exercices in chapter 2, part 1 of the book ABSWP
#infinite loop

while True:
    print('Who are you?')
    name = input()
    if name != 'Andres':
        print('Invalid name.')
        continue
    print('Hello, Andres. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    else:
        print('Invalid password.')
print('Access granted.')
