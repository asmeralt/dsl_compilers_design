import ast


def count_number_of_BinOp(code_ast: ast.Module) -> int:
    """Обчисліть кількість бінарних операцій в початковому коді.
    Бінарна операція це вузол дерева з типом ast.BinOp
    https://docs.python.org/3/library/ast.html#ast.BinOp

    Args:
        code_ast: (ast.Module): корінь абстрактного синтаксичного дерева

    Returns:
        int: кількість вузлів ast.BinOp
    """
    raise NotImplementedError("Not implemented")


def make_all_addition_substraction(code_ast: ast.Module) -> ast.Module:
    """Замініть усі бінарні операції додавання в початковому коді на віднімання.
    Бінарна операція це вузол дерева з типом ast.BinOp, та полем 'op', яке вказує не тип операції
    https://docs.python.org/3/library/ast.html#ast.BinOp


    Args:
        code_ast: (ast.Module): корінь абстрактного синтаксичного дерева

    Returns:
        ast.Module: корінь абстрактного синстаксичного дерева
    """
    raise NotImplementedError("Not implemented")
