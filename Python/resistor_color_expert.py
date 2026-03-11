COLOR_VALUES = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
}

TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"
}


def format_value(value):
    if value >= 1_000_000:
        v = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        v = value / 1_000
        unit = "kiloohms"
    else:
        v = value
        unit = "ohms"

    v_str = f"{v:.2f}".rstrip("0").rstrip(".")
    return v_str, unit


def resistor_label(colors):

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        d1 = COLOR_VALUES[colors[0]]
        d2 = COLOR_VALUES[colors[1]]
        multiplier = 10 ** COLOR_VALUES[colors[2]]
        tolerance = TOLERANCE[colors[3]]

        value = (d1 * 10 + d2) * multiplier

    elif len(colors) == 5:
        d1 = COLOR_VALUES[colors[0]]
        d2 = COLOR_VALUES[colors[1]]
        d3 = COLOR_VALUES[colors[2]]
        multiplier = 10 ** COLOR_VALUES[colors[3]]
        tolerance = TOLERANCE[colors[4]]

        value = (d1 * 100 + d2 * 10 + d3) * multiplier

    v_str, unit = format_value(value)

    return f"{v_str} {unit} ±{tolerance}"
