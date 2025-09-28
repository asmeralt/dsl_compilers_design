from substrings.aho_corasick import build_state_machine, search


def test_build_state_machine_1():
    words = ["hello", "world"]
    root = build_state_machine(words)

    assert len(root.children) == 2


def test_build_state_machine_2():
    words = ["ab", "abc", "aby"]
    root = build_state_machine(words)

    assert root.children["a"].children["b"].fail == root


def test_build_state_machine_3a():
    words = ["весна", "весло", "народ", "сир", "снасть"]
    root = build_state_machine(words)

    assert len(root.children) == 3


def test_build_state_machine_3b():
    words = ["весна", "весло", "народ", "сир", "снасть"]
    root = build_state_machine(words)

    word0 = (
        root.children["в"]
        .children["е"]
        .children["с"]
        .children["н"]
        .children["а"]
        .fail.char
        == "а"
    )
    word2 = root.children["н"].children["а"].fail.char == "а"
    word4 = root.children["с"].children["н"].children["а"].fail.char == "а"

    # Only one "a" node should fail to root
    assert int(word0) + int(word2) + int(word4) == 2


def test_build_state_machine_3c():
    words = ["весна", "весло", "народ", "сир", "снасть"]
    root = build_state_machine(words)

    word0 = (
        root.children["в"].children["е"].children["с"].children["н"].fail.char == "н"
    )
    word2 = root.children["н"] == "н"
    word4 = root.children["с"].children["н"].fail.char == "н"

    # Only one "н" node should fail to root
    assert int(word0) + int(word2) + int(word4) == 2


def test_search_1():
    words = ["hello", "world"]
    txt = "hello worldhello"

    assert search(words, txt) == {"hello": [0, 11], "world": [6]}


def test_search_2():
    words = ["ab", "abc", "aby"]
    txt = "abxabcabcaby"

    assert search(words, txt) == {"ab": [0, 3, 6, 9], "abc": [3, 6], "aby": [9]}


def test_search_3():
    words = ["весна", "весло", "народ", "сир", "снасть"]
    txt = "веснарод веснасть"

    assert search(words, txt) == {
        "весна": [0, 9],
        "весло": [],
        "народ": [3],
        "сир": [],
        "снасть": [11],
    }
