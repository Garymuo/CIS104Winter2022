#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
fname = input("Enter file:")
if len(fname) < 3:
    fname = "mbox-short.txt" #just so I dont have to cop/paste mbox constantly
fhand = open(fname)

dictionary = dict()
lst = list()

for line in fhand :
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    timesplit = words[5].find(':')
    hour = words[5][:timesplit]
    dictionary[hour] = dictionary.get(hour, 0) + 1 

for key, val in list(dictionary.items()):
    lst.append((key, val))  #key = hour, val = count
lst.sort()
for key, val in lst:
    print(key, val)
