import pylab
import string

inFile = open('julyTemps.txt', 'r', 0)
high=[]
low=[]
diffTemps=[]
lines = inFile.readlines()
for line in lines:
    fields = string.split(line)
    if len(fields)<3 or not fields[0].isdigit():
        continue
    high.append(int(fields[1]))
    low.append(int(fields[2]))
    diffTemps=int(fields[1])-int(fields[2])
    
print high
print low

