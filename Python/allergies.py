class Allergies:
    ALLERGENS = [
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128),
    ]

    def __init__(self, score):
        self.score = score

        self._allergies = []
        for allergen, value in self.ALLERGENS:
            if self.score & value:
                self._allergies.append(allergen)

    def allergic_to(self, item):
        return item in self._allergies

    @property
    def lst(self):
        return self._allergies
