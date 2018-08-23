import numpy as np
from scipy import optimize


def Rosenbrock(x):
    """
    This is the function for Rosenbrock with n=3
    :param x: a list representing the input vector [x1,x2,x3]
    :return: a number which is the Rosenbrock value
    """
    return 100 * (x[2] - x[1] ** 2) ** 2 + (1 - x[1]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def gradient(x):
    """
    This is the calculate the gradident of Rosenbrock when n=3
    :param x: a list representing the input vector [x1,x2,x3]
    :return: a list representing the gradient vector, which has length of 3
    """
    return np.array([-400 * x[0] * x[1] + 400 * x[0] ** 3 - 2 * (1 - x[0]),
                     -400 * x[1] * x[2] + 400 * x[1] ** 3 - 2 * (1 - x[1]) + 200 * (x[1] - x[0] ** 2),
                     200 * (x[2] - x[1] ** 2)])


if __name__ == "__main__":
    x1 = [222, 4, 1]
    x2 = [-4, 5, 99]
    x3 = [66, 91, 20000]
    x4 = [34, 1, -5]
    x5 = [2, -5, 2]
    x = [x1, x2, x3, x4, x5]
    res = []
    for x0 in x:
        res.append(optimize.minimize(Rosenbrock, x0, method='BFGS', jac=gradient).fun)
    print(min(res))
