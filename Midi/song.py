import phrase
import time as timeUtil
from MIDIUtil import MIDIFile

soundCode = 35
bitCode = 34

track    = 0
tempo    = 60   # In BPM
channel  = 9
volume = 127




# Create a midi file from a phrase
def toFile(fileName, myPhrase, metronome = True):
    time = 0
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, 0, tempo)


    # Ticks in first measure
    if metronome == True:
        if myPhrase.meter == phrase.Meter.TRIPLE:
            for i in range(3):
                MyMIDI.addNote(track, channel, bitCode, time, 1, volume)
                time += 1 # Update time
        else:
            for i in range(4):
                MyMIDI.addNote(track, channel, bitCode, time, 1, volume)
                time += 1 # Update time
            
        
    for wordInPrhase in myPhrase.phrase:
        for syllable in wordInPrhase:
            
            # Tick in first beat
            if metronome == True:
                MyMIDI.addNote(track, channel, bitCode, time, 1, volume)
                
            for item in syllable.getRythm():
                #print(item)
                MyMIDI.addNote(track, channel, soundCode, time, item, volume)
                time += item # Update time
                #print("timeitem: %s -> : %s"% (time, item))
       
    #If name is empty geneates a TimeStampName
    if not fileName and not fileName.strip():
        timestr = timeUtil.strftime("%Y%m%d-%H%M%S")
        fileName = "%s-%s"% (timestr, myPhrase.meter.name)
                
    #Write midi file
    with open(fileName + '.mid', "wb") as output_file:
        MyMIDI.writeFile(output_file)             
    
    #Write text file      
    print(myPhrase,  file=open(fileName + '.txt', 'w'))        
        
    print('written file to %s'% fileName)    
        

def main():
    myPhraseObj = phrase.Phrase(4,phrase.Meter.DUPLE) #length:2, meter=DUPLE
    print(myPhraseObj)
    toFile('', myPhraseObj)
    
if __name__== "__main__":
    main()




