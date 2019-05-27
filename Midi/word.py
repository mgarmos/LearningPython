import random
import patterns

patternChoice = [patterns.A1, patterns.A2,  patterns.A3, patterns.A4, patterns.A5]

# print(patterns.A3().getNotes())

def getWord(length, patternChoice):
	
	word = []
	for i in range(length):
		pattern = random.choice(patternChoice)()
		word.append(pattern.name)
	
	print(word)
	

getWord(4,patternChoice)
	