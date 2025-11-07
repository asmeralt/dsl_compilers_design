import ast
from task_abc import (
    find_first_defined_function_argument_types,
    find_first_defined_function_name,
    find_first_defined_function_return_type,
)
from task_de import make_all_addition_substraction, count_number_of_BinOp


if __name__ == "__main__":
    code = """
def square(x: float) -> float:
    return x * x
"""
    func_name = find_first_defined_function_name(code)
    print(func_name)
    assert func_name == "square"

    arg_types = find_first_defined_function_argument_types(code)
    print(arg_types)
    assert arg_types == ["float"]

    ret_type = find_first_defined_function_return_type(code)
    print(ret_type)
    assert ret_type == "float"

    code = """
PI = 3.1416
"""
    func_name = find_first_defined_function_name(code)
    print(func_name)
    assert func_name == None

    code = """
def add(x, y):
    return x + y

def increment(x):
    return x + 1

print(add(1, 2))

print(increment(3))
"""

    code_ast = ast.parse(code)

    print("Orig BinOp count")
    print(count_number_of_BinOp(code_ast))

    print("Orig tree")
    exec(compile(code_ast, "<string>", "exec"))

    print("Transformed tree")
    code_ast_transformed = make_all_addition_substraction(code_ast)
    exec(compile(code_ast_transformed, "<string>", "exec"))
