def is_isogram(string):
    letters = []
    string = string.lower()
    for c in string:
        if c.isalpha():
            if c in letters:
                return False

            letters.append(c)

    return True
