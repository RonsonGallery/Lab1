import math

# globals
APPROX = 0.1
epsilon = 1e-5
MAX = 100


# function we are using
def function(x):
    return 1 * pow(x, 3) - x - 1


# Actual Secant Method
def secant(p0, p1):
    if (function(p1) - function(p0) == 0):
        return "Guess resulted in divison by 0 enter a different guess"
    for i in range(0, MAX):
        p = p1 - ((function(p1) * (p1 - p0)) / (function(p1) - function(p0)))
        #print(p)
        #print('Itteration:',i , ' - ', p)
        if abs(p - p1) < epsilon:
            return p
        print("{0:.4f}              {1:.4f}                 {2:.4f}                 {3:.4f}                 {4:.4f}             {5:.4f}             {6:.4f}".format(i,p0,function(p0),p1,function(p1),p,function(p)))
        p0 = p1
        p1 = p

    return "Them method failed after {} iterations" > format(MAX)

print("iteration            x0                     f(x0)                   x1                    f(x1)                x2                 f(x2)")
print("Secant method solution: x = ", secant(2, 1))
