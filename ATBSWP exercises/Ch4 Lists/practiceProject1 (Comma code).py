#Write a function that takes a list value as an argument and returns
#a string with all the items separated by a comma and a space, with "and"
#inserted before the last item. For example, passing the previous spam list to
#the function would return 'apples, bananas, tofu, and cats'. But your function
#should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = ['abc', 'def', 'ghi', 'jkl', 'mnñ', 'opq', 'rst', 'uvw', 'xyz']

def commasAnd (var):
    for i in range(len(var)):
        print(var[i], end=', ')
        if i == (len(var)-2) :
            break
    print('and ' + var[-1])

commasAnd (spam)
commasAnd (eggs)
