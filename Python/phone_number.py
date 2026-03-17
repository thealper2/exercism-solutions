class PhoneNumber:
    def __init__(self, number):
        self.number = self._validate_and_clean(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

    def _validate_and_clean(self, number):
        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")

        digits = []
        for char in number:
            if char.isdigit():
                digits.append(char)
            elif char in ' ()-.+':
                continue
            else:
                raise ValueError("punctuations not permitted")

        digits_str = "".join(digits)

        if len(digits_str) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits_str) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(digits_str) == 11:
            if digits_str[0] != "1":
                raise ValueError("11 digits must start with 1")

            digits_str = digits_str[1:]

        if digits_str[0] == "0":
            raise ValueError("area code cannot start with zero")

        if digits_str[0] == "1":
            raise ValueError("area code cannot start with one")

        if digits_str[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        if digits_str[3] == "1":
            raise ValueError("exchange code cannot start with one")

        return digits_str

    def pretty(self):
        if len(self.number) == 11:
            return f"({self.number[1:4]})-{self.number[4:7]}-{self.number[7:]}"
        else:
            return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
