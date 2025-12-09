"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture

def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(calc):
        """Test multiplying positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(calc):
        """Test dividing positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

class TestaddInvalidInput:
    """Tests for invalid inputs in add method."""

    def test_add_invalid_input_raises_exception(calc):
        """Test that invalid inputs raise InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10000000  # Invalid input
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(a, b)
        assert "Input value out of valid range" in str(excinfo.value)

class TestSubtractInvalidInput:
    """Tests for invalid inputs in subtract method."""

    def test_subtract_invalid_input_raises_exception(calc):
        """Test that invalid inputs raise InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = -10000000  # Invalid input
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.subtract(a, b)
        assert "Input value out of valid range" in str(excinfo.value)

class TestMultiplyInvalidInput:
    """Tests for invalid inputs in multiply method."""

    def test_multiply_invalid_input_raises_exception(calc):
        """Test that invalid inputs raise InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 5000000  # Invalid input
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.multiply(a, b)
        assert "Input value out of valid range" in str(excinfo.value)

class TestDivideInvalidInput:
    """Tests for invalid inputs in divide method."""

    def test_divide_invalid_input_raises_exception(calc):
        """Test that invalid inputs raise InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -2000000  # Invalid input

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.divide(a, b)
        assert "Input value out of valid range" in str(excinfo.value)

class TestDivideByZero:
    """Tests for division by zero in divide method."""

    def test_divide_by_zero_raises_exception(calc):
        """Test that dividing by zero raises ValueError."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            calc.divide(a, b)
        assert "Cannot divide by zero" in str(excinfo.value)

class test_maximum_minimum_InputValues:
    """Tests for maximum input values."""

    def test_add_maximum_input_values(calc):
        """Test adding maximum input values."""
        # Arrange
        calc = Calculator()
        a = 1000000
        b = 1
        expected = 10000001

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected
    
    def test_add_minimum_input_values(calc):
        """Test adding minimum input values."""
        # Arrange
        calc = Calculator()
        a = -1000000
        b = -1
        expected = -1000001

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected
    
    def test_subtract_maximum_input_values(calc):
        """Test subtracting maximum input values."""
        # Arrange
        calc = Calculator()
        a = 1000000
        b = -1
        expected = 1000001

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_minimum_input_values(calc):
        """Test subtracting minimum input values."""
        # Arrange
        calc = Calculator()
        a = -1000000
        b = 1
        expected = -1000001

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_maximum_input_values(calc):
        """Test multiplying maximum input values."""
        # Arrange
        calc = Calculator()
        a = 1000000
        b = 1000
        expected = 1000000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_minimum_input_values(calc):
        """Test multiplying minimum input values."""
        # Arrange
        calc = Calculator()
        a = -1000000
        b = 1000
        expected = -1000000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
    
    def test_divide_maximum_input_values(calc):
        """Test dividing maximum input values."""
        # Arrange
        calc = Calculator()
        a = 1000000
        b = 2
        expected = 500000

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected
    
    def test_divide_minimum_input_values(calc):
        """Test dividing minimum input values."""
        # Arrange
        calc = Calculator()
        a = -1000000
        b = 2
        expected = -500000

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

class test_exception_messages:
    """Tests for exception messages."""

    def test_invalid_input_exception_message(calc):
        """Test the message of InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 2000000  # Invalid input
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(a, b)
        assert str(excinfo.value) == "Input value out of valid range (-1,000,000 to 1,000,000)"

    def test_divide_by_zero_exception_message(calc):
        """Test the message of ValueError when dividing by zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(ValueError) as excinfo:
            calc.divide(a, b)
        assert str(excinfo.value) == "Cannot divide by zero"

class test_only_b_is_invalid:
    """Tests where only the second input is invalid."""

    def test_add_only_b_invalid(calc):
        """Test adding where only b is invalid."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 2000000  # Invalid input

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(a, b)
        assert "Input value out of valid range" in str(excinfo.value)

    def test_subtract_only_b_invalid(calc):
        """Test subtracting where only b is invalid."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -2000000  # Invalid input

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.subtract(a, b)
        assert "Input value out of valid range" in str(excinfo.value)
    
    def test_multiply_only_b_invalid(calc):
        """Test multiplying where only b is invalid."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 2000000  # Invalid input

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.multiply(a, b)
        assert "Input value out of valid range" in str(excinfo.value)
    
    def test_divide_only_b_invalid(calc):
        """Test dividing where only b is invalid."""
        # Arrange
        calc = Calculator()
        a = 2000000 # Invalid input
        b = 2  

        # Act & Assert
        with pytest.raises(InvalidInputException) as excinfo:
            calc.divide(a, b)
        assert "Input value out of valid range" in str(excinfo.value)