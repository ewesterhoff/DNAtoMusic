import mido
import csv

def readInMidi(myFile):
    mid = mido.MidiFile(myFile)

    notes = []
    noteLengths = []
    for msg in mid.play():
        notes.append(msg.note)
        noteLengths.append(msg.time)
    return notes, noteLengths

def createFirstTwoAcids(notes):
    lengthSong = int(len(notes))

    for i in range(0, lengthSong//2):
        notes[i] = notes[i*2]

    sequence = []
    sequenceU = []
    startingPitch = 60 #sets the key to C major
    notesInKey = [0,2,4,5,7,9,11,12,14,16,17,19,21,23,24,26]
    acidsList = ['AA', 'AT', 'AC', 'AG',
                 'TA', 'TT', 'TC', 'TG',
                 'CA', 'CT', 'CC', 'CG',
                 'GA', 'GT', 'GC', 'GG']
    possibleNumNotes = int(len(notesInKey))
    for pitch in notes:
        for i in range(0, possibleNumNotes):
            if pitch == startingPitch+notesInKey[i]:
                acid = acidsList[i]
        sequence.append(acid)
    return sequence

def createThirdAcid(noteLengths):
    sequenceThird = []
    for l in noteLengths:
        if l == .25:
            thirdAcid = 'C'
            sequenceThird.append(thirdAcid)
        if l == .5:
            thirdAcid = 'A'
            sequenceThird.append(thirdAcid)
        if l == .75:
            thirdAcid = 'G'
            sequenceThird.append(thirdAcid)
        if l == 1:
            thirdAcid = 'T'
            sequenceThird.append(thirdAcid)
    return sequenceThird

def writeToText(data):
    file = open("DNAfromMidi3.txt", "w")
    for i in data:
        file.write(i+"")
    file.close()


myNotes, myNoteLengths = readInMidi('DNAmusic3.mid')
firstTwo = createFirstTwoAcids(myNotes)
third = createThirdAcid(myNoteLengths)
finalSequence = []
lengthSequence = int(len(third))

for a in range(0, lengthSequence):
    nuc = firstTwo[a] + third[a]
    finalSequence.append(nuc)

writeToText(finalSequence)
