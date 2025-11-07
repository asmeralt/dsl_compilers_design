import ast
from ast_operations.task_de import count_number_of_BinOp


def test_1():
    code = """
def add(x, y):
    return x + y
"""
    code_ast = ast.parse(code)

    assert count_number_of_BinOp(code_ast) == 1


def test_2():
    code = """
def shift(x, y):
    return (x >> 1) + y
"""
    code_ast = ast.parse(code)

    assert count_number_of_BinOp(code_ast) == 2


def test_3():
    code = """
def increment(x):
    x += 1
    return x
"""
    code_ast = ast.parse(code)

    assert count_number_of_BinOp(code_ast) == 0
