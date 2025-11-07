from ast_operations.task_abc import find_first_defined_function_name


def test_1():
    code = """
def square(x: float) -> float:
    return x * x
"""
    assert find_first_defined_function_name(code) == "square"


def test_2():
    code = """
def increment(x: int) -> int:
    return x + 1

def square(x: float) -> float:
    return x * x
"""
    assert find_first_defined_function_name(code) == "increment"


def test_3():
    code = """
PI = 3.1416
"""
    assert find_first_defined_function_name(code) == None
