from unit_tester import test

'''
eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

for k in eng2sp.keys():   # The order of the k's is not defined
    #.keys inncesesara, iterating over a dictionary implicitly iterates over its keys
    print("Got key", k, "which maps to value", eng2sp[k])

print(list(eng2sp.keys()))

print(list(eng2sp.values()))

print(list(eng2sp.items()))

for (k,v) in eng2sp.items():
    print("Got key",k,"that maps to value",v)
'''
'''
#Memoization optimization technique we can use thanks to dictionaries:
alreadyknown = {0: 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

print(fib(50))
print(alreadyknown)
'''

#Exercise 1:
example = 'ThiS is String with Upper and lower case Letters'
example_low = example.lower()

letters_ocurrence = {}

for l in example_low:
    letters_ocurrence[l] = letters_ocurrence.get(l,0) + 1

letters_ocurrence_list = list(letters_ocurrence.items())
letters_ocurrence_list.sort()

for (k,v) in letters_ocurrence_list:
    if k == ' ':
        continue
    else:
        print(k,'  ',v)

'''
#Exercise 2:
def add_fruit(inventory, fruit, quantity=0):
     inventory[fruit] = inventory.get(fruit, 0) + quantity
     return inventory

new_inventory = {}

# Make these tests work...
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)
'''