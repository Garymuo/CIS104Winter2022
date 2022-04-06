import re

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()

revision = list()

for line in fhand:
    line = line.rstrip()
    temp = re.findall('^New Revision: ([0-9.]+)', line)
    if temp != [] :
        for value in temp:
            value = float(value)
            revision = revision + [value]

sum = sum(revision)
count = float(len(revision))
average = sum / count

print(average)
