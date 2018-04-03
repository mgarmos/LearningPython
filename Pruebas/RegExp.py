import re

text = 'From: asdf@por.com msg:this is teh message'

result = re.findall('From',text)
print (result)

result = re.findall('([@]*)',text)
print (result)

result = re.findall('(@.*)',text)
print (result)
