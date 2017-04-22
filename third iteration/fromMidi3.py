import mido
import csv
#from itertools import islice

def every_other(l):
    return l[1::2]

def readInMidi(myFile):
    mid = mido.MidiFile(myFile)

    notes = []
    noteLengths = []
    for msg in mid.play():
        notes.append(msg.note)
        noteLengths.append(msg.time)
    return notes, noteLengths

def removeTriplets(notes, noteLengths):
    #which indicies triplets happen at
    exclude_indices = [i for i in range(len(noteLengths)) if noteLengths[i] == (1/6)]
    #get rid of triplets in noteLengths
    noteLengths = [n for n in noteLengths if n != (1/6)]
    #remove the same notes from the pitch list
    notes = [notes[i] for i in range(len(notes)) if i not in exclude_indices]
    # notes = [n for n in notes if (n[0] != 1/6)]
    return notes, noteLengths

def removeSixthTurnaround(notes, noteLengths, startingPitch):
    key_indices = [i for i in range(len(notes)) if notes[i] == startingPitch+8]
    indicies_to_remove = [x+1 for x in key_indices]
    indicies_to_remove.append([x+2 for x in key_indices])
    print(indicies_to_remove)

    notes = [notes[i] for i in range(len(notes)) if i not in indicies_to_remove]
    noteLengths = [noteLengths[i] for i in range(len(noteLengths)) if i not in indicies_to_remove]
    return notes, noteLengths

def createFirstTwoAcids(notes, noteLengths, startingPitch):
    sequence = []
    sequenceU = []
    #notesInKey = [0,2,4,5,7,9,11,12,14,16,17,19,21,23,24,26]
    notesInKey = [0,2,4,5,7,9,10,8,12,14,17,19,21,16,11,23] #increased key pattern
    acidsList = ['AA', 'AT', 'AC', 'AG',
                 'TA', 'TT', 'TC', 'TG',
                 'CA', 'CT', 'CC', 'CG',
                 'GA', 'GT', 'GC', 'GG']

    possibleNumNotes = int(len(notesInKey))
    for pitch in notes:
        print(pitch)
        for i in range(0, possibleNumNotes):
            if pitch == startingPitch+notesInKey[i]:
                acid = acidsList[i]
        sequence.append(acid)
    return sequence

def createThirdAcid(noteLengths):
    sequenceThird = []
    lengths_iter = iter(noteLengths)
    for l in lengths_iter:
        if l == .25:
            thirdAcid = 'T'
            sequenceThird.append(thirdAcid)
        if l == .5:
            thirdAcid = 'A'
            sequenceThird.append(thirdAcid)
        if l == .75:
            thirdAcid = 'G'
            sequenceThird.append(thirdAcid)
        if l == 1:
            thirdAcid = 'C'
            sequenceThird.append(thirdAcid)
    return sequenceThird

def writeToText(data):
    file = open("DNAfromMidi3.txt", "w")
    for i in data:
        file.write(i+"")
    file.close()

def start():
    startingPitch = 60 #sets the key to C major
    myNotes, myNoteLengths = readInMidi('DNAmusic3.mid')
    myNotes = every_other(myNotes)
    myNoteLengths = every_other(myNoteLengths)

    myNotes, myNoteLengths = removeTriplets(myNotes, myNoteLengths)
    myNotes, myNoteLengths = removeSixthTurnaround(myNotes, myNoteLengths, startingPitch)
    firstTwo = createFirstTwoAcids(myNotes, myNoteLengths, startingPitch)
    third = createThirdAcid(myNoteLengths)

    finalSequence = []
    lengthSequence = int(len(third))

    for a in range(0, lengthSequence):
        nuc = firstTwo[a] + third[a]
        finalSequence.append(nuc)

    writeToText(finalSequence)

if __name__ == '__main__':
    start()
