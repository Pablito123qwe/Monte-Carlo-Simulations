import math

import matplotlib.pyplot as plt
import numpy as np
import random
def rectangular_integration(start, end, number_of_rectangles):
    dx = (end-start) / number_of_rectangles
    x_i = 0
    result = 0
    for x in range(number_of_rectangles):
        result += math.sin(x_i)
        x_i += dx
    return result*dx

def rectangular_integration_accuracy(number_of_intervals):
    arguments = []
    values = []
    for x in range(1,number_of_intervals+1):
        arguments.append(x)
        values.append(2-rectangular_integration(0, math.pi, x))
    return arguments, values


def trapezoidal_integration(start, end, number_of_trapezoids):
    dx = (end - start) / number_of_trapezoids
    x_i = 0
    result = 0
    for x in range(number_of_trapezoids):
        x_i_next = x_i + dx
        result += (math.sin(x_i) + math.sin(x_i_next))/2 * dx
        x_i = x_i_next
    return result

def trapezoidal_integration_accuracy(number_of_intervals):
    arguments = []
    values = []
    for x in range(1,number_of_intervals+1):
        arguments.append(x)
        values.append(2-trapezoidal_integration(0, math.pi, x))
    return arguments, values

arguments, values = rectangular_integration_accuracy(1000)
# arguments, values = trapezoidal_integration_accuracy(1000)



def plot_errors(arguments, values):
    plt.plot(arguments, values, linestyle='-', color='blue')
    plt.grid(True)
    plt.yscale('log')
    plt.xscale('log')
    plt.show()








#Monte Carlo
# a = 0
# b = math.pi
# N = 1000
# arguments = []
# for x in range(N):
#     arguments.append(random.uniform(0,math.pi))
#
# values = []
# sum = 0
# for x in range(N):
#     values.append(math.sin(arguments[x]))
#     sum += math.sin(arguments[x])
#
# mean = sum/N
# print(mean*math.pi)