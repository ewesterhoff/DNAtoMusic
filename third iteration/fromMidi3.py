import mido
import csv

mid = mido.MidiFile('DNAmusic3.mid')

notes = []
noteLengths = []
for msg in mid.play():
    notes.append(msg.note)
    noteLengths.append(msg.time)

lengthSong = int(len(notes))

for i in range(0, lengthSong//2):
    notes[i] = notes[i*2]

durations = []
blanks = []

# for i in range(lengthOfNoteLengths):
#     if noteLengths[i] != 0
#         durations.append(noteLengths[i])
# print(durations)

sequence = []
sequenceU = []
startingPitch = 60 #sets the key to C major
for pitch in notes:
    if pitch == startingPitch + 0:
        acid = 'AA'
    if pitch == startingPitch + 2:
        acid = 'AT'
    if pitch == startingPitch + 4:
        acid = 'AC'
    if pitch == startingPitch + 5:
        acid = 'AG'

    if pitch == startingPitch + 7:
        acid = 'TA'
    if pitch == startingPitch + 9:
        acid = 'TT'
    if pitch == startingPitch + 11:
        acid = 'TC'
    if pitch == startingPitch + 12:
        acid = 'TG'

    if pitch == startingPitch + 14:
        acid = 'CA'
    if pitch == startingPitch + 16:
        acid = 'CT'
    if pitch == startingPitch + 17:
        acid = 'CC'
    if pitch == startingPitch + 19:
        acid = 'CG'

    if pitch == startingPitch + 21:
        acid = 'GA'
    if pitch == startingPitch + 23:
        acid = 'GT'
    if pitch == startingPitch + 24:
        acid = 'GC'
    if pitch == startingPitch + 26:
        acid = 'GG'
    sequence.append(acid)

for l in noteLengths:
    if l == .25:
        thirdAcid = 'C'
        sequenceU.append(thirdAcid)
    if l == .5:
        thirdAcid = 'A'
        sequenceU.append(thirdAcid)
    if l == .75:
        thirdAcid = 'G'
        sequenceU.append(thirdAcid)
    if l == 1:
        thirdAcid = 'T'
        sequenceU.append(thirdAcid)

finalSequence = []
lengthSequence = int(len(sequenceU))

for a in range(0, lengthSequence):
    nuc = sequence[a] + sequenceU[a]
    finalSequence.append(nuc)
print(finalSequence)

file = open("DNAfromMidi3.txt", "w")
for i in finalSequence:
    file.write(i+"")
file.close()
