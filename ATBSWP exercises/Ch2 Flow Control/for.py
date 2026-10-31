#exercices in chapter 2, part 1 of the book ABSWP

print('My name is')
for conteo in range(2,5):
    print('Jimmy Five Times (' + str(conteo) + ')')

#same formula but using while
    
print('My name is')
i = 2
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1


#Karl Friedrich Gauss
total = 0
for num in range(101):
    total = total + num
print(total)

#including the thepping argument in range()
print('My name is')
for conteo in range(2,10,2):
    print('Jim goes up (' + str(conteo) + ')')

print('My name is')
for conteo in range(10,-11,-3):
    print('Jim goes down (' + str(conteo) + ')')
