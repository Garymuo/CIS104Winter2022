hours = input("How many hours did you work?")
rate = input("What rate were you working at?")

try:
    fHours = float(hours)
    fRate = float(rate)
except:
    print("Error, Please Input Numeric Value")

if fHours > 40 :
    #rhours = 1.5(hours - 40) + 40
    total = (1.5 * (fHours - 40) + 40) * fRate

else: total = fHours * fRate
print("You made", total, "dollars!")
