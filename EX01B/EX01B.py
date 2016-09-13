import math

def fun_z(x, y):
    return((5/x)*(math.pow((x*x)+(y*y), 1/3)))/(7*(math.pow((math.cos(math.pi*x)), 2)))
print(fun_z(5, 10))