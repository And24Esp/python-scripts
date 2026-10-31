   1 import sys
   2 
   3 def test(did_pass):
   4     """  Print the result of a test.  """
   5     linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
   6     if did_pass:
   7         msg = "Test at line {0} ok.".format(linenum)
   8     else:
   9         msg = ("Test at line {0} FAILED.".format(linenum))
  10     print(msg)
  11 '''
  12 def find(strng, ch):
  13     """
  14       Find and return the index of ch in strng.
  15       Return -1 if ch does not occur in strng.
  16     """
  17     ix = 0
  18     while ix < len(strng):
  19         if strng[ix] == ch:
  20             return ix
  21         ix += 1
  22     return -1
  23 
  24 test(find("Compsci", "p") == 3)
  25 test(find("Compsci", "C") == 0)
  26 test(find("Compsci", "i") == 6)
  27 test(find("Compsci", "x") == -1)
  28 '''
  29 '''
  30 def find2(strng, ch, start=0):
  31     ix = start
  32     while ix < len(strng):
  33         if strng[ix] == ch:
  34             return ix
  35         ix += 1
  36     return -1
  37 
  38 test(find2("banana", "a", 2) == 3)
  39 test(find2("banana", "n", 3) == 4)
  40 test(find2("banana", "n") == 2)
  41 test(find2("banana", "a") == 1)
  42 '''
  43 '''
  44 #Adding another optional parameter to find makes it search from a starting position,
  45 # up to but not including the end position:
  46 def find(strng, ch, start=0, end=None):
  47     ix = start
  48     if end is None:
  49        end = len(strng)
  50     while ix < end:
  51         if strng[ix] == ch:
  52             return ix
  53         ix += 1
  54     return -1
  55 
  56 ss = "Python strings have some interesting methods."
  57 test(find(ss, "s") == 7)
  58 test(find(ss, "s", 7) == 7)
  59 test(find(ss, "s", 8) == 13)
  60 test(find(ss, "s", 8, 13) == -1)
  61 test(find(ss, "s", 8, 14) == 13)
  62 test(find(ss, ".") == len(ss)-1)
  63 test(find(ss, "d") == 42)
  64 '''
  65 '''
  66 n1 = 4
  67 n2 = 5
  68 s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
  69 print(s3)
  70 '''
  71 '''
  72 n1 = "Paris"
  73 n2 = "Whitney"
  74 n3 = "Hilton"
  75 
  76 print("Pi to three decimal places is {0:.3f}".format(3.1415926))
  77 print("123456789 123456789 123456789 123456789 123456789 123456789")
  78 print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||"
  79         .format(n1,n2,n3,1981))
  80 print("The decimal value {0} converts to hex value {0:x}"
  81         .format(123456))
  82 '''
  83 '''
  84 letter = """
  85 Dear {0} {2}.
  86  {0}, I have an interesting money-making proposition for you!
  87  If you deposit $10 million into my bank account, I can
  88  double your money ...
  89 """
  90 
  91 print(letter.format("Paris", "Whitney", "Hilton"))
  92 print(letter.format("Bill", "Henry", "Gates"))
  93 '''
  94 '''
  95 layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
  96 
  97 print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
  98 for i in range(1, 11):
  99     print(layout.format(i, i**2, i**3, i**5, i**10, i**20))
 100 '''
 101 # Exercises chapter 8
 102 '''
 103 prefixes = "JKLMNOPQ"
 104 suffix1 = "uack"
 105 suffix2 = "ack"
 106 
 107 for letter in prefixes:
 108     if letter == 'O' or letter == 'Q':
 109         print(letter + suffix1)
 110     else:
 111         print(letter + suffix2)
 112 '''
 113 '''
 114 b = 'bananass'
 115 
 116 def count_letters(string, letter):
 117     count = 0
 118     for char in string:
 119         if char == letter:
 120             count += 1
 121     return count
 122     
 123 print(count_letters(b,'s'))
 124 print(count_letters(b,'a'))
 125 '''
 126 '''
 127 fruit = 'bananasss'
 128 
 129 def count_letters2(string, letter, ocurrence=0):
 130     count = 0
 131     while ocurrence < len(string):
 132         index = string.find(letter,ocurrence)
 133         if index == -1:
 134             break
 135         ocurrence = index + 1
 136         count += 1
 137     return count
 138 
 139 def test_count_letters2():
 140     test(count_letters2(fruit,'s',7)==2)
 141     test(count_letters2(fruit,'a',3)==2)
 142     test(count_letters2(fruit,'nan',2)==1)
 143     test(count_letters2(fruit,'nan',3)==0)
 144     test(count_letters2(fruit,'bananasss')==1)
 145 
 146 test_count_letters2()
 147 '''
 148 '''
 149 poema = """Ahora me dejen tranquilo.
 150 Ahora se acostumbren sin mí.
 151 
 152 Yo voy a cerrar los ojos
 153 
 154 Y sólo quiero cinco cosas,
 155 cinco raices preferidas.
 156 
 157 Una es el amor sin fin.
 158 
 159 Lo segundo es ver el otoño.
 160 No puedo ser sin que las hojas
 161 vuelen y vuelvan a la tierra.
 162 
 163 Lo tercero es el grave invierno,
 164 la lluvia que amé, la caricia
 165 del fuego en el frío silvestre.
 166 
 167 En cuarto lugar el verano
 168 redondo como una sandía.
 169 
 170 La quinta cosa son tus ojos,
 171 Matilde mía, bienamada,
 172 no quiero dormir sin tus ojos,
 173 no quiero ser sin que me mires:
 174 yo cambio la primavera
 175 por que tú me sigas mirando.
 176 
 177 Amigos, eso es cuanto quiero.
 178 Es casi nada y casi todo.
 179 
 180 Ahora si quieren se vayan.
 181 
 182 He vivido tanto que un día
 183 tendrán que olvidarme por fuerza,
 184 borrándome de la pizarra:
 185 mi corazón fue interminable.
 186 
 187 Pero porque pido silencio
 188 no crean que voy a morirme:
 189 me pasa todo lo contrario:
 190 sucede que voy a vivirme.
 191 
 192 Sucede que soy y que sigo.
 193 
 194 No será, pues, sino que adentro
 195 de mí crecerán cereales,
 196 primero los granos que rompen
 197 la tierra para ver la luz,
 198 pero la madre tierra es oscura:
 199 y dentro de mí soy oscuro:
 200 soy como un pozo en cuyas aguas
 201 la noche deja sus estrellas
 202 y sigue sola por el campo.
 203 
 204 Se trata de que tanto he vivido
 205 que quiero vivir otro tanto.
 206 
 207 Nunca me sentí tan sonoro,
 208 nunca he tenido tantos besos.
 209 
 210 Ahora, como siempre, es temprano.
 211 Vuela la luz con sus abejas.
 212 
 213 Déjenme solo con el día.
 214 Pido permiso para nacer."""
 215 
 216 import string
 217 
 218 def remove_split_count(paragraph,letter):
 219     """Function which removes all punctuation from the string, breaks the string into a list of words,
 220     and returs the number of words in your text that contain any character or word placed as a parameter,
 221     the total number of words in the paragraph, and the percentage between the two."""
 222     new_paragraph = ''
 223     for ch in paragraph:
 224         if ch not in string.punctuation:
 225             new_paragraph += ch
 226     word_count = 0
 227     list_paragraph = new_paragraph.lower().split()
 228     for wd in list_paragraph:
 229         if letter in wd:
 230             word_count +=1
 231     total_words = len(list_paragraph)
 232     percentage = round( word_count / total_words * 100 , 1)
 233     return letter, word_count, total_words, percentage
 234 
 235 letter, word_count, total_words, percentage = remove_split_count(poema,'a')
 236 
 237 message = 'Your text contains {0} words, of which {1} ({2}%) contains \
 238 the letter/word "{3}".'.format(total_words, word_count, percentage, letter)
 239 
 240 print(message)
 241 '''
 242 '''
 243 def neat_multiplication_table(nrc):
 244     #Create a "neat" format version of a multiplication table of nrc rows & colums
 245     print('     ',end='')
 246     for c in range(1, nrc+1):
 247         print('{0:>4}'.format(c), end='')
 248     print()
 249     print('  :--',end='')
 250     for c in range(1, nrc+1):
 251         print('----', end='')
 252     print()
 253     for r in range(1, nrc+1):
 254         print('{0:>2}:  '.format(r),end='')
 255         for c in range(1, nrc+1):
 256            print('{0:>4}'.format(r*c), end='')
 257         print()
 258 
 259 neat_multiplication_table(12)
 260 '''
 261 '''
 262 def reverse(word):
 263     """ reverses its string argument"""
 264     reversed_word = ''
 265     for i in range(-1,-len(word)-1,-1):
 266 	    reversed_word += word[i]
 267     return reversed_word
 268 
 269 def test_reverse():
 270     test(reverse("happy") == "yppah")
 271     test(reverse("Python") == "nohtyP")
 272     test(reverse("") == "")
 273     test(reverse("a") == "a")
 274     test(reverse("cake") == "ekac")
 275 
 276 test_reverse()
 277 '''
 278 '''
 279 def mirror(word):
 280     """ mirrors its string argument"""
 281     reversed_word = ''
 282     for i in range(-1,-len(word)-1,-1):
 283 	    reversed_word += word[i]
 284     mirrored_word = word + reversed_word 
 285     return mirrored_word
 286 
 287 def test_mirror():
 288     test(mirror("good") == "gooddoog")
 289     test(mirror("Python") == "PythonnohtyP")
 290     test(mirror("") == "")
 291     test(mirror("a") == "aa")
 292 
 293 test_mirror()
 294 '''
 295 '''
 296 def remove_letter(letter, word):
 297     newWord = ''
 298     for i in word:
 299         if i != letter:
 300             newWord += i
 301     return newWord
 302 
 303 def test_remove_letter():
 304     test(remove_letter("a", "apple") == "pple")
 305     test(remove_letter("a", "banana") == "bnn")
 306     test(remove_letter("z", "banana") == "banana")
 307     test(remove_letter("i", "Mississippi") == "Msssspp")
 308     test(remove_letter("b", "") == "")
 309     test(remove_letter("b", "c") == "c")
 310 
 311 test_remove_letter()
 312 '''
 313 '''
 314 def is_palindrome(word):
 315     if reverse(word) == word:
 316         return True
 317     else:
 318         return False
 319 
 320 test(is_palindrome("abba"))
 321 test(not is_palindrome("abab"))
 322 test(is_palindrome("tenet"))
 323 test(not is_palindrome("banana"))
 324 test(is_palindrome("straw warts"))
 325 test(is_palindrome("a"))
 326 test(is_palindrome(""))    # Is an empty string a palindrome?
 327 '''
 328 '''
 329 def count(letters, string, startingIndex=0):
 330     count = 0
 331     while startingIndex < len(string):
 332         index = string.find(letters,startingIndex)
 333         if index == -1:
 334             break
 335         startingIndex = index + 1
 336         count += 1
 337     return count
 338 
 339 test(count("is", "Mississippi") == 2)
 340 test(count("an", "banana") == 2)
 341 test(count("ana", "banana") == 2)
 342 test(count("nana", "banana") == 1)
 343 test(count("nanan", "banana") == 0)
 344 test(count("aaa", "aaaaaa") == 4)
 345 '''
 346 '''
 347 def remove(letters, string):
 348     """ removes the 1st ocurrence of a substring from a string,
 349     startingIndex in this function is irrelevant, its just a "scaffold" for next exercice"""
 350     new_word = ''
 351     startingIndex= 0
 352     while startingIndex < len(string):
 353         index = string.find(letters,startingIndex)
 354         if index == -1:
 355             return string
 356         for i in range(len(string)):
 357             if i < index or i >= (index + len(letters)):
 358                 new_word += string[i]
 359         startingIndex = len(string)
 360     return new_word
 361 
 362 test(remove("an", "banana") == "bana")
 363 test(remove("cyc", "bicycle") == "bile")
 364 test(remove("iss", "Mississippi") == "Missippi")
 365 test(remove("eggs", "bicycle") == "bicycle")
 366 '''
 367 
 368 def remove_all(letters, string):
 369     """ Removes all substring ocurrences from a string"""
 370     new_word = ''
 371     startingIndex = 0
 372     lenght_string = len(string)
 373     while startingIndex < lenght_string:
 374         index = string.find(letters,startingIndex)
 375         if index == -1:
 376             for i in range(startingIndex,lenght_string):
 377                 new_word += string[i]
 378             return new_word
 379         for i in range(startingIndex, lenght_string):
 380             if i < index:
 381                 new_word += string[i]
 382             elif i < (index + len(letters)):
 383                 continue
 384             elif i >= (index + len(letters)):
 385                 startingIndex = i
 386                 break
 387     return new_word
 388 
 389 test(remove_all("an", "banana") == "ba")
 390 test(remove_all("cyc", "bicycle") == "bile")
 391 test(remove_all("iss", "Mississippi") == "Mippi")
 392 test(remove_all("eggs", "bicycle") == "bicycle")
