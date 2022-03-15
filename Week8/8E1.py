#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
listone = [1, 2, 3, 4, 5]
listtwo = [1, 2, 3, 4, 5]

def chop(lst) :
    lst.pop(0)
    lst.pop()
    return()

def middle(lst) :
    newlst = lst[1:]
    newlst.pop()
    return newlst

choplist = chop(listone)
print(listone)
print(choplist)

middlelist = middle(listtwo)
print(listtwo)
print(middlelist)
