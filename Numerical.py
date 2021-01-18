import math
import sys

print(abs(round(3.0*(((4.0/3.0)-1)))-1))

value = 1
epsilon = 1
#sum = value + epsilon
counter = 0
while value + epsilon != 1:
    epsilon = epsilon / 2
   # sum = value + epsilon
    counter += 1

print("Loop Counter: ",counter ,"\nEpsilon: ",epsilon)

print(sys.float_info.epsilon)


#Fact = input("Enter factorial number ")
#print(str(factorial(Fact)))



#Celc = input("Enter degrees in celcius ")
#print(str(Tempc(Celc)))