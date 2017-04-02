#!/usr/bin/env python
import csv
from midiutil import MIDIFile

#first iteration
#results = ['A', 'G', 'T', 'C', 'A', 'G', 'G', 'T', 'C', 'A', 'A', 'C']

results = []
with open("sampleDNA3.txt") as f:
  while True:
    c = f.read(3)
    if not c:
      break
    results.append(c)

#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees = []
for a in results:
    i = a[0:2] #determines pitch
    c = a[2] #determines...something?

    print(i)
    if i == 'AA':
        pitch = 60
    if i == 'AT':
        pitch = 62
    if i == 'AC':
        pitch = 64
    if i == 'AG':
        pitch = 65

    if i == 'TA':
        pitch = 67
    if i == 'TT':
        pitch = 69
    if i == 'TC':
        pitch = 71
    if i == 'TG':
        pitch = 72

    if i == 'CA':
        pitch = 74
    if i == 'CT':
        pitch = 76
    if i == 'CC':
        pitch = 77
    if i == 'CG':
        pitch = 79

    if i == 'GA':
        pitch = 81
    if i == 'GT':
        pitch = 83
    if i == 'GC':
        pitch = 84
    if i == 'GG':
        pitch = 84

    degrees.append(pitch)

print(degrees)
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 110   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1, adjust_origin = True)  # One track
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("DNAmusic.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
