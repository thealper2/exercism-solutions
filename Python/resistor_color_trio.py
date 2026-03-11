def label(colors):
    COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    value = (COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * (10 ** COLORS.index(colors[2]))
    if value < 1000:
        units = "ohms"
    elif value < 1000000:
        units = "kiloohms"
        value /= 1000
    elif value < 1000000000:
        units = "megaohms"
        value /= 1000000
    else:
        units = "gigaohms"
        value /= 1000000000

    return f"{int(value)} {units}"
