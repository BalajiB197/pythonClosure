import os
import pytest
import session8
from session8 import counter


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def my_func():
    # this is comment
    """Passing this statement to check the
    length of docstring is greater than 50 or not.
    This function is passed as argument and the free variable
    to check the length is assigned to var x
    """

def test_doc_string():
    counter_add = session8.counter(my_func)
    assert counter_add() == True

def my_func2():
    # this is comment
    """Passing this statement to check the
    """

def test_doc_string2():
    counter_add = session8.counter(my_func2)
    assert counter_add() == False

counter2 = session8.fib()
def test_fib():
    assert counter2() == 1

def test_fib2():
    assert counter2() == 1

def test_fib3():
    assert counter2() == 2

def test_fib4():
    for _ in range(3):
        counter2()
    assert counter2() == 13

def add(a, b):
    return a + b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

counter_add = session8.closure_counts(add)
counter_mul = session8.closure_counts(mul)
counter_div = session8.closure_counts(div)

def test_closure_counts():
    assert counter_mul(1,2) == {'mul': 1}

def test_closure_counts2():
    assert counter_add(1,2) == {'add': 1, 'mul': 1}

def test_closure_counts3():
    assert counter_mul(2,2) == {'add': 1, 'mul': 2}

def test_closure_counts4():
    assert counter_div(2, 2) == {'add': 1, 'div': 1, 'mul': 2}

def test_closure_counts5():
    for _ in range(3):
        counter_div(5, 2)
        counter_mul(5,2)
        counter_add(5,2)
    assert counter_div(3, 2) == {'add': 4, 'div': 5, 'mul': 5}

dict1, dict2, dict3 = {}, {}, {}
counter_dict_add = session8.closure_counts_dict(add, dict1)
counter_dict_mul = session8.closure_counts_dict(mul, dict2)
counter_dict_div = session8.closure_counts_dict(div, dict3)

def test_closure_counts_dict1():
    for _ in range(2):
        counter_dict_add(2,3)
    assert counter_dict_add(2, 2) == {'add': 3}

def test_closure_counts_dict2():
    for _ in range(4):
        counter_dict_mul(2,3)
    assert counter_dict_mul(2, 2) == {'mul': 5}

def test_closure_counts_dict3():
    for _ in range(10):
        counter_dict_div(2,3)
    assert counter_dict_div(2, 2) == {'div': 11}

