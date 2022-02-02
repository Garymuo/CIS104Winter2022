hours = input("How many hours did you work?")
rate = input("What rate were you working at?")

fHours = float(hours)
fRate = float(rate)

def computepay(fHours, fRate):

    if fHours > 40 :
        #rhours = 1.5(hours - 40) + 40
        total = (1.5 * (fHours - 40) + 40) * fRate

    else: total = fHours * fRate

    print("You made", total, "dollars!")

computepay(fHours, fRate)

quit()
