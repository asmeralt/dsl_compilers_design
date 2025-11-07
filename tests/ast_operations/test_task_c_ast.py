from ast_operations.task_abc import find_first_defined_function_return_type


def test_ffdfrt_1():
    code = """
def square(x: float) -> float:
    return x * x
"""
    assert find_first_defined_function_return_type(code) == "float"


def test_ffdfrt_2():
    code = """
def increment(x: int) -> int:
    return x + 1

def square(x: float) -> float:
    return x * x
"""
    assert find_first_defined_function_return_type(code) == "int"


def test_ffdfrt_3():
    code = """
def get_one():
    return 1

"""
    assert find_first_defined_function_return_type(code) == "None"


def test_ffdfrt_4():
    code = """
def add(x:float, y) -> int:
    return 1

"""
    assert find_first_defined_function_return_type(code) == "int"


def test_ffdfrt_5():
    code = """
PI = 3.1416

"""
    assert find_first_defined_function_return_type(code) is None
