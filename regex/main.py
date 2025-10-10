from task_a import find_number
from task_b import merge_white_spaces
from task_c import extract_email_domains
from task_d import trim_each_line


def run_task_a():
    txt = """10 + 10 = 20\nУ нас було 5 діжок меду та 13 кілограм мʼяса.\n3.14*4524=1.420536e4"""
    txt_true = ["20", "13", "1.420536e4"]
    txt_answer_iter = find_number(txt)

    for txt_true_match, txt_answer_match in zip(txt_true, txt_answer_iter):
        print(txt_true_match, txt_answer_match.group(1))
        assert txt_true_match == txt_answer_match.group(1)


def run_task_b():
    txt = """Встала  весна, \tчорну   землю
Сонну \t\t розбудила,
Уквітчала \t її рястом,
Барвінком  укрила;
І    на    полі    жайворонок,
Соловейко    \t\t\t \t\t\t в \t \t \t \t гаї
Землю,    убрану  \t\t \t\t весною,
Вранці \t зустрічають…"""

    txt_true = """Встала весна, чорну землю
Сонну розбудила,
Уквітчала її рястом,
Барвінком укрила;
І на полі жайворонок,
Соловейко в гаї
Землю, убрану весною,
Вранці зустрічають…"""

    txt_answer, n = merge_white_spaces(txt)
    print(n)
    print(txt_answer)
    assert txt_true == txt_answer
    assert n == 15


def run_task_c():
    txt = """White Wizard: gandalf@middle.earth.com
Lord roboute.guilliman@w40k.com vs Master frodo.baggings@middle.earth.com
sauron@mordor.ru is enemy
Mister neo.anderson@matrix.eu we greet you"""

    txt_true = [
        ("gandalf@middle.earth.com", "middle.earth.com", "middle"),
        ("roboute.guilliman@w40k.com", "w40k.com", "w40k"),
        ("sauron@mordor.ru", "mordor.ru", "mordor"),
        ("neo.anderson@matrix.eu", "matrix.eu", "matrix"),
    ]
    txt_answer = extract_email_domains(txt)

    for txt_true_match, txt_answer_match in zip(txt_true, txt_answer):
        for i in range(3):
            print(txt_true_match[i], txt_answer_match.group(i + 1))
            assert txt_true_match[i] == txt_answer_match.group(i + 1)


def run_task_d():
    txt = """ \t На зеленому горбочку, \t 
 У вишневому садочку,\t
 Притулилася хатинка,
 \t Мов маленькая дитинка   \t """
    txt_true = """На зеленому горбочку,
У вишневому садочку,
Притулилася хатинка,
Мов маленькая дитинка"""

    txt_answer = trim_each_line(txt)
    print(txt_answer)
    assert txt_true == txt_answer


if __name__ == "__main__":

    run_task_a()
    print("-" * 50)

    run_task_b()
    print("-" * 50)

    run_task_c()
    print("-" * 50)

    run_task_d()
    print("-" * 50)
