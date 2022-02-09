count = 0
total = 0

while True:
    inpt = input("Enter a number: ")
    if inpt == "done" :
        break
    try :
        val = float(inpt)
    except :
        print("Invalid input")
    #    num = num - 1 #Does not include invalid inputs for count
    #    total = total - val #Does not include invalid inputs for total,
    # continue makes the above lines impact final results negatively, but does the same job
        continue
    count = count + 1
    total = total + val

print(total, num, total/num)
