import word
from enum import Enum

volume   = 127  # 0-127, as per the MIDI standard 


Hand_Clap = 39
Side_Stick = 37
Short_Whistle = 71

class Meter(Enum):
    DUPLE = 2
    TRIPLE = 3

class Note:
    '''
    A class that encapsulates a note
    '''

    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration    

    def __eq__(self, other):
        return (self.pitch == other.pitch)

    def __str__(self):
        return 'pitch: {} duration: {} '.format(self.pitch, self.duration)
		
    def getPitch(self):
        return self.pitch
		
    def getDuration(self):
        return self.duration		
        


def getPhrase(length, meter= Meter.DUPLE):
    phrase = []  # A phrase is a list of words. A word is a list of four syllables
    for i in range(length):
        wordRequested = word.getDupleWord() if meter == Meter.DUPLE else word.getTripleWord()		
        phrase.append(wordRequested)
    return phrase

    
      
def phraseToNotes(phrase):
    notes = []
    for wordInPrhase in phrase:
        for syllable in wordInPrhase:
            for item in (syllable.getRythm()):
                myNote = Note(Side_Stick, item) # The instrument is setted
                notes.append(myNote)
    return notes

def printPhrase(myPhrase):
    for myWord in myPhrase:
        for syllable in myWord:
	        print(syllable,end=', ')
        print('')


	   

