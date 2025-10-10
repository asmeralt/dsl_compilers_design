import pytest
from regex.task_a import find_number


def test_1():
    txt = "124"
    txt_true = "124"

    txt_answer = find_number(txt)

    assert txt_true == next(txt_answer).group(1)


def test_2():
    txt = "1234 124"
    txt_true = "124"

    txt_answer = find_number(txt)

    assert txt_true == next(txt_answer).group(1)


def test_3():
    txt = "word 1234 word 124 word"
    txt_true = "124"

    txt_answer = find_number(txt)

    assert txt_true == next(txt_answer).group(1)


def test_4():
    txt = "word 1234 word 2025-10-10 word"
    txt_true = "-10"

    txt_answer = find_number(txt)

    assert txt_true == next(txt_answer).group(1)


def test_5():
    txt = "124\n1234 124\nword 1234 word 124 word\nword 1234 word 2025-10-10 word"
    txt_true_list = ["124", "124", "124", "-10"]

    txt_answer_iter = find_number(txt)

    for txt_true, txt_answer in zip(txt_true_list, txt_answer_iter):
        assert txt_true == txt_answer.group(1)


def test_6():
    txt = """10 + 10 = 20\nУ нас було 5 діжок меду та 13 кілограм мʼяса.\n3.14*4524=1.420536e4"""
    txt_true = ["20", "13", "1.420536e4"]
    txt_answer_iter = find_number(txt)

    for txt_true_match, txt_answer_match in zip(txt_true, txt_answer_iter):
        assert txt_true_match == txt_answer_match.group(1)


def test_7():
    txt = """3.14*4524=1.420536E-4\n3.14*4524=1.420536E4\n3.14*4524=1.420536e-4"""
    txt_true = ["1.420536E-4", "1.420536E4", "1.420536e-4"]
    txt_answer_iter = find_number(txt)

    for txt_true_match, txt_answer_match in zip(txt_true, txt_answer_iter):
        assert txt_true_match == txt_answer_match.group(1)
