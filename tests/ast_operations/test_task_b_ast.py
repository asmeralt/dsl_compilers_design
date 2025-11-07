from ast_operations.task_abc import find_first_defined_function_argument_types


def test_1():
    code = """
def square(x: float) -> float:
    return x * x
"""
    assert find_first_defined_function_argument_types(code) == ["float"]


def test_2():
    code = """
def increment(x: int) -> int:
    return x + 1

def square(x: float) -> float:
    return x * x
"""
    assert find_first_defined_function_argument_types(code) == ["int"]


def test_3():
    code = """
def get_one() -> int:
    return 1

"""
    assert find_first_defined_function_argument_types(code) == []


def test_4():
    code = """
def add(x:float, y) -> int:
    return 1

"""
    assert find_first_defined_function_argument_types(code) == ["float", "None"]


def test_5():
    code = """
PI = 3.1416

"""
    assert find_first_defined_function_argument_types(code) is None
