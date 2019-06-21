import phrase
from MIDIUtil import MIDIFile

tempo    = 60   # In BPM
track    = 0
channel  = 9
volume = 127


#def toFile(output_file, notes)
#    for note in notes:
#        track, channel, pitch, time, duration, volume = event
#        MyMIDI.addNote(track, channel, pitch, time, duration, volume)
#
#    with open("C:/Users/magarami/Desktop/rythmTraining.mid", "wb") as output_file:
#        MyMIDI.writeFile(output_file)

def toFile(output_file, myPhrase, metronome = True):
    time = 0
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, 0, tempo)
    
    if metronome == True: #Only for duple meter -> TODO parametrize
        # Tick in first measure
        MyMIDI.addNote(track, channel, 34, time, 1, volume)
        time += 1 # Update time

    notes = phrase.phraseToNotes(myPhrase)
    for note in notes:
        # Tick in first measure
        if metronome == True: #Only for duple meter -> TODO parametrize
            MyMIDI.addNote(track, channel, 34, time, 1, volume)
    
        MyMIDI.addNote(track, channel, note.getPitch(), time, note.getDuration(), volume)
        #print(str(time) + '-> ' + str(note))        
        time += note.getDuration() # Update time
        
        

    #Write file
    with open("rythmTraining.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
    

    # Convert notes to midi events
    print('Metronome: ' + str(metronome))
    print('Tempo: ' + str(tempo))
    phrase.printPhrase(myPhrase)



#phrase.printPhrase(myPhrase)
myPhrase = phrase.getPhrase(4,phrase.Meter.TRIPLE)
toFile('pp.mid', myPhrase, )
