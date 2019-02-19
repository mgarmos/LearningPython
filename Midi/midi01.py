#!/usr/bin/env python

'''midi01.py
Crear una aaray de notas y generar el archivo
'''
from midiutil import MIDIFile
song = []

degrees  = [61, 63, 66, 68, 70, 73, 75, 78, 80, 82]  # MIDI note number

track    = 0
tempo    = 120   # In BPM
time     = 0    # In beats

note01 =[0, 0, 66, 0, 0.5, 127]
note02 =[0, 0, 82, 0.5, 0.5, 127]
note03 =[0, 0, 73, 1, 0.5, 127]
note04 =[0, 0, 63, 1.5, 0.5, 127]
note05 =[0, 0, 61, 2, 1, 127]
note06 =[0, 0, 73, 3, 1, 127]
note07 =[0, 0, 78, 4, 0.25, 127]
note08 =[0, 0, 63, 4.25, 0.25, 127]
note09 =[0, 0, 73, 4.5, 0.25, 127]
note10 =[0, 0, 78, 4.75, 0.25, 127]

song.append(note01)
song.append(note02)
song.append(note03)
song.append(note04)
song.append(note05)
song.append(note06)
song.append(note07)
song.append(note08)
song.append(note09)
song.append(note10)


MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

# for track, channel, pitch, time, duration, volume in enumerate(song):
#     MyMIDI.addNote(track, channel, pitch, time, duration, volume)

for note in song:
    track, channel, pitch, time, duration, volume = note
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    print (note)

with open("C:/Users/magarami/Desktop/major-scale1.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
