

def check_viable(letters: list[str], result: list[str], word: str):
    if word in result:
        return False

    viable = True
    for c in word:
        if c not in letters:
            viable = False

    return viable


letters = ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]

result = []

print(check_viable(letters=letters, result=result, word="lksdj"))
print(check_viable(letters=letters, result=result, word="uiopt"))


