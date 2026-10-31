#V2 is a line by line code review of the vb, in order for me to understand it

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mooses', 'gooses']]

#Line by line output validation on the Shell:

print(tableData[0])
print(len(tableData))
print(range(len(tableData)))

colWidths = [0] * len(tableData)

#Get the longest string on the "x axis"

for y in range(len(tableData)):
    for x in tableData[y]:
        if colWidths[y] < len(x):
            colWidths[y] = len(x)
print(colWidths)
print(colWidths[0])
print(colWidths[1])
print(colWidths[2])

#Print "y axis" lists

for x in range(len(tableData[0])):
    for y in range(len(tableData)):
        print(tableData[y][x].rjust(colWidths[y]), end = ' ')
    print()
    x += 1

#The "x and y coordenates" similie is helpfoul for understanding this exercise 
