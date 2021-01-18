#Roni Gerkerov - 316583145
#Eden Mozes - 315997049
import math

import sympy as sp
from numpy import log
x = sp.symbols('x')
f = sp.Function('f')

def func_calc(func,x,val):
    return func.subs(x,val).evalf()

def f(x):
    #x = sp.symbols('x')
    #x**5 -5*x - +2
    #(math.sin(x**2 + 5*x + 6))/(2*(2.718)**(-x))
    return (0.5*2.2718**x)*(math.sin(x**2 + 5*x + 6))

def bisection (a,b,epsilon):                  #Recives a range and returns the root in that range if one exists
    xl = a
    xr = b
    #k = round(-log(epsilon/(b-a))/log(2)) + 1
    iterator = 0
    #print(k)
    while abs((xl-xr)) >= epsilon:
        c = (xl+xr)/2
        prod = f(xl) * f(c)
        if prod > epsilon:
            xl = c
        elif prod < epsilon:
            xr = c
        #if iterator == int(k):
            #return None
        iterator += 1
    return c

def bisection_special (a,b,epsilon,f):                     #same as the previos one but for dervative
    xl = a
    xr = b
    while abs((xl-xr)) >= epsilon:
        c = (xl+xr)/2
        prod = func_calc(f,x,xl) * func_calc(f,x,c)
        if prod > epsilon:
            xl = c
        elif prod < epsilon:
            xr = c
    return c
iter = 0
def bigger_bisection(a,b,g):                             #recives a large range and uses bisection function to find all possible roots
    xl = a
    xr = b
    my_dict = {}
    while xr - 0.1 >= xl - 0.1:
        #    print(xr)
        my_dict[xr] = g(xr)
        xr = round(xr - 0.100, 2)
    current = 0
    last = f(b)
    current_key = 0
    last_key = 0
    roots = []
    for key in my_dict:
        current_key = key
        current = my_dict[key]
        #print(my_dict[key])
        if current * last < 0:
            #print(current, last)
            print("Potential root in this range: " + str( current_key), str(last_key))
            if bisection(current_key, last_key, 1e-10) != None:
                roots.append(bisection(current_key, last_key, 1e-10))
        last = current
        last_key = current_key
    return roots
def bigger_bisection_diff(a,b,g):                                   #same as previous only for the direvative version
    xl = a
    xr = b
    my_dict = {}
    while xr - 0.1 >= xl - 0.1:
        #print(xr)
        my_dict[xr] = func_calc(g,x,xr)
        xr = round(xr - 0.100, 2)
    current = 0
    last = func_calc(g,x,b)
    current_key = 0
    last_key = 0
    roots = []
    for key in my_dict:
        current_key = key
        current = my_dict[key]
        #print(my_dict[key])
        if check_root(my_dict[key]):
            roots.append(my_dict[key])
        if current * last < 0:
            #print(current, last)
            #print(current_key,last_key)
            roots.append(bisection_special(current_key, last_key, 1e-10,g))
        last = current
        last_key = current_key
    return roots
"""
my_dict = {}
while xr - 0.1 >= xl-0.1:
#    print(xr)
    my_dict[xr] = f(xr)
    xr = round(xr - 0.100,2)

current = 0
last = f(b)
current_key = 0
last_key = 0
roots = []
for key in my_dict:
    current_key = key
    current = my_dict[key]
    if current * last < 0:
        print(current,last)
        roots.append(bisection(current_key,last_key,1e-10))
    last = current
    last_key = current_key

"""
def check_root(x):
    if f(x) == 0:
        return True
    return False
def ftx(x):
    return 0.5 * (2.718 ** x) * (math.cos(x**2 + 6 + 5*x)*(5+2*x) + math.sin(x**2 + 6 + 5*x))
#print(key , current)
#answer = bisection(-5,5,1e-10)
a = -3
b = 1
x = sp.symbols('x')
solutions = bigger_bisection(a,b,f)
print(solutions)
#ftx = (sp.diff(f(x),x))
#check_roots = bigger_bisection_diff(a,b,ftx)
print("Potential roots for derivative:")
check_roots = bigger_bisection(a,b,ftx)
roots = list(filter(check_root,check_roots))
for i in roots:
    solutions.append(roots[i])
print("Answer with bisection method gives the root at X = ",solutions)
#print(f(check_roots[0]))
#print(f(check_roots[1]))