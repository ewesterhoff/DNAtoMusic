# DNAtoMusic
Transforms a text file of atcg type into unique midi file
Requires mido, csv, midiUtil, and random be installed.  Sibelius is recommended as a viewing tool for the midi files.

## Goals of Project
This project will create a midi file from an existing text file of DNA.  In addition, the program will be able to read midi files and convert them into text files of DNA.

The overall goal of the project is to import the midi file into Sibelius, where it other sounds will be added to it to enhance the experience.  From there, a wav file will be generated, and imported into a video, where a visualization will scroll the DNA sequence used to generate the music across the screen.

## So, where's the biology?
The biology of this project comes from the text file that is being imported. A study has proposed a link between a gene in 8q.24.21 and perfect pitch. (https://www.ncbi.nlm.nih.gov/pubmed/11239158) More studies have reliably shown a link between perfect/absolute pitch and genetics, while relative pitch is something that can be achieved with enough musical training.

A flaw in the re-translation code actually has critical biological meaning.  At the end of the lines of the input DNA, the re-translated file will have an extra base pair, or be lacking one.  While the real DNA can be seen clearly in the re-translation, it is not perfect.  Biologically, this is a frameshift mutation.  The three base pairs are now shifted over one or two steps, and the proteins they code for are now entirely different.

## first iteration
Contained in the first iteration project folder is the basic files to read and write midi files.  These are the basis for the rest of the program

## second iteration
This version of the project begins to implement music theory in the generation of midi files.  The reading file will also be updated to be able to interpret them.

## third iteration
This version will explore more complex music generation algorithms.  The final DNA file will be chosen, and be used in this iteration along with sample files for testing.  The code will be cleaned up, with design and functionality considered.

## final version
The final wav file is included in the Deliverables folder, along with the critical code and text files.  
