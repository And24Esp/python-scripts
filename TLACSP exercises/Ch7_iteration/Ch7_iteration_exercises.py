import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

'''
edades = [65,45,38,45,4,84,46,3,14,87,4]
posneg = [4,-65,45,38,-45,84,46,-3,14,-87,4]
sinpares = [-65,45,-45,-3,87]
palabras = ['Hola','como','estas','el','dia','de','hoy','amigo','Pedro']
Samsara = ['She','is','Sam','from','Brazil']
Laura = ['She','is','Laura','from','Brazil']
SamLaura = ['Sam','and','Laura','are','from','BR']
'''
'''
#Write a function to count how many odd numbers are in a list

def count_odd_numbers(numberList):
    odd_count = 0
    for i in numberList:
        if i % 2 == 1:
            odd_count += 1
    return odd_count

print(count_odd_numbers(edades))
'''
'''
# Sum up all the even numbers in a list.

def sumup_even_numbers(numberList):
    even_sumup = 0
    for i in numberList:
        if i % 2 == 0:
            even_sumup += i
    return even_sumup

print(sumup_even_numbers(edades))
'''
'''
# Sum up all the negative numbers in a list.

def sumup_negative_numbers(numberList):
    negative_sumup = 0
    for i in numberList:
        if i < 0:
            negative_sumup += i
    return negative_sumup

print(sumup_negative_numbers(posneg))
'''
'''
# Count how many words in a list have length 5.

def count_words_lenght5(wordList):
    length5_count = 0
    for i in wordList:
        if len(i) == 5:
            length5_count += 1
    return length5_count

print(count_words_lenght5(palabras))
'''
'''
# Sum all the elements in a list up to but not including the first even number. 
# Write your unit tests. What if there is no even number?

def sumup_allBut1stEven(numberList):
    sumup = 0
    for i in numberList:
        sumup += i
    for i in numberList:
        if i % 2 == 0:
            sumup -= i
            return sumup
    return sumup

def test_sumup_allBut1stEven():
    test(sumup_allBut1stEven(edades) == (65+45+38+45+4+84+46+3+14+87+4-38))
    test(sumup_allBut1stEven(posneg) == (4-65+45+38-45+84+46-3+14-87+4-4))
    test(sumup_allBut1stEven(sinpares) == (-65+45-45-3+87))

test_sumup_allBut1stEven()
'''
'''
# Count how many words occur in a list up to and including the 
#   first occurrence of the word “sam”. Write your unit tests.

def count_words_upTo_Sam(wordList):
    count = 0
    for i in wordList:
        count += 1
        if i == 'Sam':
            return count
    return count

def test_count_words_upTo_Sam():
    test(count_words_upTo_Sam(Samsara) == 3)
    test(count_words_upTo_Sam(Laura) == 5)
    test(count_words_upTo_Sam(SamLaura) == 1)

test_count_words_upTo_Sam()
'''
'''
def print_triangular_numbers(n):
    tn=0
    for i in range(1,n+1):
        tn += i
        print(i,'\t',tn)
    
print_triangular_numbers(1000)
'''
'''
#Take an integer and return True when is a prime number and False otherwise.
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(not is_prime(19861224))

test_is_prime()
'''
'''
import turtle

def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

w = make_window("black", "Eulerian Graphics")

def make_turtle(name, colr, sz):
    name = turtle.Turtle()
    name.color(colr,'red')
    name.pensize(sz)
    return name

donatello = make_turtle('donatello','white', 2)

drunkRoute = [(160,20),(-43,10),(270,8),(-43,12)]
eulerianPath1= [(0,141.4),(135,100),(0,100),(135,141.4),(135,100),(0,100),
                (135,141.4),(-135,100),(-90,100),(-45,141.4)]

def donnie_path(path):
    for a, d in path:
        donatello.left(a)
        donatello.forward(d)

donnie_path(eulerianPath1)

w.mainloop()
'''
'''
# Computes the sum of the squares of the numbers in the list xs 

def sum_of_squares(numberList):
    sumup = 0
    for i in numberList:
        sumup += i**2
    return sumup

def test_sum_of_squares():
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)

test_sum_of_squares()
'''

# Last exercise in chapter
# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first = {0},  winner = {1} ".format(human_plays_first, result))
    return result

gameCounter = 0
scoreHuman = 0
scoreCPU = 0
scoreDraw =0

while True:
    
    gameCounter += 1
    
    if gameCounter % 2 == 1:
        gameResult = play_once(True)
    elif gameCounter % 2 == 0:
        gameResult = play_once(False)
    
    if gameResult == -1:
        scoreHuman += 1
        PWH = '(' + str(int(scoreHuman / (scoreHuman + scoreCPU + scoreDraw) * 100)) + '%)'
        print(' You win!\n Current score ->    Human:', scoreHuman, PWH, '    CPU:', 
            scoreCPU, '    Draws:', scoreDraw)     
    elif gameResult == 0:
        scoreDraw += 1
        PWH = '(' + str(int(scoreHuman / (scoreHuman + scoreCPU + scoreDraw) * 100)) + '%)'
        print(' Game drawn!\n Current score ->    Human:', scoreHuman, PWH,'    CPU:', 
            scoreCPU, '    Draws:', scoreDraw)
    elif gameResult == 1:
        scoreCPU += 1
        PWH = '(' + str(int(scoreHuman / (scoreHuman + scoreCPU + scoreDraw) * 100)) + '%)'
        print(' I win!\n Current score -> Human:',scoreHuman, PWH,'    CPU:', 
            scoreCPU,'    Draws:',scoreDraw)
    playAgain = input('Do you want to play again? (Type YES or NO and then Enter)')
    if playAgain == 'YES':
        print('')
        continue
    elif playAgain == 'NO':
        print('Ok. Goodbye. \n')
        break
    else:
        print('I assume that\'s a YES!!! \n')
        continue

