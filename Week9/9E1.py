fhand = open("words.txt")

counter = dict()
for line in fhand :
    #print(line) I used counter not fhand :(
    lowerline = line.lower()
    words = lowerline.split()
    for word in words :
        counter[word] = counter.get(word, 0) + 1
print(counter.keys())
#print(counter.items())
#counts uppercase as unqiue words
