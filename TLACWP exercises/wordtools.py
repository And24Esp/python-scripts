"""
Exercise 8, chapter 12. 
Instructions: Save this module so you can use the tools it contains in future programs.
"""

from unit_tester import test
from string import punctuation


def cleanword(word):
    """ Returns a word without punctuation marks""" 
    new_word = ''
    for i in word:
        if i not in punctuation:
            new_word += i
    return new_word

'''
test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")
'''

def has_dashdash(word):
    """ Returns a word without dashdash marks"""
    if '--' in word:
        return True
    else:
        return False

'''
test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))
'''

def extract_words(phrase):
    """ Returns a list from a phrase with no dashdash elements. All returned items are lowercased."""
    no_dashdash_phrase = ' '.join(phrase.split('--'))   #statement that removes dashdash elements
    splitted_phrase = no_dashdash_phrase.lower().split()
    cleaned_list = []
    for i in splitted_phrase:
        cleaned_word = cleanword(i)
        cleaned_list.append(cleaned_word)
    return cleaned_list

'''
test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])
'''

def wordcount(word,list):
    """ Returns how many ocurrences of a word is within a list"""
    counter = 0
    for wd in list:
        if wd == word:
            counter += 1
    return counter
'''
test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)
'''

def wordset(list):
    """ Returns a set of the words contained in a list"""
    new_list = []
    for wd in list:
        if wd not in new_list:
            new_list.append(wd)
    new_list.sort()             # .sort() is a modifier, thats why no variable assigment is needed
    return new_list

'''
test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])
'''

def longestword(list):
    """ Returns the length of the longest word within a list"""
    lw_lenght = 0
    for wd in list:
        if len(wd) > lw_lenght:
            lw_lenght = len(wd)
    return lw_lenght


test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
