def double(y):
    """local variable y is different from global var y"""
    y = y * 2

def changeit(lst):
    """lst refers to the same global list lst"""
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
    return lst

y = 5 #global variable
double(y)
print(y)

mylst = ['our','students','are','awesome']
#changeit(mylst)
newlst = changeit(list(mylst)) #This creates a new list
print(mylst)
print(newlst)