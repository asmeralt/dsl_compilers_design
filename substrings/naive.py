from typing import List


def search(pat: str, txt: str) -> List[int]:
    """Naive implementation of substring search

    Args:
        pat (str): pattern to search for
        txt (str): text to search in

    Returns:
        List[int]: list of position of all matches
    """
    raise NotImplementedError("Search method is not implemented yet")


if __name__ == "__main__":
    txt = "ababababa"
    pat = "abab"

    res = search(pat, txt)
    print(*res)
