def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not digits:
        return [0]
    
    for d in digits:
        if not (0 <= d < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    decimal = 0
    for d in digits:
        decimal = decimal * input_base + d
    
    if decimal == 0:
        return [0]
    
    result = []
    while decimal > 0:
        result.append(decimal % output_base)
        decimal //= output_base
    
    return result[::-1]
