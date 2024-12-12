from dual import Dual as pydual
import math
import matplotlib.pyplot as plt
import numpy as np

#second compute the dual number derivative and compare to the analytical derivative
def dual_function_derivative(x):
    """ 
    This method computes the given function and its derivative using dual numbers.

    f(x) = log(sin(x)) + x^2 * cos(x)

    Parameters:
    -----------
    x : float
        The input value to evalute the function and its derivative
    Returns:
    --------
    Dual
        A Dual object where the real part represents the value of the function
        at x and the dual part that represents the derivative of the function
        at x. 
    """
    x = pydual(x, 1) #define dual number with derivative seed = 1
    return x.sin().log() + x**2 * x.cos()

def f(x):
    """
    This method evaluates the function f(x).

    f(x) = log(sin(x)) + x^2 * cos(x)

    Parameters:
    -----------
    x : float
        The input value to evaluate the function. 

    Returns:
    --------
    float 
        The value of the function f(x) at the given input x.
    """
    return math.log(math.sin(x)) + x**2 * math.cos(x)

#first compute the analytical derivative
def analytical_derivative(x):
    """
    This method computes the analytical derivative at the function f(x).

    f(x) = log(sin(x)) + x^2 * cos(x)

    f'(x) = (cos(x) / sin(x)) + 2x * cos(x) - x^2 * sin(x)

    Parameters:
    -----------
    x : float
        The input value where the derivative is evaluated. 

    Returns:
    --------
    float
        The value of the derivative f'(x) at the given input x. 
    
    """
    return (math.cos(x) / math.sin(x)) + 2 * x * math.cos(x) - x**2 * math.sin(x)

#third compute the numerical derivative using an increasingly smaller step size
def numerical_derivative(x, s):
    """
    This method approximates the derivative of the function f(x) 
    by calculating the derivative by taking the difference of 
    the function values at two opints separated by a small sample size.

    Parameters:
    -----------
    x : float
        The value to approximate the derivative
    s: float
        The step size for the approximation. 
    
    Returns:
    --------
    float
        The approximate value of the derivative f'(x). 
    
    """
    return (f(x + s) - f(x - s)) / (2 * s)