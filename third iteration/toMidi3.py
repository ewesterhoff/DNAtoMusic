#!/usr/bin/env python
import csv
from midiutil import MIDIFile

def formatDNAFile(rawFile):
    results = []
    with open(rawFile) as f:
      while True:
        c = f.read(3)
        if not c:
          break
        results.append(c)
    return results



def textToPitches(dnaText):
    degrees = []
    speeds = []
    startingPitch = 60 #determines key 60 = C MAJOR
    notesInKey = [0,2,4,5,7,9,11,12,14,16,17,19,21,23,24,26]
    acidsList = ['AA', 'AT', 'AC', 'AG',
                 'TA', 'TT', 'TC', 'TG',
                 'CA', 'CT', 'CC', 'CG',
                 'GA', 'GT', 'GC', 'GG']
    possibleNumAcidCombos = int(len(acidsList))
    for a in dnaText:
        i = a[0:2] #determines pitch
        c = a[2] #determines...something?

        for x in range(0, possibleNumAcidCombos):
            if i == acidsList[x]:
                pitch = startingPitch + notesInKey[x]

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
    return degrees, speeds


formattedForInsert = formatDNAFile("sampleDNA6.txt")
myDegrees, mySpeeds = textToPitches(formattedForInsert)

track    = 0
channel  = 0
time     = 0    # In beats
#duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1, adjust_origin = True)  # One track
MyMIDI.addTempo(track, time, tempo)
currentTime = time

for i, pitch in enumerate(myDegrees):
    MyMIDI.addNote(track, channel, pitch, currentTime, mySpeeds[i], volume)
    currentTime = currentTime+mySpeeds[i]

with open("DNAmusic3.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
