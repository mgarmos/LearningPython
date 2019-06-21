import random
import patterns
import word

from midiutil import MIDIFile

track    = 0
channel  = 9
time     = 0    # In beats

tempo    = 60   # In BPM
volume   = 127  # 0-127, as per the MIDI standard

words = [patterns.A2, patterns.A2, patterns.A4, patterns.A5]
words = [patterns.A1, patterns.A1, patterns.A2, patterns.A3, patterns.A4, patterns.A5]


# print(patterns.A3().getNotes())


def printSong(cadena):
	for i in range(len(cadena)):
		print('|' + cadena[i],end='')
		if i%4 == 3:
			print("|")


def getWord(length, patternChoice):
	
	word = []
	for i in range(length):
		pattern = random.choice(patternChoice)()
		word.append(pattern.name)	
	
	#print(word)
	

text = []
song = []

# Introduction
for i in range(4):
    event = [track, channel,34,time,1,127]
    song.append(event)
    time += 1 # Update time

for i in range(136):
	pattern = random.choice(words)()
	text.append(pattern.name)

    # Tick in first measure
	event = [track, channel,34,time,1,127]
	song.append(event)


	for note in pattern.getNotes():
		
		event = [track, channel]
		event.append(note[0])
		event.append(time)
		event.append(note[1])
		event.append(volume)
		#print(event)
		song.append(event)
        time += note[1] # Update time		

		

printSong(text)

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
MyMIDI.addTempo(track, 0, tempo)


for event in song:
    track, channel, pitch, time, duration, volume = event
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)

with open("C:/Users/magarami/Desktop/rythmTraining.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)