def rows(letter):
    n = ord(letter) - ord("A")
    start_ascii = ord("A")
    top = []
    for i in range(n + 1):
        outer = " " * (n - i)
        current_letter = chr(start_ascii + i)
        if i == 0:
            top.append(outer + "A" + outer)
        else:
            inner = " " * (2 * i - 1)
            top.append(outer + current_letter + inner + current_letter + outer)
    
    return top + top[-2::-1]
