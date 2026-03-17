def count_words(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(",", " ")
    sentence = sentence.replace("_", " ")
    sentence = sentence.replace("\n", " ")
    words = sentence.split()
    freq = {}
    for word in words:
        while not word[0].isalpha() and not word[-1].isdigit():
            word = word[1:]
        
        while not word[-1].isalpha() and not word[-1].isdigit():
            word = word[:-1]

        freq[word] = freq.get(word, 0) + 1

    return freq
