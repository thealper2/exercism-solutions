def abbreviate(words):
    phrase = words.replace('-', ' ')
    phrase = phrase.replace('_', ' ')
    return "".join(word[0].upper() for word in phrase.split())
