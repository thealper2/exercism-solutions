import random
import string

class Cipher:
    def __init__(self, key=None):
        self.key = key if key else ''.join(random.choices(string.ascii_lowercase, k=100))

    def encode(self, text):
        encrypted = []
        key_len = len(self.key)
        key_index = 0

        for c in text:
            if c.isalpha():
                p = ord(c.lower()) - ord('a')
                k = ord(self.key[key_index]) - ord('a')
                e_c = chr((p + k) % 26 + ord('a'))
                key_index = (key_index + 1) % key_len
                encrypted.append(e_c)
            else:
                encrypted.append(c)

        return "".join(encrypted)
        

    def decode(self, text):
        decrypted = []
        key_len = len(self.key)
        key_index = 0

        for e_c in text:
            if e_c.isalpha():
                c = ord(e_c.lower()) - ord('a')
                k = ord(self.key[key_index]) - ord('a')
                d_c = chr((c - k + 26) % 26 + ord('a'))
                key_index = (key_index + 1) % key_len
                decrypted.append(d_c)
            else:
                decrypted.append(e_c)

        return "".join(decrypted)
