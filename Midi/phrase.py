import word

track    = 0
channel  = 9
time     = 4    # In beats

tempo    = 60   # In BPM
volume   = 127  # 0-127, as per the MIDI standard 


Hand_Clap = 39
Side_Stick = 37
Short_Whistle = 71

class Note:
    '''
    A class that encapsulates a note
    '''

    def __init__(self, channel, pitch, duration, volume, annotation=None):
        self.pitch = pitch
        self.duration = duration
        self.volume = volume
        self.channel = channel
        self.annotation = annotation
        

    def __eq__(self, other):
        return (self.pitch == other.pitch and self.channel == other.channel)


    def __str__(self):
        #return '%d channel %d pitch %d duration %d volume %s annotation' % (self, self.channel, self.pitch, self.duration, self.volume, self.annotation)
        return 'channel: {} pitch: {} duration: {} volume: {} annotation: {}'.format(self.channel, self.pitch, self.duration, self.volume, self.annotation)
        


def getPhrase(length):
    phrase = []  # A phrase is a list of words. A word is a list of four syllables
    for i in range(length):
        wordRequested = word.getDupleWord()
        phrase.append(wordRequested)
    return phrase

    
    
# Under construction    
def phraseToNotes(phrase):
    notes = []
    for wordInPrhase in phrase:
        for syllable in wordInPrhase:
            for item in (syllable.getRythm()):
                myNote = Note(channel, Side_Stick, item, volume, '') # The instrument is setted
                notes.append(myNote)
                #print(myNote)
            #print(syllable,)
        #print()
    #print(notes)
    return notes

def printPhrase(phrase):
   notes = []
   for wordInPrhase in phrase:
       print(str(wordInPrhase))


        
#myNote = Note(1,120,1,127,'annotation')
#print(myNote)        
#word.getDupleWord()
#print((Syllable)(getPhrase(4)[2][1]))
#print(phraseToNotes(getPhrase(4)))

printPhrase(getPhrase(4))