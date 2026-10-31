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

print('\n'.join(map(''.join, zip(*grid))))

# done by Stephan Pochman on Stackoverflow

#"The zip(*grid) effectively transposes the matrix (flip it on the main
#diagonal), then each row is joined into one string, then the rows are 
#joined with newlines so the whole thing can be printed at once".

#https://stackoverflow.com/questions/30424355/automate-the-boring-stuff-with-python-chapter-4-exercise

#THIS CODE IS TO ADVANCED FOR ME AT THE MOMENT.
