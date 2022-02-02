try:
    score = input("Input Grade Value")
    fScore = float(score)
except:
    print("Error, Bad Score")
    quit()

def computegrade(fScore):

    if fScore >= .9 :
        grade = print("A")
    elif fScore >= .8 :
        grade = print("B")
    elif fScore >= .7 :
        grade = print("C")
    elif fScore >= .6 :
        grade = print("D")
    else:
        grade = print("F")

    return(grade)

computegrade(fScore)


quit()
