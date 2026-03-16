def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    scales = ["", "thousand", "million", "billion"]
    
    groups = []
    n = number
    while n > 0:
        groups.append(n % 1000)
        n //= 1000
    
    result_parts = []
    for i in range(len(groups) - 1, -1, -1):
        group_value = groups[i]
        if group_value > 0:
            group_text = say_num_999(group_value)
            if i > 0:
                group_text += " " + scales[i]
            result_parts.append(group_text)
    
    return " ".join(result_parts)


def say_num_999(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", 
            "sixty", "seventy", "eighty", "ninety"]

    if number == 0:
        return ""
    
    if 10 <= number <= 19:
        return teens[number - 10]
    
    parts = []
    
    hundreds = number // 100
    remainder = number % 100
    
    if hundreds > 0:
        parts.append(ones[hundreds] + " hundred")
    
    if remainder > 0:
        if remainder < 10:
            parts.append(ones[remainder])
        elif remainder < 20:
            parts.append(teens[remainder - 10])
        else:
            ten = remainder // 10
            one = remainder % 10
            if one == 0:
                parts.append(tens[ten])
            else:
                parts.append(f"{tens[ten]}-{ones[one]}")
    
    return " ".join(parts)
