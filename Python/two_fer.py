def two_fer(*args):
    if not args:
        return "One for you, one for me."

    return f"One for {args[0]}, one for me."
