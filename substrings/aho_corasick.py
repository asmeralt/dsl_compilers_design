from typing import Dict, List, Optional


class TrieNode:
    def __init__(self, char: str):
        # Initialize TrieNode attributes
        self.char = char
        self.output: List[str] = []
        self.children: Dict[str, TrieNode] = {}
        self.fail: Optional[TrieNode] = None

    def __str__(self) -> str:
        return self.char

    def info(self) -> str:
        return f"{self.char}: {len(self.children):2d}/{len(self.output):2d}/{self.fail.char if self.fail else ''}"


def build_state_machine(words: List[str]) -> TrieNode:
    """State machine (automaton) build for Aho Korasick algorithm

    Args:
        keywords (List[str]): list of keywords to build an state machine

    Returns:
        TrieNode: Root node of state machine
    """
    raise NotImplementedError("build_automaton method is not implemented yet")


def search(words: List[str], txt: str) -> Dict[str, List[int]]:
    """Aho-Korasick (AK) algorithm substrings search

    Args:
        words (List[str]): list of words to search for
        txt (str): text to search in

    Returns:
        Dict[str, List[int]]: dict of position of all matches for each word
    """
    raise NotImplementedError("search_text method is not implemented yet")


if __name__ == "__main__":
    words = ["весна", "весло", "народ", "сир", "снасть"]
    txt = "веснарод веснасть"
    res = search(words, txt)
    print(res)

    # Example 1
    words = ["hello", "world"]
    txt = "hello worldhello"
    res = search(words, txt)
    print(res)

    # Example 2
    words = ["ab", "abc", "aby"]
    txt = "abxabcabcaby"
    res = search(words, txt)
    print(res)
