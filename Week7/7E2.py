fname = input("Input File Address/File Name:")

try:
    fhand = open(fname)
except:
    print("File Cannot Be Opened, Try Again.")
    quit()

total = 0
count = 0

for line in fhand :
    if not 'X-DSPAM-Confidence:' in line :
        continue
    position = line.find(':')
    number = float(line[position+1 : ])
    count = count + 1
    total = total + number
    print(count, line[19 : ])

average = total/count
print("Average Spam Confidence:", average)

#X-DSPAM-Confidence
