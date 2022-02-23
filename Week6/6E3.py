string = input("Enter String:")
character = input("Enter Character")

if len(character) > 1 :
    print("Input Only One Character!")
    quit()

def count(string, character) :
    count = 0
    for letter in string:
        if letter == character:
            count = count + 1
    print(count)

count(string, character)

quit()
