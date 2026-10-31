grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#With the previous grid value, write code that uses it to print the image:

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

for i in range(len(grid)):
    print(grid[i][0], end='')
    if i == (len(grid)-1):
       print()

for i in range(len(grid)):
    print(grid[i][1], end='')
    if i == (len(grid)-1):
       print()

for i in range(len(grid)):
    print(grid[i][2], end='')
    if i == (len(grid)-1):
       print()

for i in range(len(grid)):
    print(grid[i][3], end='')
    if i == (len(grid)-1):
       print()

for i in range(len(grid)):
    print(grid[i][4], end='')
    if i == (len(grid)-1):
       print()

for i in range(len(grid)):
    print(grid[i][5], end='')
    if i == (len(grid)-1):
       print()
