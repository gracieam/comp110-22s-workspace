


def indices_word(word: str, char: str) -> str:
    """"""
    index: str = ""
    i: int = 0
    while i < len(word):
        if char == word[i]:
            index += word[i]
    i += 1
    return index
