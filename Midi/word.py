import random
import patterns

#patternChoice = [patterns.A1, patterns.A2,  patterns.A3, patterns.A4, patterns.A5]
patternChoice = [patterns.B1, patterns.B2, patterns.B3, patterns.B4, patterns.B5, patterns.B6]

# print(patterns.A3().getNotes())

def getWord(length, patternChoice):
	for j in range(2):
		word = []
		for i in range(length):
			pattern = random.choice(patternChoice)()
			word.append(pattern.name)
		
		print(word)
	

getWord(4,patternChoice)
	
