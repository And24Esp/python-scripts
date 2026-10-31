#Importing standard library's modules

import random

#for i in range(10000):
#    print(random.randint(0, 100000000000000000000000000000000000000000000000000000000000000000000000000000000))


#for i in range(100):
#    print(random.random())


#Intento fallido de jackpot

number = 1

while number != 7:
    r = print(random.randint(1,10))
    if r == 7:
        break
print('jackpot')
