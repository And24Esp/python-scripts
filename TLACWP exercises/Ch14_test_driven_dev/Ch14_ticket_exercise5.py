
import random
from unit_tester import test
from copy import deepcopy

def lotto_draw():
    """ Each lotto draw takes six random balls, numbered from 1 to 49"""
    draw = []
    rng = random.Random()
    for i in range(6):
        ball = rng.randint(1,50)
        draw.append(ball)
    return draw


def lotto_match(draw, ticket):
    """compares a single ticket and a draw, and returns the number
     of correct picks on that ticket"""
    matches = 0
    for n in ticket:
        if n in draw:
            matches += 1
    return matches

'''
test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
'''

def lotto_matches(draw, ticket_list):
    """takes a list of tickets and a draw, and returns a list 
     telling how many picks were correct on each ticket"""
    picks = []
    for t in ticket_list:
        matches = lotto_match(draw, t)
        picks.append(matches)
    return picks

my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

'''
test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])
'''

def is_prime(n):
    """Take an integer and return True when is a prime number and 
    False otherwise. Function built on chapter 7 of the book."""
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def primes_in(draw):
    """Take list of integers, and return number of primes in list"""
    count = 0
    for num in draw:
        if is_prime(num) == True:
            count += 1
    return count

'''
test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
'''

def prime_misses(ticket_list):
    prime_nums_upto50 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    missing_primes = []
    consolidated_list = []
    for i in ticket_list:
        consolidated_list.extend(i)
    for j in prime_nums_upto50:
        if j not in consolidated_list:
            missing_primes.append(j)
    return missing_primes

'''
test(prime_misses(my_tickets) == [3, 29, 47])
'''

def compare_draws_tickets(ticket_list, req_picks):
    """repeatedly makes a new draw, and compares the draw to the 
    four choosen lotto tickets"""
    counter_a = 0
    counter_b = 0
    while counter_b < 20:
        counter_a += 1
        draw = lotto_draw()
        matches = lotto_matches(draw,ticket_list)
        if req_picks in matches:
            counter_b += 1
    return counter_a // counter_b

print(compare_draws_tickets(my_tickets,3))
print('Processing...')
print(compare_draws_tickets(my_tickets,4))
print('Processing...')
print(compare_draws_tickets(my_tickets,5))