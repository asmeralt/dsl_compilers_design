from substrings.naive import search


def test_1():
    pat = "dN"
    txt = "MabcdabdN"
    assert search(pat, txt) == [7]


def test_2():
    pat = "M"
    txt = "MabcdabdN"
    assert search(pat, txt) == [0]


def test_3():
    pat = "abca"
    txt = "MabcdabdN"
    assert search(pat, txt) == []


def test_4():
    pat = "abd"
    txt = "MabcdabdN"
    assert search(pat, txt) == [5]


def test_5():
    pat = "ab"
    txt = "MabcdabdN"
    assert search(pat, txt) == [1, 5]


def test_6():
    pat = "aa"
    txt = "MaaaaaN"
    assert search(pat, txt) == [1, 2, 3, 4]


def test_search_pat_longer_than_txt():
    pat = "aaaa"
    txt = "aaa"
    assert search(pat, txt) == []


def test_search_pat_equal_than_txt():
    pat = "abcd"
    txt = "abcd"
    assert search(pat, txt) == [0]
