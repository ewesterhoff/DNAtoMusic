import mido
import csv

mid = mido.MidiFile('firstSteps.mid')
notes = []
for msg in mid.play():
    notes.append(msg.note)

length = len(notes)
length = int(length)

for i in range(0, length//2):
    notes[i] = notes[i*2]
print(notes)

sequence = []
for i in notes:
    if i == 60:
        acid = 'A'
    if i == 64:
        acid = 'T'
    if i == 67:
        acid = 'C'
    if i == 72:
        acid = 'G'
    sequence.append(acid)
print(sequence)

file = open("DNAfromMidi1.txt", "w")
for i in sequence:
    file.write(i)
file.close()
