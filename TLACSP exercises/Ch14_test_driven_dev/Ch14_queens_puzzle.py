
from unit_tester import test
import random
from copy import deepcopy
import time
import Ch17_draw_queens as draw_queens

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

'''
test(not share_diagonal(5,2,2,0))
test(share_diagonal(5,2,3,0))
test(share_diagonal(5,2,4,3))
test(share_diagonal(5,2,4,1))
'''

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

'''
# Solutions cases that should not have any clashes:
test(not col_clashes([6,4,2,0,5], 4))
test(not col_clashes([6,4,2,0,5,7,1,3], 7))
# More test cases that should mostly clash:
test(col_clashes([0,1], 1))
test(col_clashes([5,6], 1))
test(col_clashes([6,5], 1))
test(col_clashes([0,6,4,3], 3))
test(col_clashes([5,0,7], 2))
test(not col_clashes([2,0,1,3], 1))
test(col_clashes([2,0,1,3], 2))
'''

def has_clashes(the_board):       
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

'''
test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two
test(has_clashes([0,1,2,3]))             # Try small 4x4 board
test(not has_clashes([2,0,3,1]))         # Solution to 4x4 case
#My two paper solutions:
test(not has_clashes([1,3,5,7,2,0,6,4]))
test(not has_clashes([1,3,5,7,0,2,6,4])) #This paper solution was wrong
'''

def main(board_size,req_solutions):
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(board_size))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < req_solutions:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1

'''
t0 = time.clock()
#main(4,10)
#main(8,10)
#main(12,10)
#main(15,1)
main(16,1)  #It takes about one minute to find a solution on a 16*16 board
#main(17,1)
t1 = time.clock()
print("That took {0:.4f} seconds.".format(t1-t0))
'''

def mirror_y_axis(board):
    new_board = []
    for i in board:
        new_board += [len(board)-1-i]
    return new_board

'''
test(mirror_y_axis([6,4,2,0,5,7,1,3])==[1,3,5,7,2,0,6,4])
test(mirror_y_axis([1,3,5,7,2,0,6,4])==[6,4,2,0,5,7,1,3])
'''

def mirror_x_axis(board):
    new_board = []
    for i in range(-1,-len(board)-1,-1):
        new_board += [board[i]]
    return new_board

'''
test(mirror_x_axis([6,4,2,0,5,7,1,3])==[3,1,7,5,0,2,4,6])
test(mirror_x_axis([1,3,5,7,2,0,6,4])==[4,6,0,2,7,5,3,1])
'''

def rotate_anti_clockwise(board):
    new_board = []
    for i in range(len(board)):
        new_board += [len(board)-1-board.index(i)]
    return new_board


test(rotate_anti_clockwise([6,4,2,0,5,7,1,3])==[4,1,5,0,6,3,7,2])
test(rotate_anti_clockwise([0,4,7,5,2,6,1,3])==[7,1,3,0,6,4,2,5])


def family_symmetries(board):
    family = []
    family.append(board)
    family.append(rotate_anti_clockwise(board))
    family.append(rotate_anti_clockwise
        (rotate_anti_clockwise(board)))
    family.append(rotate_anti_clockwise
        (rotate_anti_clockwise(rotate_anti_clockwise(board))))
    family.append(mirror_x_axis(board))
    family.append(mirror_x_axis(rotate_anti_clockwise
        (rotate_anti_clockwise(rotate_anti_clockwise(board)))))
    family.append(mirror_x_axis(rotate_anti_clockwise
        (rotate_anti_clockwise(board))))
    family.append(mirror_x_axis(rotate_anti_clockwise(board)))
    return family

'''
test(family_symmetries([0,4,7,5,2,6,1,3])==
[[0,4,7,5,2,6,1,3],[7,1,3,0,6,4,2,5],
 [4,6,1,5,2,0,3,7],[2,5,3,1,7,4,6,0],
 [3,1,6,2,5,7,4,0],[0,6,4,7,1,3,5,2],
 [7,3,0,2,5,1,6,4],[5,2,4,6,0,3,1,7]])
'''

def main2(board_size,req_solutions):
    import random
    rng = random.Random()   # Instantiate a generator
    repository = []
    bd = list(range(board_size))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < req_solutions:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           if bd in repository:
               continue
           else:
               repository += deepcopy((family_symmetries(bd))) 
               #In prior line, += could be replaced with the extend method
               print("Found unique solution {0} in {1} tries.".format(bd, tries))
               draw_queens.draw_board(bd)
               tries = 0
               num_found += 1
    return repository

main2(8,12)
#WARNING: If the required solutions parameter is higher than the available 
# fundamental solutions, the main function enters on an infinite loop.
# Fundamental solutions: https://en.wikipedia.org/wiki/Eight_queens_puzzle