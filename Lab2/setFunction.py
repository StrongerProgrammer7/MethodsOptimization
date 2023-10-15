import numpy as np


def function_1(x, y):
    return x ** 2.0 + y ** 2.0


def function_2(x, y):
    return np.sin(x) * np.cos(y)


def function_Bila(x, y):
    return (1.5 - x + x * y) ** 2.0 + (2.25 - x + x * y ** 2.0) ** 2.0 + (
            2.625 - x + x * y ** 3.0) ** 2.0  # -4.5< x,y < 4.5


def function_Buta(x, y):
    return (x + 2 * y + 7) ** 2.0 + (2 * x + y - 5) ** 2.0  # -10 < x,y < 10


def function_Bukina(x, y):
    return 100 * np.sqrt(np.abs(y - 0.01 * x ** 2.0)) + 0.01 * np.abs(x + 10)  # -15 < x < -5 ; -3 <y <3


def function_Eggholder(x, y):
    return -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47)))) - x * np.sin(
        np.sqrt(np.abs(x - (y + 47))))  # 512 < x ,y < 512


def quadratic(x, y):
    return 2 * np.power(x, 2) + 3 * np.power(y, 2) + (4 * x * y) - (6 * x) - (3 * y)

def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

def func_ROMA(x,y):
    return 3*x*y-x**2*y-x*y**2

chooseFunc = {
    "function_1": {'f': function_1, 'from': -5, 'to': 5},
    "function_2": {'f': function_2, 'from': -5, 'to': 5},
    "Bila": {'f': function_Bila, 'from': -4.5, 'to': 4.5},
    "Buta": {'f': function_Buta, 'from': -10, 'to': 10},
    "Bukina": {'f': function_Bukina, 'x': {1: -15, 2: -5}, 'y': {1: -3, 2: 3}},
    "Eggholder": {'f': function_Eggholder, 'from': -128, 'to': 128},
    "quadratic": {'f': quadratic, 'from': -5, 'to': 5},
    "rosenbrock":{'f':rosenbrock,'from':-10,'to':10},
    "ROMA":{'f':func_ROMA,'from':-10,'to':10}
}
