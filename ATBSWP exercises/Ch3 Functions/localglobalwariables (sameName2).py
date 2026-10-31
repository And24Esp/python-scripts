#Local and Global Variables with the Same Name

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
