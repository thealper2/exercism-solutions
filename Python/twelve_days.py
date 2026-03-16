def recite(start_verse, end_verse):
    ORDINALS = ["", "first", "second", "third", "fourth", "fifth", "sixth",
                "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    VERSES = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, and ",
        "a Partridge in a Pear Tree."
    ]

    result = [None] * (end_verse - start_verse + 1)
    result_idx = 0
    header_template = "On the {} day of Christmas my true love gave to me: "
    for day in range(start_verse, end_verse + 1):
        header = header_template.format(ORDINALS[day])
        verses_slice = VERSES[-day:]
        rest_vers = "".join(verses_slice)
        result[result_idx] = header + rest_vers
        result_idx += 1

    return result
