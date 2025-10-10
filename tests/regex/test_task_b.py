from regex.task_b import merge_white_spaces


def test_1():
    txt = "І    на    полі     жайворонок,"
    txt_true = "І на полі жайворонок,"

    txt_answer, n = merge_white_spaces(txt)

    assert n == 3
    assert txt_true == txt_answer


def test_2():
    txt = "І    на    полі    жайворонок,"
    txt_true = "І на полі жайворонок,"

    txt_answer, n = merge_white_spaces(txt)

    assert n == 3
    assert txt_true == txt_answer


def test_3():
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

    assert n == 15
    assert txt_true == txt_answer
