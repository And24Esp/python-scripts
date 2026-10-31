#Local and Global Variables with the Same Name

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local' # local assigment has to go first, or doesnt have to be there

eggs = 'global'
spam()
