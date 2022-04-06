import re
fname = input("Enter file:")
fhand = open(fname)
total = 0

for line in fhand :
    numbers = re.findall('[0-9]+', line)
    if not numbers :
        continue
    else :
        for number in numbers :
            total += float(number)

print(total)
