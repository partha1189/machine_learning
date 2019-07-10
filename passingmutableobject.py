def double(y):
    """local variable y is different from global var y"""
    y = y * 2

def changeit(lst):
    """lst refers to the same global list lst"""
    lst[0] = "Michigan"
    lst[1] = "Wolverines"

y = 5 #global variable
double(y)
print(y)

mylst = ['our','students','are','awesome']
changeit(mylst)
print(mylst)