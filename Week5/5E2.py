largest = None
smallest = None

while True:
    inpt = input("Enter a number: ")
    if inpt == "done":
        break
    try:
        num = int(inpt)
    except :
        print("Invalid input")
        continue

    if largest == None or num > largest :
        largest = num
    elif smallest == None or num < smallest :
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
