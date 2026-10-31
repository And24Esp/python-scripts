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
def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

test(find("Compsci", "p") == 3)
test(find("Compsci", "C") == 0)
test(find("Compsci", "i") == 6)
test(find("Compsci", "x") == -1)
'''
'''
def find2(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

test(find2("banana", "a", 2) == 3)
test(find2("banana", "n", 3) == 4)
test(find2("banana", "n") == 2)
test(find2("banana", "a") == 1)
'''
'''
#Adding another optional parameter to find makes it search from a starting position,
# up to but not including the end position:
def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
       end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

ss = "Python strings have some interesting methods."
test(find(ss, "s") == 7)
test(find(ss, "s", 7) == 7)
test(find(ss, "s", 8) == 13)
test(find(ss, "s", 8, 13) == -1)
test(find(ss, "s", 8, 14) == 13)
test(find(ss, ".") == len(ss)-1)
test(find(ss, "d") == 42)
'''
'''
n1 = 4
n2 = 5
s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
print(s3)
'''
'''
n1 = "Paris"
n2 = "Whitney"
n3 = "Hilton"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||"
        .format(n1,n2,n3,1981))
print("The decimal value {0} converts to hex value {0:x}"
        .format(123456))
'''
'''
letter = """
Dear {0} {2}.
 {0}, I have an interesting money-making proposition for you!
 If you deposit $10 million into my bank account, I can
 double your money ...
"""

print(letter.format("Paris", "Whitney", "Hilton"))
print(letter.format("Bill", "Henry", "Gates"))
'''
'''
layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))
'''
# Exercises chapter 8
'''
prefixes = "JKLMNOPQ"
suffix1 = "uack"
suffix2 = "ack"

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + suffix1)
    else:
        print(letter + suffix2)
'''
'''
b = 'bananass'

def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count
    
print(count_letters(b,'s'))
print(count_letters(b,'a'))
'''
'''
fruit = 'bananasss'

def count_letters2(string, letter, ocurrence=0):
    count = 0
    while ocurrence < len(string):
        index = string.find(letter,ocurrence)
        if index == -1:
            break
        ocurrence = index + 1
        count += 1
    return count

def test_count_letters2():
    test(count_letters2(fruit,'s',7)==2)
    test(count_letters2(fruit,'a',3)==2)
    test(count_letters2(fruit,'nan',2)==1)
    test(count_letters2(fruit,'nan',3)==0)
    test(count_letters2(fruit,'bananasss')==1)

test_count_letters2()
'''
'''
poema = """Ahora me dejen tranquilo.
Ahora se acostumbren sin mí.

Yo voy a cerrar los ojos

Y sólo quiero cinco cosas,
cinco raices preferidas.

Una es el amor sin fin.

Lo segundo es ver el otoño.
No puedo ser sin que las hojas
vuelen y vuelvan a la tierra.

Lo tercero es el grave invierno,
la lluvia que amé, la caricia
del fuego en el frío silvestre.

En cuarto lugar el verano
redondo como una sandía.

La quinta cosa son tus ojos,
Matilde mía, bienamada,
no quiero dormir sin tus ojos,
no quiero ser sin que me mires:
yo cambio la primavera
por que tú me sigas mirando.

Amigos, eso es cuanto quiero.
Es casi nada y casi todo.

Ahora si quieren se vayan.

He vivido tanto que un día
tendrán que olvidarme por fuerza,
borrándome de la pizarra:
mi corazón fue interminable.

Pero porque pido silencio
no crean que voy a morirme:
me pasa todo lo contrario:
sucede que voy a vivirme.

Sucede que soy y que sigo.

No será, pues, sino que adentro
de mí crecerán cereales,
primero los granos que rompen
la tierra para ver la luz,
pero la madre tierra es oscura:
y dentro de mí soy oscuro:
soy como un pozo en cuyas aguas
la noche deja sus estrellas
y sigue sola por el campo.

Se trata de que tanto he vivido
que quiero vivir otro tanto.

Nunca me sentí tan sonoro,
nunca he tenido tantos besos.

Ahora, como siempre, es temprano.
Vuela la luz con sus abejas.

Déjenme solo con el día.
Pido permiso para nacer."""

import string

def remove_split_count(paragraph,letter):
    """Function which removes all punctuation from the string, breaks the string into a list of words,
    and returs the number of words in your text that contain any character or word placed as a parameter,
    the total number of words in the paragraph, and the percentage between the two."""
    new_paragraph = ''
    for ch in paragraph:
        if ch not in string.punctuation:
            new_paragraph += ch
    word_count = 0
    list_paragraph = new_paragraph.lower().split()
    for wd in list_paragraph:
        if letter in wd:
            word_count +=1
    total_words = len(list_paragraph)
    percentage = round( word_count / total_words * 100 , 1)
    return letter, word_count, total_words, percentage

letter, word_count, total_words, percentage = remove_split_count(poema,'a')

message = 'Your text contains {0} words, of which {1} ({2}%) contains \
the letter/word "{3}".'.format(total_words, word_count, percentage, letter)

print(message)
'''
'''
def neat_multiplication_table(nrc):
    #Create a "neat" format version of a multiplication table of nrc rows & colums
    print('     ',end='')
    for c in range(1, nrc+1):
        print('{0:>4}'.format(c), end='')
    print()
    print('  :--',end='')
    for c in range(1, nrc+1):
        print('----', end='')
    print()
    for r in range(1, nrc+1):
        print('{0:>2}:  '.format(r),end='')
        for c in range(1, nrc+1):
           print('{0:>4}'.format(r*c), end='')
        print()

neat_multiplication_table(12)
'''
'''
def reverse(word):
    """ reverses its string argument"""
    reversed_word = ''
    for i in range(-1,-len(word)-1,-1):
	    reversed_word += word[i]
    return reversed_word

def test_reverse():
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    test(reverse("cake") == "ekac")

test_reverse()
'''
'''
def mirror(word):
    """ mirrors its string argument"""
    reversed_word = ''
    for i in range(-1,-len(word)-1,-1):
	    reversed_word += word[i]
    mirrored_word = word + reversed_word 
    return mirrored_word

def test_mirror():
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")

test_mirror()
'''
'''
def remove_letter(letter, word):
    newWord = ''
    for i in word:
        if i != letter:
            newWord += i
    return newWord

def test_remove_letter():
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")

test_remove_letter()
'''
'''
def is_palindrome(word):
    if reverse(word) == word:
        return True
    else:
        return False

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))    # Is an empty string a palindrome?
'''
'''
def count(letters, string, startingIndex=0):
    count = 0
    while startingIndex < len(string):
        index = string.find(letters,startingIndex)
        if index == -1:
            break
        startingIndex = index + 1
        count += 1
    return count

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)
'''
'''
def remove(letters, string):
    """ removes the 1st ocurrence of a substring from a string,
    startingIndex in this function is irrelevant, its just a "scaffold" for next exercice"""
    new_word = ''
    startingIndex= 0
    while startingIndex < len(string):
        index = string.find(letters,startingIndex)
        if index == -1:
            return string
        for i in range(len(string)):
            if i < index or i >= (index + len(letters)):
                new_word += string[i]
        startingIndex = len(string)
    return new_word

test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")
'''

def remove_all(letters, string):
    """ Removes all substring ocurrences from a string"""
    new_word = ''
    startingIndex = 0
    lenght_string = len(string)
    while startingIndex < lenght_string:
        index = string.find(letters,startingIndex)
        if index == -1:
            for i in range(startingIndex,lenght_string):
                new_word += string[i]
            return new_word
        for i in range(startingIndex, lenght_string):
            if i < index:
                new_word += string[i]
            elif i < (index + len(letters)):
                continue
            elif i >= (index + len(letters)):
                startingIndex = i
                break
    return new_word

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
