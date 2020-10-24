import math

def Tempc(Celc):
    return float(Celc) * 9/5 + 32

def factorial(n):
    if int(n) < 2:
        return 1

    num = 1
    i = 0
    while i < int(n):
        i += 1
        num *= i
    return num
def Cubes():
    for n in range(10):
        print(str(str(n) + "\t" + str(n * n) + "\t" + str(n * n * n)))
def gcd(x,y):
    for i  in range (1,y):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd
#x , y = input("Enter numbers to gcd ") , input("")
#print(gcd(int(x),int(y)))

#x = input("Enter X ")
#print(str(((math.exp(float(x))-1)/float(x))-1))
print(abs((3.0*((4.0/3.0)-1))-1))
value = 1
epsilon = 1
#sum = value + epsilon
counter = 0
while value != sum:
    epsilon = epsilon / 2
    sum = value + epsilon
    counter += 1

print("Loop Counter: ",counter ,"\nEpsilon: ",epsilon)



#Fact = input("Enter factorial number ")
#print(str(factorial(Fact)))



#Celc = input("Enter degrees in celcius ")
#print(str(Tempc(Celc)))