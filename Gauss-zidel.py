def gaus_zidel(matrix,b):
    xn = 0
    yn = 0
    zn = 0
    epsilon = 0.0001
    Iteration = 0
    for Iteration in range (100):
        xn_1 =   (b[0] - matrix[0][1]*yn - matrix[0][2]*zn) / matrix[0][0]
        Yn_1 =   (b[1] - matrix[1][0]*xn_1 - matrix[1][2]*zn) / matrix[1][1]
        Zn_1 =   (b[2] - matrix[2][0] * xn_1 - matrix[2][1] * Yn_1) / matrix[2][2]
        print("gaus_zidel Iteration number:",Iteration,xn_1," ",Yn_1," ",Zn_1)
        if xn_1 - xn == 0 and Yn_1 - yn == 0 and Zn_1 - zn ==0:
            break
        if xn_1 - xn < epsilon:
            xn_1 = round(xn_1,3)
        if Yn_1 - yn < epsilon:
            Yn_1=round(Yn_1, 3)
        if Zn_1 - zn < epsilon:
            Zn_1 = round(Zn_1, 3)
        xn = xn_1
        yn = Yn_1
        zn = Zn_1

def jacobi(matrix,b):
    xn = 0
    yn = 0
    zn = 0
    epsilon = 0.0001
    Iteration = 0
    for Iteration in range(100):
        xn_1 = (b[0] - matrix[0][1] * yn - matrix[0][2] * zn) / matrix[0][0]
        Yn_1 = (b[1] - matrix[1][0] * xn - matrix[1][2] * zn) / matrix[1][1]
        Zn_1 = (b[2] - matrix[2][0] * xn - matrix[2][1] * yn) / matrix[2][2]
        print("jacobi Iteration number:", Iteration, xn_1, " ", Yn_1, " ", Zn_1)
        if xn_1 - xn == 0 and Yn_1 - yn == 0 and Zn_1 - zn == 0:
            break
        if xn_1 - xn < epsilon:
            xn_1 = round(xn_1, 3)
        if Yn_1 - yn < epsilon:
            Yn_1 = round(Yn_1, 3)
        if Zn_1 - zn < epsilon:
            Zn_1 = round(Zn_1, 3)
        xn = xn_1
        yn = Yn_1
        zn = Zn_1

def dominant_pivot(matrix):
    if (abs(matrix[0][0]) > abs(matrix[0][1] + matrix[0][2]) and abs(matrix[1][1]) > abs(matrix[1][0] + matrix[1][2]) and abs(matrix[2][2]) > abs(matrix[2][0] + matrix[2][1])) or (abs(matrix[0][0]) > abs(matrix[0][1]) and abs(matrix[0][0]) > abs(matrix[0][2])):
        return True
    print("Not a dominant pivot")
    return False

matrix = [[3,-1,1],[0,1,-1],[1,1,-2]]
b = [4,-1,-3]
#matrix2 = [[3,-1,1],[0,1,-1],[1,1,-2]]
#b2 = [4,-1,-3]
gaus_zidel(matrix,b)
jacobi(matrix,b)
print(dominant_pivot(matrix))