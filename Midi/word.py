import random
from syllables import A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,B6


# TODO meter to constant

dupleSyllablesChoice = [A1,A2,A3,A4,A5]
tripleSyllablesChoice = [B1,B2,B3,B4,B5,B6]

def getDupleWord():
	__getWord(2)
		
def getTripleWord():
	__getWord(3)
		
def __getWord(meter):
	word = []
	syllablesChoice = dupleSyllablesChoice if meter == 2 else tripleSyllablesChoice
	for i in range(4):
		syllable = random.choice(syllablesChoice)()
		word.append(syllable.name)
	print(word)
	return word

def printWord(word):
	pass
			
	
getDupleWord()
getTripleWord()
	
