def translate(text):
    result = []
    for word in text.split():
        vowels = ["a", "e", "i", "o", "u"]
        if word[0] in vowels or word[:2] in ["xr", "yt"]:
            new_word = word + "ay"
            
        elif word[0] not in vowels and word[1:3] == "qu":
            new_word = word[3:] + word[0] + "quay"
        
        elif word[:2] == "qu":
            new_word = word[2:] + "quay"

        else:
            for i in range(len(word)):
                if word[i] in vowels or (i > 0 and word[i] == "y"):
                    new_word = word[i:] + word[:i] + "ay"
                    break

        result.append(new_word)
    
    return " ".join(result)
