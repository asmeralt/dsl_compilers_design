from typing import List, Optional


def find_first_defined_function_name(code: str) -> Optional[str]:
    """Знаходить назву першої визначеної функції в коді, якщо вона існує

    Args:
        code (str): початковий код

    Returns:
        Optional[str]: назва першої визначеної функцї
    """
    raise NotImplementedError("Not implemented")


def find_first_defined_function_argument_types(code: str) -> Optional[List[str]]:
    """Знаходить типи аргументів першої визначеної функції в коді, якщо вона існує
    Якщо тип аргумента не визначено, то повертаємо "None"

    Args:
        code (str): початковий код

    Returns:
        Optional[str]: типи аргументів першої визначеної функцї
    """
    raise NotImplementedError("Not implemented")


def find_first_defined_function_return_type(code: str) -> Optional[str]:
    """Знаходить тип даних, що повертає перша визначена функця в коді, якщо вона існує
    Якщо тип даних не визначено, то повертаємо "None"

    Args:
        code (str): початковий код

    Returns:
        Optional[str]: тип даних, що повертає перша визначена функця
    """
    raise NotImplementedError("Not implemented")
