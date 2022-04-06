fname = input("Input File Name")

try:
    fhand = open(fname)
except :
    print("Given File Threw An Error, Using Mbox-short.txt")
    fhand = open("mbox-short.txt")

users = dict()
lst = list()
for lines in fhand :
    words = lines.split()
    if len(words) < 3 or words[0] != "From" :
        continue
    else:
        user = words[1]
        #print(user)
        users[user] = users.get(user, 0) + 1
#print(users.items())
for key,value in users.items() :
    lst.append( (value, key) )

lst = sorted(lst, reverse=True)
print(lst)
print("Most Commits By:", lst[0])
