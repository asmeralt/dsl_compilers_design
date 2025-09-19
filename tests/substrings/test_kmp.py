from substrings.kmp import computeLPSArray, search


def test_lsp_1():
    assert computeLPSArray("aabaaac") == [0, 1, 0, 1, 2, 2, 0]


def test_lsp_2():
    assert computeLPSArray("abcdabca") == [0, 0, 0, 0, 1, 2, 3, 1]


def test_lsp_3():
    assert computeLPSArray("abcdabcdabcd") == [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8]


def test_lsp_4():
    assert computeLPSArray("abcdabcdabcdk") == [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 0]


def test_search_1():
    pat = "dN"
    txt = "MabcdabdN"
    assert search(pat, txt) == [7]


def test_search_2():
    pat = "M"
    txt = "MabcdabdN"
    assert search(pat, txt) == [0]


def test_search_3():
    pat = "abca"
    txt = "MabcdabdN"
    assert search(pat, txt) == []


def test_search_4():
    pat = "abd"
    txt = "MabcdabdN"
    assert search(pat, txt) == [5]


def test_search_5():
    pat = "ab"
    txt = "MabcdabdN"
    assert search(pat, txt) == [1, 5]


def test_search_6():
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
