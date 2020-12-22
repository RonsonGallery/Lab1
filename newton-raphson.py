# Roni Gerkerov - 316583145
# Eden Mozes - 315997049

def newton_raphson_method(func, deriv, x, tolerence, max_iterations, real_root=None):
    if deriv(x) == 0:
        print("Newton-Raphson method will fail.")
        return None
    else:
        iterations = 1
        while abs(func(x) / deriv(x)) >= tolerence and iterations <= max_iterations:
            current_iteration_print = "Iteration: {0}".format(iterations)
            if func(x) == 0:
                print(current_iteration_print + "Found exact solution: {0}".format(x))
                return x
            x = x - func(x) / deriv(x)
            if deriv(x) == 0:
                print("Newton-Raphson method will fail.")
                return None
            current_iteration_print += ", Current root approximation: {0}".format(x)
            if real_root is not None:
                current_iteration_print += ", Difference from the real root: {0}".format(abs(real_root - x))
            iterations = iterations + 1
            print(current_iteration_print)

        if real_root is not None:
            print("Final approximation: {0}, Difference from the real root: {1}".format(x, abs(real_root - x)))
        else:
            print("Final approximation: {0}".format(x))
        return x


def f1(x):
    return x ** 3 -x - 1


def df1(x):
    return 3 * (x ** 2) -1


print(newton_raphson_method(f1, df1, 1.5, 0.001, 20))