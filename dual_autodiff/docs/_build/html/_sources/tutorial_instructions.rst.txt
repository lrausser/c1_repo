Tutorial
--------

The **Dual_Autodiff Package** is a python package that performs automatic differentiation using dual numbers. 
This approach to compute derivatives with dual numbers is known as forward-mode automatic differentiation. 
Automatic differentiation is at the core of learning algorithms for deep neural networks. The forward mode is 
efficient for functions with relatively few input variables but many output variables, like a deep neural 
network with a few nodes in the input layer and many nodes in the output layer. 

Formally, dual numbers are like complex numbers, but instead of a real and imaginary part, they have a real part and a dual. In the same way the 
complex part of complex numbers is carried by i, the dual part of dual numbers is carried by epsilon. The major 
difference with complex numbers is that instead of the imaginary unit :math:`i^2 = -1`, we have :math:`\epsilon^2 = 0`. 

Consider the dual number :math:`x = a + b\epsilon`. Then, :math:`x^2 = (a + b\epsilon)^2 = a^2 + 2ab\epsilon`. Note that the derivative of :math:`x^2` 
with respect to :math:`x` is :math:`2ax` , thus, with :math:`b = 1` , the dual part of :math:`x^2` , i.e., :math:`2ab\epsilon`, is the derivative of :math:`x^2` 
with respect to :math:`x` evaluated at :math:`x = a`. In fact, you can show that any function :math:`f(x)` can be extended to dual numbers and that its dual part is its derivative. 
You have: :math:`f(a + b\epsilon) = f(a) + f'(a)b\epsilon`.

Features
--------

- **Dual class**: Core attributes and methods, including math functions that compute automatic differentiation using dual numbers.

.. autoclass:: dual_autodiff.Dual
    :members:
    :special-members: __init__, __str__, __add__, __sub__, __mul__, __truediv__

Installation
------------

Ensure you have Python 3.6 or higher. Install the package and its dependencies with:

.. code-block:: bash

    pip install -e . 

Usage
-----

Here's a quick example of how to use the package: 

.. code-block:: python 

    from dual_autodiff.dual import Dual

    dual_test1 = Dual(2, 2)
    dual_test2 = Dual(1, 2)
    result = dual_test1 + dual_test2
    print(result)


Contributing
------------

Contributions are welcome! Fork our repository and submit a pull request.

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.

.. API Reference
.. ---------------------------------------------------------------------
.. .. include:: dual_autodiff.rst



.. include:: ../dual_autodiff.rst 

