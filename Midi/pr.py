import random
import patterns

from midiutil import MIDIFile

track    = 0
channel  = 9
time     = 4    # In beats

tempo    = 60   # In BPM
volume   = 127  # 0-127, as per the MIDI standard

words = [patterns.A2, patterns.A2, patterns.A4, patterns.A5]
#words = [patterns.A1, patterns.A1, patterns.A2, patterns.A2, patterns.A3, patterns.A3, patterns.A4, patterns.A5]


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

for i in range(136):
	pattern = random.choice(words)()
	text.append(pattern.name)

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

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, 0, tempo)


for event in song:
    track, channel, pitch, time, duration, volume = event
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)

with open("C:/Users/magarami/Desktop/major-scale1.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
