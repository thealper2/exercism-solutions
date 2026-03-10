def is_pangram(sentence):
    sentence = sentence.lower()
    letters = set()
    for c in sentence:
        if c.isalpha():
            letters.add(c)

    return len(letters) == 26
