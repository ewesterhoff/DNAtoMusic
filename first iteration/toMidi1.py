#!/usr/bin/env python
import csv
from midiutil import MIDIFile

results = open('sampleDNA1.txt').read()
print(results)

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
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
