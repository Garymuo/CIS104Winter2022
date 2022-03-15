fhand = open('romeo.txt')
word_list = []

for line in fhand :
    words = line.split()
    for word in words :
        if word in word_list :
            continue
        word_list.append(word)
print(sorted(word_list))
