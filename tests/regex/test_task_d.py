from regex.task_d import trim_each_line


def test_1():
    txt = "   Lorem ipsum dolor sit amet, \t 1\n consectetur adipiscing elit.\n \t _ Praesent eleifend.  \t "
    txt_true = "Lorem ipsum dolor sit amet, \t 1\nconsectetur adipiscing elit.\n_ Praesent eleifend."

    txt_answer = trim_each_line(txt)

    assert txt_true == txt_answer


def test_2():
    txt = """ \t На зеленому горбочку, \t 
 У вишневому садочку,\t
 Притулилася хатинка,
 \t Мов маленькая дитинка   \t """
    txt_true = """На зеленому горбочку,
У вишневому садочку,
Притулилася хатинка,
Мов маленькая дитинка"""

    txt_answer = trim_each_line(txt)

    assert txt_true == txt_answer
