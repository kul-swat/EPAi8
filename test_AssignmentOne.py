import pytest
import AssignmentOne

"""def test_addition(): #test_anything 
    summation = calculator.addition(10,20)
    assert summation == 30
    assert calculator.addition("Swati","Bohidar") == "SwatiBohidar"

def test_multiplication():
    assert calculator.multiplication(10,20) == 200"""

inner = AssignmentOne.check_docstr()

def my_func():
    """This function is created to calculate the number of characters are used to the function or number of characters are used in docstring"""
    return 0

def less_num_docstr():
    """keeping a short description"""
    return 0

def null_docstr():
    return 0

def test_check_docstr_positive():
    result = inner(my_func)
    assert result == "Yes, The docstring has more than 50 Character"

def test_check_docstr_negative():
    result = inner(less_num_docstr)
    assert result == "The docstring does not have more than 50 Character"

def test_check_docstr_null():
    result = inner(null_docstr)
    assert result == "oops!! You didnot mention docstring"



