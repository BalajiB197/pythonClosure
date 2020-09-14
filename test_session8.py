import os
import pytest
import session8
from session8 import *


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_doc_string():
    assert session8.outer() == True

def test_fib():
    assert session8.fibonacci(6) == [0, 1, 1, 2, 3, 5, 8, 13]
