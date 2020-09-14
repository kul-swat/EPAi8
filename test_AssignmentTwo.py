import pytest
import AssignmentTwo

fibonacci_function = AssignmentTwo.fibonacci()
def test_fibonacci1():
    fibonacci_number1 = fibonacci_function()
    assert fibonacci_number1 == 0

def test_fibonacci2():
    fibonacci_number2 = fibonacci_function()
    assert fibonacci_number2 == 1

def test_fibonacci3():
    fibonacci_number3 = fibonacci_function()
    assert fibonacci_number3 == 1
