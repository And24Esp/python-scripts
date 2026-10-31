from unit_tester import test

#The 1st step is to load the text from Alice in Wonderland, and
# transform its text into a list of words with all punctuation punctuation
# removed and all in text in lower case. For this, we simply copy from
# Ch14_list_algorithms 3 elements: the url path where the .txt file is, the 
# text_to_words function, and the get_words_from_book function:

folder = "C:\\Users\\ecues\\OneDrive\\Documentos\\03 Academico\\03 Computer \
Science\\Automation\\Python\\TLACSP exercises\\Ch14_test_driven_dev\\"

def text_to_words(the_text):
    """ Return list of words with all punctuation removed, all in lowercase. """
    my_substitutions = 'abc'.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
    
    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

'''
test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
test(text_to_words('"Well, I never!", said Alice.') == 
["well", "i", "never", "said", "alice"])
'''

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)   # calling text_to_words function
    return wds

book_words = get_words_in_book(folder+"alice_in_wonderland.txt")

'''
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))
'''
#The 2nd step is to create an empty dictionary, and use this chapter's
# exercise 1 function (located in Ch20_dictionaries) as a benchmark to
# transit through the all the words in the book and count them inside
# the dictionary we created in the first place. For formatting the result,
# we'll use a little help from the string format method (from Ch8):

words_ocurrence = {}

for word in book_words:
    words_ocurrence[word] = words_ocurrence.get(word,0) + 1

words_ocurrence_list = list(words_ocurrence.items())
words_ocurrence_list.sort()


#Let's print a summary of the fisrt 10 words in the book:
print('Word                Count')
print('=========================')

for (k,v) in words_ocurrence_list[:10]:
    if k == ' ':
        continue
    else:
        print('{0:20}{1}'.format(k,v))


#Let's answer the question about the word's 'alice' occurence in the book:
print('')
print('The word Alice occurs', words_ocurrence['alice'], 'times in the book.')


#Let's answer question/exercise 4:
longest_word = 'accidentally'   #I'll start with the longest word I already know

for word in words_ocurrence:
    if len(word) >= len(longest_word):
        longest_word = word
    else:
        continue

print('The longest word in the book is', longest_word, 'which has \
a total of', len(longest_word), 'letters.')
print('')