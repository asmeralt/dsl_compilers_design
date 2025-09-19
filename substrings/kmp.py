from typing import List


def computeLPSArray(pat: str) -> List[int]:
    """Computer longest prefix suffix array

    Args:
        pat (str): pattern to process

    Returns:
        List[int]: Longest prefix suffix array
    """
    raise NotImplementedError("ComputeLPSArray method is not implemented yet")


def search(pat: str, txt: str) -> List[int]:
    """Knuth-Morris-Pratt (KMP) algorithm substring search

    Args:
        pat (str): pattern to search for
        txt (str): text to search in

    Returns:
        List[int]: list of position of all matches
    """
    raise NotImplementedError("Search method is not implemented yet")


if __name__ == "__main__":

    _ = computeLPSArray("aabaaac")
    _ = computeLPSArray("abcdabca")
    _ = computeLPSArray("abcdabcdabcdk")

    txt = "ababababa"
    pat = "abab"

    lps = computeLPSArray(pat)
    print(lps)

    res = search(pat, txt)
    print(*res)
