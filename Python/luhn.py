class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num = self.card_num.replace(' ', '')
        if not card_num or not card_num.isdigit():
            return False
        
        if len(card_num) <= 1:
            return False
        
        digits = [int(d) for d in card_num]
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            digits[i] = doubled if doubled <= 9 else doubled - 9
        
        total = sum(digits)
        return total % 10 == 0
