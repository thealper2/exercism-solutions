def commands(binary_str):
    handshake = ["wink", "double blink", "close your eyes", "jump"]
    n = int(binary_str, 2) & 0b11111
    if n == 0:
        return []

    result = []
    for i in range(4):
        if n & (1 << i):
            result.append(handshake[i])

    if n & 0b10000:
        result.reverse()

    return result
