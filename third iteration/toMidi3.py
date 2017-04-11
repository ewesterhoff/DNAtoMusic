#!/usr/bin/env python
import csv
from midiutil import MIDIFile

#first iteration
#results = ['A', 'G', 'T', 'C', 'A', 'G', 'G', 'T', 'C', 'A', 'A', 'C']

results = []
with open("sampleDNA6.txt") as f:
  while True:
    c = f.read(3)
    if not c:
      break
    results.append(c)

#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees = []
speeds = []
for a in results:
    i = a[0:2] #determines pitch
    c = a[2] #determines...something?
    startingPitch = 60 #determines key 60 = C MAJOR

    if i == 'AA':
        pitch = startingPitch + 0
    if i == 'AT':
        pitch = startingPitch + 2
    if i == 'AC':
        pitch = startingPitch + 4
    if i == 'AG':
        pitch = startingPitch + 5

    if i == 'TA':
        pitch = startingPitch + 7
    if i == 'TT':
        pitch = startingPitch + 9
    if i == 'TC':
        pitch = startingPitch + 11
    if i == 'TG':
        pitch = startingPitch + 12

    if i == 'CA':
        pitch = startingPitch + 14
    if i == 'CT':
        pitch = startingPitch + 16
    if i == 'CC':
        pitch = startingPitch + 17
    if i == 'CG':
        pitch = startingPitch + 19

    if i == 'GA':
        pitch = startingPitch + 21
    if i == 'GT':
        pitch = startingPitch + 23
    if i == 'GC':
        pitch = startingPitch + 24
    if i == 'GG':
        pitch = startingPitch + 26

    if c == 'A':
        duration = 1
    if c == 'T':
        duration = 2
    if c == 'C':
        duration = .5
    if c == 'G':
        duration = 1.5

    degrees.append(pitch)
    speeds.append(duration)

print(degrees)
track    = 0
channel  = 0
time     = 0    # In beats
#duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1, adjust_origin = True)  # One track
MyMIDI.addTempo(track, time, tempo)
currentTime = time

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, currentTime, speeds[i], volume)
    currentTime = currentTime+speeds[i]

with open("DNAmusic3.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
