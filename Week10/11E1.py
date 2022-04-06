import re
fname = 'mbox.txt'
fhand = open(fname)

count = 0
input = input('Enter a regular expression: ')

for line in fhand:
    line = line.rstrip()
    if re.findall(input, line) != []:
        count += 1

print(fname + ' had ' + str(count) + ' lines that matched ' + input)
