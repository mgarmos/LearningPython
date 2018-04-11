# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:', line): #equivalent line.find()
		print(line)
hand.close()
		
print('----------')	
		
# Search for lines that start with 'From'
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip() #equivalent line.startswith()
    if re.search('^From:', line):
        print(line)
hand.close()
print('----------')	
		
""" 
. Character matching in regular expressions
^ Start of line
"""		
#The most commonly used special character is the period or full stop, which matches any character
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip() #equivalent line.startswith()
    if re.search('F..m', line):
        print(line)
hand.close()
print('----------')

""" 
EXTRACTING DATA USING REGULAR EXPRESSIONS
* zero-or-more characters
+ one-or-more of the characters
"""		

# Search for lines that start with From and have an at sign
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:.+@', line):
		print(line)
hand.close()
print('----------')

# Search for lines that start with From and have an at sign
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('\S+@.*\.org', line):
		print(line)
hand.close()
print('----------')

#If we want to extract data from a string in Python we can use the findall()
#method to extract all of the substrings which match a regular expression
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

