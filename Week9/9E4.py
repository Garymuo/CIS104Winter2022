fname = input("Input File Name")

try:
    fhand = open(fname)
except :
    print("Given File Threw An Error, Using Mbox-short.txt")
    fhand = open("mbox-short.txt")

users = dict()
for lines in fhand :
    words = lines.split()
    if len(words) < 3 or words[0] != "From" :
        continue
    else:
        user = words[1]
        #print(user)
        users[user] = users.get(user, 0) + 1
#print(users.items())
largestValue = -1
largestKey = None
for key,value in users.items() :
    if largestValue < value :
        largestValue = value
        largestKey = key
    print(key , value)
print("Most Messages Sent By User:", largestKey, "Amount:" , largestValue)
