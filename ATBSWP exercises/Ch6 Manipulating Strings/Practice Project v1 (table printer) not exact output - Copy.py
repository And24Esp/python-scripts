tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mooses', 'gooses']]

def printTable(table):
    columnLength = [0] * len(table)
    for i in range(len(table)):
        columnLength[i] = len(' '.join(table[i]))
    for i in range(len(table)):
        print(' '.join(table[i]).rjust(max(columnLength)))

printTable(tableData)

'''After finishing the exercise, I realized the order of the elements on
my output is different from the one showed on the book (pg 143). The vb
version (benchmark) of the exercise has the correct/exact output'''
