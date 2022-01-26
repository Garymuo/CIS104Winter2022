try:
    grade = input("Input Grade Value")
    fGrade = float(grade)
except:
    print("Error, Bad Score")
    quit()


if fGrade >= .9 :
    print("A")
elif fGrade >= .8 :
    print("B")
elif fGrade >= .7 :
    print("C")
elif fGrade >= .6 :
    print("D")
else:
    print("F")

quit()
