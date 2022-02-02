a = input("Input First Value")
b = input("Input Second Value")
c = input("Input Third Value")

def maxthree(a, b, c):

    if a > b and a > c :
        print(a)
    elif b > a and b > c :
        print(b)
    elif c > a and c > b :
        print(c)


maxthree(a, b, c)

quit()
