"""Develop a program to sort the contents of a text file and write the sorted contents into
a separate text file."""


import os.path
import sys
fname = input("Enter the filename whose contents are to be sorted : ")
if not os.path.isfile(fname):
    print("File", fname, "doesn't exists")
    sys.exit(0)
infile = open(fname, "r")
myList = infile.readlines()

lineList = []
for line in myList:
    lineList.append(line.strip())

lineList.sort()


outfile = open("sorted.txt","w")
for line in lineList:
    outfile.write(line + "\n")
infile.close() # Close the input file
outfile.close() # Close the output file
if os.path.isfile("sorted.txt"):
    print("\nFile containing sorted content sorted.txt created successfully")
    print("sorted.txt contains", len(lineList), "lines")
    print("Contents of sorted.txt")
    print("===========================================================")
    rdFile = open("sorted.txt","r")
    for line in rdFile:
        print(line, end="")