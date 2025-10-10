from regex.task_c import extract_email_domains


def test_1():
    txt = "myemailbox@example.com"
    txt_true = [("myemailbox@example.com", "example.com", "example")]

    txt_answer = extract_email_domains(txt)

    for txt_true_match, txt_answer_match in zip(txt_true, txt_answer):
        for i in range(3):
            assert txt_true_match[i] == txt_answer_match.group(i + 1)


def test_2():
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
            assert txt_true_match[i] == txt_answer_match.group(i + 1)
