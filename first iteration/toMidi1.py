#!/usr/bin/env python
import csv
from midiutil import MIDIFile

#first iteration
results = ['A', 'G', 'T', 'C', 'A', 'G', 'G', 'T', 'C', 'A', 'A', 'C']
#eventually results will be imported from txt file

#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees = []
for i in results:
    #i = results[entry]
    if i == 'A':
        pitch = 60
    if i == 'T':
        pitch = 64
    if i == 'C':
        pitch = 67
    if i == 'G':
        pitch = 72
    degrees.append(pitch)

print(degrees)
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1, adjust_origin = True)  # One track
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("firstSteps.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
