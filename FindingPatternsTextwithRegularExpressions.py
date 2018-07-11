# Finding Patterns of Text with Regular Expressions

import re

# Creating Regex Objects
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

miText = 'My number is 415-555-4242. My number is 245-535-4742.'
matchingObject = phoneNumRegex.search(miText)
print(matchingObject.group(0)) # 415-555-4242

# Se definen dos grupos mediante parentesis
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchingObject = phoneNumRegex.search(miText)
print(matchingObject.group(0)) # 415-555-4242
print(matchingObject.group(1))
print(matchingObject.group(2))




# Se definen dos grupos mediante parentesis
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchingObject = phoneNumRegex.findall((miText))
print(matchingObject)

# Se definen dos grupos mediante parentesis
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchingObject = phoneNumRegex.findall((miText))
print(matchingObject)
