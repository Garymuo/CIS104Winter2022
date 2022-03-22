fname = input("Input File Name")

try:
    fhand = open(fname)
except :
    print("Given File Threw An Error, Using Mbox-short.txt")
    fhand = open("mbox-short.txt")

domains = dict()
for lines in fhand :
    words = lines.split()
    if len(words) < 3 or words[0] != "From" :
        continue
    else:
        user = words[1]
        #print(user)
        address = user.split("@")
        domain = address[1]
        #print(addresssplit)
        #print(address)
        domains[domain] = domains.get(domain, 0) + 1
#print(users.items())
largestValue = -1
largestKey = None
for key,value in domains.items() :
    if largestValue < value :
        largestValue = value
        largestKey = key
    print(key , value)
print("Most Messages Sent By Domain:", largestKey, "Amount:" , largestValue)
