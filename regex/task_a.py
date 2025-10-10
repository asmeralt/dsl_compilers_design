import re
from typing import Iterator


def find_number(txt: str) -> Iterator[re.Match[str]]:
    """Використовуючи регулярні вирази та пакет 're' виконайте наступне.
    Для всіх рядків вхідного тексту знайдіть останнє число в рядку

    Приклад:
        | 10 + 10 = 20
        | У нас було 5 діжок меду та 13 кілограм мʼяса.
        | 3.14*4524=1.420536e4
    Результат:
        | 20
        | 13
        | 1.420536e4
    Args:
        txt (str): Відний текст

    Returns:
        Iterator[re.Match[str]]: Перелік збігів
    """
    raise NotImplementedError("Not implemented")
