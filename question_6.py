import os.path
import sys
fname = input("enetr the filename whose contants are to sorted: ")
if not os.path.isfile(fname):
    print("file", fname, "doesn't exist")
    sys.exit(0)
infile=open(fname, "r")
mylist = infile.readlines()
print(mylist)

lineList = []
for line in mylist:
    lineList.append(line.strip())
print(lineList)
lineList.sort()
print(lineList)

outfile = open("sorted.txt", "w")
for line in lineList:
    outfile.write(line + "\n")
infile.close()
outfile.close()

if os.path.isfile("sorted.txt"):
    print("\nfile containing sorted content sorted.txt created successfull")
    print("sorted.txt contains", len(lineList), "lines")
    print("contents of sorted.txt")
    print("===============================================================================")
    rdFile = open("sorted.txt", "r")
    for line in rdFile:
        print(line, end='')
