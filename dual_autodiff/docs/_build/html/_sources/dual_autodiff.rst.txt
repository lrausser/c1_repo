
Dual Autodiff Tutorial 
----------------------

Import the dual autodifferentiation package:

.. code:: ipython3

    from dual_autodiff.dual import Dual as pydual
    from dual_autodiff_x.dual_autodiff_x.dual import Dual as cydual

.. code:: ipython3

    pip install memory_profiler


.. parsed-literal::

    Requirement already satisfied: memory_profiler in /Users/lilyrausser/venvs/coursework_env/lib/python3.13/site-packages (0.61.0)
    Requirement already satisfied: psutil in /Users/lilyrausser/venvs/coursework_env/lib/python3.13/site-packages (from memory_profiler) (6.1.0)
    Note: you may need to restart the kernel to use updated packages.


.. code:: ipython3

    import math
    import matplotlib.pyplot as plt
    import numpy as np
    from dual_autodiff.q.q5 import * 
    import timeit
    from timeit import Timer
    from memory_profiler import memory_usage

Here are some ways of utilizing the Dual class via simple math
operations:

.. code:: ipython3

    x = pydual(2, 3)
    y = pydual(4, 5)
    
    print("Addition of dual numbers: ",  x.__add__(y))
    print("Subtration of dual numbers: ", x.__sub__(y))
    print("Multiplication of dual numbers: ", x.__mul__(y))
    print("Division of dual numbers: ", x.__truediv__(y))


.. parsed-literal::

    Addition of dual numbers:  Dual(real = 6, dual = 8)
    Subtration of dual numbers:  Dual(real = -2, dual = -2)
    Multiplication of dual numbers:  Dual(real = 8, dual = 22)
    Division of dual numbers:  Dual(real = 0.5, dual = 0.125)


Additionally, trigonometric, logarithmic, and exponential
transformations can be efficiently performed using dual numbers.

.. code:: ipython3

    #sin example
    x = pydual(np.pi / 6, 1)
    sin_x = pydual.sin(x)
    
    print("Sin(pi / 6): ", sin_x.real)
    print("Derivative of sin(x) at pi/6: ", sin_x.dual)


.. parsed-literal::

    Sin(pi / 6):  0.49999999999999994
    Derivative of sin(x) at pi/6:  0.8660254037844387


.. code:: ipython3

    #cosine example
    x = pydual(np.pi / 3, 1)
    cos_x = pydual.cos(x)
    
    print("Cos(pi / 3): ", cos_x.real)
    print("Derivative of cos(x) at pi/3: ", cos_x.dual)


.. parsed-literal::

    Cos(pi / 3):  0.5000000000000001
    Derivative of cos(x) at pi/3:  -0.8660254037844386


.. code:: ipython3

    #tangent example
    x = pydual(np.pi / 8, 1)
    tan_x = pydual.tan(x)
    
    print("Tan(pi / 8): ", tan_x.real)
    print("Derivative of tan(x) at pi/8: ", tan_x.dual)


.. parsed-literal::

    Tan(pi / 8):  0.4142135623730951
    Derivative of tan(x) at pi/8:  1.17157287525381


.. code:: ipython3

    #exponential example
    x = pydual(0.5, 2)
    exp_x = pydual.exp(x)
    
    print("exp(0.5): ", exp_x.real)
    print("Derivative of exp(x) at 0.5: ", exp_x.dual)


.. parsed-literal::

    exp(0.5):  1.6487212707001282
    Derivative of exp(x) at 0.5:  3.2974425414002564


.. code:: ipython3

    #logarithmic example
    x = pydual(3.0, 1)
    log_x = pydual.log(x)
    
    print("lin(3): ", log_x.real)
    print("Derivative of log(x) at 3: ", log_x.dual)


.. parsed-literal::

    lin(3):  1.0986122886681098
    Derivative of log(x) at 3:  0.3333333333333333


A particularly useful example is the how chain rule can be applied using
Dual numbers:

.. code:: ipython3

    #chain rule example:
    x = pydual(1, 1)
    outcome = x * pydual.sin(pydual.exp(x))
    
    print("x * sin(exp(x)) at x = 1: ", outcome.real)
    print("Derivative of x * sin(exp(x)) at x = 1: ", outcome.dual)


.. parsed-literal::

    x * sin(exp(x)) at x = 1:  0.41078129050290885
    Derivative of x * sin(exp(x)) at x = 1:  -2.067568442452326


Dual numbers are particularly useful in optimization problems as they
simplify the computation of derivatives and help locate critical points
without requiring manual differentiation. For example, to find the
critical points of f(x) = x \* cos(x), dual numebrs can be used
iteratively:

.. code:: ipython3

    x = pydual(1, 1)
    f = x * pydual.cos(x)
    print("f(x) = x cos x: ", f.real)
    print("Derivative of f(x) at x = 0: ", f.dual)


.. parsed-literal::

    f(x) = x cos x:  0.5403023058681398
    Derivative of f(x) at x = 0:  -0.30116867893975674


In this example, f’(1) is not equal to 0, meaning x = 1 is not a
critical point. This process can be repeated iteratively, updating x
until f’(x) = 0, which identifies the critical points of the function.

This approach shows how dual numbers automate derivative computation and
streamline the search for critical points in optimization tasks.
