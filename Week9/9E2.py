fname = input("Input File Name")

try:
    fhand = open(fname)
except :
    print("Given File Threw An Error, Using Mbox-short.txt")
    fhand = open("mbox-short.txt")

dates = dict()
for lines in fhand :
    words = lines.split()
    if len(words) < 3 or words[0] != "From" :
        continue
    else:
        date = words[2]
        #print(date)
        dates[date] = dates.get(date, 0) + 1
#print(dates.items())
for key,value in dates.items() :
    print(key , value)
