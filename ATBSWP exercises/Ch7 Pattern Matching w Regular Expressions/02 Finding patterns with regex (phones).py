# 2nd exercise of chapter 7. Finding/validating a telephone number
# Patern matching using regular expressions

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#Example 1:
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

#Example 2:
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
mo2 = phoneNumRegex.search(message) #search() returns only the 1st match
print('Phone number found: ' + mo2.group()) 
