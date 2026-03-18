def transpose(text):
    if not text:
        return ""

    lines = text.split("\n")
    max_len = max(len(line) for line in lines)

    result = [""] * max_len

    for row_idx, line in enumerate(lines):
        for col in range(max_len):
            if col < len(line):
                result[col] += line[col]
            else:
                if any(col < len(lines[i]) for i in range(row_idx + 1, len(lines))):
                    result[col] += " "

    return "\n".join(result)
