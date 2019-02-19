#!/usr/bin/env python

from midiutil import MIDIFile
import random

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees1  = [61, 63, 66, 68, 70, 73, 75, 78, 80, 82]  # MIDI note number

track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 127  # 0-127, as per the MIDI standard

note = []
music = []

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees1):
    note = [track, channel, pitch, time + i, random.choice(degrees1), time + i, duration, volume]
    music.append(note)
   
    #MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    MyMIDI.addNote(track, channel, random.choice(degrees1), time + i, duration, volume)


print(music)

with open("C:/Users/magarami/Desktop/major-scale1.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)