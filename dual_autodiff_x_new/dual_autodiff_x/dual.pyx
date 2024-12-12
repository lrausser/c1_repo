
import math


class Dual:
    def __init__(self, real, dual=0.0):
        """
        __init__ allows us to initialize a dual number

        Dual numbers are like complex numbers, but instead of a real 
        and imaginary part, they have a real part and a dual. In the 
        same way the complex part of complex numbers is carried by i, 
        the dual part of a dual is carried by epsilon. The major difference
        with complex numbers is that instead of the imaginary unit i^2 = -1, 
        ε^2 = 0. 

        dual = real + dual_part * ε

        Parameters: 

        real: float or int
            the real part of a dual number
        dual: float or int
            the dual part of the dual number , default to 0

        Examples:
        
        >>> d1 = Dual(5) # Dual number with real part 5 and dual part 0
        >>> d2  = Dual(5, 3) # Dual number with real part 5, dual part 3
        """

        self.real = real
        self.dual = dual


    def __add__(self, other_dual):
        """
        This add method computes the sum of the current dual
        number and another number (either dual or scalar):

        (a + bε) + (c + dε) = (a + c) + (b + d)ε

        Returns:

        Dual
            a new Dual object that is the sum of the current dual 
            and the other dual/scalar value.
        
        Examples:

        >>> d1 = Dual(2, 3)
        >>> d2 = Dual(3, 4)
        >>> d1 + d2
        Dual(real = 5, dual = 7)

        >>> d1 + 5
        Dual(real = 7, dual = 3)
        """
        return Dual(self.real + other_dual.real, self.dual + other_dual.dual)

    def __sub__(self, other_dual):
        """
        This subtract method computes the subtraction of the current
        dual number and another number (either dual or scalar):

        (a + bε) - (c + dε) = (a - c) + (b - d)ε

        Returns:

        Dual 
            A new Dual object that is the result of a subtraction 
            between the current dual and the other dual/scalar value.

        Examples:

        >>> d1 = Dual(2, 3)
        >>> d2 = Dual(3, 4)
        >>> d1 - d2 
        Dual(real = -1, Dual = -1)
        >>> d1 - 5
        Dual(real = -3, Dual = 3.0)
        """
        return Dual(self.real - other_dual.real, self.dual - other_dual.dual)

    def __mul__(self, other_dual):
        """
        This multiplication method computes the product of the
        current dual number and another number (either dual or scalar):

        (a + bε) * (c + dε) = (a * c) + (a * d + b * c)ε

        Returns:

        Dual
            A new Dual object that is the result of the multiplication
            between the current dual and the other dual/scalar value.

        Examples:

        >>> d1 = Dual(2, 3)
        >>> d2 = Dual(3, 4)
        >>> d1 * d2
        Dual(real = 6, dual = 17)
        >>> d1 * 5
        Dual(real = 10, dual = 15)
        """

        return Dual(
            self.real * other_dual.real,
            self.real * other_dual.dual + self.dual * other_dual.real,
        )

    def __truediv__(self, other_dual):
        """
        This true division method computes the remainder of the 
        current dual number and another number (either dual or scalar):

        (a + bε) / (c + dε) = (a / c) + ((b * c - a * d) / c^2)ε

        Returns:

        Dual 
            A new Dual object that is the result of dividing the current
            dual and the other dual/scalar value. 

        Examples:

        >>> d1 = Dual(2, 3)
        >>> d2 = Dual(3, 4)
        >>> d2 / d1
        Dual(real = 1.5, dual = -0.25)
        >>> d2 / 2
        Dual(real = 1.5, dual = 2.0)
        """
   
        if other_dual.real == 0:
            raise ZeroDivisionError("Division by Zero")
        return Dual(
            self.real / other_dual.real,
            (self.dual * other_dual.real - self.real * other_dual.dual)
            / (other_dual.real**2),
        )

    def __pow__(self, power):
        """
        This power method computes the result of raising the dual number
        to a specified power:

        (a + bε)^n = a^n + n * a^(n - 1) * bε

        Parameters:

        power: int, float
            The exponent where the dual value is raised.

        Returns:

        Dual
            A new Dual object as the result of raising the original dual number
            to the specified power. 

        Raises:

        ValueError
            If the power is not an integer or float
            If the real part of the dual numebr is 0 and the power is less than 0
        
        Examples:
        >>> d1 = Dual(2, 3)
        >>> d1^2
        Dual(real = 4, dual = 12)
        >>> d1^-1
        ValueError: Zero cannot be raised to a negative power
        """
        if not isinstance(power, (int, float)):
            raise ValueError("Exponent must be an integer or a float")
        if self.real == 0 and power < 0:
            raise ValueError("Zero cannot be raised to a negative power")

        real_portion = self.real**power
        dual_portion = power * (self.real ** (power - 1)) * self.dual
        return Dual(real_portion, dual_portion)

    def sin(self):
        """
        This method computes the sin of a dual number:

        sin(a + bε) = sin(a) + b * cos(a)ε

        Returns:

        Dual
            A new Dual object representing the sine of the original dual number.

        Examples:

        >>> d1 = Dual(0, 1)
        >>> d1.sin()
        Dual(real = 0.0, dual = 1.0)
        >>> d2 = Dual(0, 2)
        >>> d2.sin()
        Dual(real = 0.0, dual = 2.0)
        """
        return Dual(math.sin(self.real), math.cos(self.real) * self.dual)

    def cos(self):
        """
        This method computes the cosine of a dual number:

        cos(a + bε) = cos(a) - b * sin(a)ε

        Returns:

        Dual
            A new Dual object representing the cosine of the original dual number.
        
        Examples:

        >>> d1 = Dual(0, 1)
        >>> d1.cos()
        Dual(real = 1.0, dual = -0.0)
        >>> d2 = Dual(0, 2)
        >>> d2.cos()
        Dual(real = 1.0, dual = -0.0)
        """
        return Dual(math.cos(self.real), -math.sin(self.real) * self.dual)

    def tan(self):
        """
        This method computes the tangent of a dual number:

        tan(a + bε) = tan(a) + b / cos^2(a)ε

        Returns:
        
        Dual 
            A new Dual object represnting the tangent of the original dual number.
        
        Examples:
        
        >>> d1 = Dual(0, 1)
        >>> d1.tan()
        Dual(real = 0.0, dual = 1.0)

        >>> d2 = Dual(0, 2)
        >>> d2.tan()
        Dual(real = 0.0, dual = 2.0)
        """
        if abs(math.cos(self.real)) < 1e-8:
            raise ValueError("Tangent undefined")
        return Dual(math.tan(self.real), self.dual / (math.cos(self.real) ** 2))

    def exp(self):
        """
        This method computes the exponential of a dual number:

        exp(a + bε) = exp(a) + exp(a) * bε

        Returns:
   
        Dual
            A new Dual object representing the exponential of the original dual number.
        
        Examples:
 
        >>> d1 = Dual(0, 1)
        >>> d1.exp()
        Dual(real = 1.0, dual = 1.0)
        >>> d2 = Dual(0, 2)
        >>> d2.exp()
        Dual(real = 1.0, dual = 2.0)
        """
        return Dual(math.exp(self.real), math.exp(self.real) * self.dual)

    def log(self):
        """
        This method computes the natural logrithm of a dual number:

        log(a + bε) = log(a) + (b / a)ε

        Returns:
 
        Dual
            A new Dual object after taking the natural logrithm of the original dual number.
        
        Examples:
    
        >>> d1 = Dual(1, 1)
        >>> d1.log()
        Dual(real = 0.0, dual = 0.1)
        >>> d2 = Dual(2, 2)
        >>> d2.log()
        Dual(real = 0.693147, dual = 1.0)
        """
        if self.real <= 0:
            raise ValueError("Log undefined")
        return Dual(math.log(self.real), self.dual / self.real)

    def __repr__(self):
        """
        This method returns the string representation of a Dual object.

        Returns:
    
        str 
            A string in the format "Dual(real = {real}, dual = {dual})"
        
        Examples:

        >>> d1 = Dual(1, 1)
        >>> repr(d1)
        'Dual(real = 1, dual = 1)'  
        >>> print(d1)
        Dual(real = 1, dual = 1)
        """
        return f"Dual(real = {self.real}, dual = {self.dual})"

        