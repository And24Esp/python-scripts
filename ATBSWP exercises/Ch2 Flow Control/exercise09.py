#Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
#stored in spam, and prints :( if anything else is stored in spam.

print('Enter number 1 or 2 to say hi')

spam = int(input())

if spam == 1:
    print('Hello')
elif spam == 2 :
    print('Howdy')
else:
    print(':(')
