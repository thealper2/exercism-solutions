def answer(question: str) -> int:
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    expr = question[8:-1].strip()
    if not expr:
        raise ValueError("syntax error")

    expr = expr.replace("multiplied by", "multiplied_by")
    expr = expr.replace("divided by", "divided_by")

    tokens = expr.split()

    def is_number(x):
        try:
            int(x)
            return True
        except:
            return False

    ops = {"plus", "minus", "multiplied_by", "divided_by"}

    if not is_number(tokens[0]):
        raise ValueError("syntax error")

    result = int(tokens[0])
    i = 1

    while i < len(tokens):
        try:
            op = tokens[i]
            if op not in ops:
                if not op.isdigit():
                    raise ValueError("unknown operation")

            if i + 1 >= len(tokens) or not is_number(tokens[i + 1]):
                raise ValueError("syntax error")

            num = int(tokens[i + 1])

            if op == "plus":
                result += num
            elif op == "minus":
                result -= num
            elif op == "multiplied_by":
                result *= num
            elif op == "divided_by":
                result //= num

            i += 2

        except ValueError as e:
            raise e
        except:
            raise ValueError("syntax error")

    return result
