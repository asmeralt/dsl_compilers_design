import re
from typing import Iterator


def extract_email_domains(txt: str) -> Iterator[re.Match[str]]:
    """Використовуючи регулярні вирази та пакет 're' виконайте наступне.
    Для кожного рядка вхідного тексту знайдіть в ньому першу email адресу я першу групу захоплення.
    З email адреси виділіть домену адресу як другу групу захоплення.
    З email адреуси виділіть домен найвищого рівня як третю групу захоплення.

    Приклад:
        | White Wizard: gandalf@middle.earth.com
        | Lord roboute.guilliman@w40k.com vs Master frodo.baggings@middle.earth.com
        | sauron@mordor.ru is enemy
        | Mister neo.anderson@matrix.eu we greet you
    Результат:
        | (gandalf@middle.earth.com, middle.earth.com, middle)
        | (roboute.guilliman@w40k.com, w40k.com, w40k)
        | (sauron@mordor.ru, mordor.ru, mordor)
        | (neo.anderson@matrix.eu, matrix.eu, matrix)
    Args:
        txt (str): Відний текст

    Returns:
        Iterator[re.Match[str]]: Перелік збігів
    """
    raise NotImplementedError("Not implemented")
