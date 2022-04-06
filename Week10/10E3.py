fname = input('Enter file name: ')
try:
    fhand = open(fname)
except :
    print('File cannot be opened:', fname)
    exit()
dictionary = dict()
lst = list()
counts = 0


for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words :
        for letter in word :
            print(letter)
            if letter == "a" or letter == "b" or letter == "c" or letter == "d" or letter == "e" or letter == "f" or letter == "g" or letter == "h" or letter == "i" or letter == "j" or letter == "k" or letter == "l" or letter == "m" or letter == "n" or letter == "o" or letter == "p" or letter == "q" or letter == "r" or letter == "s" or letter == "t" or letter == "u" or letter == "v" or letter == "w" or letter == "x" or letter == "y" or letter == "z" :
                counts += 1
                dictionary[letter] = dictionary.get(letter, 0) + 1
            else :
                continue
for key, value in list(dictionary.items()):
    lst.append((value / counts, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
