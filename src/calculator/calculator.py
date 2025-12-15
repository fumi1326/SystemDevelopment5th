"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""

    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    MAX_VALUE = 1000000
    MIN_VALUE = -1000000

    def Invalidinput(self, *args):
        for arg in args:
            if arg < self.MIN_VALUE or arg > self.MAX_VALUE:
                raise InvalidInputException(
                    "Input value out of valid range (-1,000,000 to 1,000,000)"
                )

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.Invalidinput(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.Invalidinput(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.Invalidinput(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self.Invalidinput(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
