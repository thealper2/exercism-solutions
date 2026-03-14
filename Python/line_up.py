def line_up(name, number):
    s_number = str(number)
    if s_number.endswith("1") and not s_number.endswith("11"):
        w = "st"
    elif s_number.endswith("2") and not s_number.endswith("12"):
        w = "nd"
    elif s_number.endswith("3") and not s_number.endswith("13"):
        w = "rd"
    else:
        w = "th"

    text = f"{name}, you are the {s_number + w} customer we serve today. Thank you!"
    return text
        
