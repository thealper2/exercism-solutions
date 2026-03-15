def encode(plain_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[::-1]
    trans = str.maketrans(plain, cipher)
    result = []
    for char in plain_text.lower():
        if char.isalpha():
            result.append(char.translate(trans))
        elif char.isdigit():
            result.append(char)
    
    encoded = ''.join(result)
    return ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))

def decode(ciphered_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[::-1]
    trans = str.maketrans(cipher, plain)
    text = ciphered_text.replace(' ', '')
    result = []
    for char in text:
        if char.isalpha():
            result.append(char.translate(trans))
        elif char.isdigit():
            result.append(char)
    
    return ''.join(result)
