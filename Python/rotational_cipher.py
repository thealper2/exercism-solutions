def rotate(text, key):
    encrypted = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)
    return "".join(encrypted)
