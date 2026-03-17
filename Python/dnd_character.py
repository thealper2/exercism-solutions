import random

def modifier(value):
    return (value - 10) // 2

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.constitution_modifier = modifier(self.constitution)
        self.hitpoints = 10 + self.constitution_modifier

    def ability(self):
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort()
        return sum(rolls[1:]) 
