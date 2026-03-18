ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"
YACHT = "yacht"


def score(dice, category):
    dice = sorted(dice)
    numbers = {
        "ones": 1,
        "twos": 2,
        "threes": 3,
        "fours": 4,
        "fives": 5,
        "sixes": 6,
    }
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        number = int(numbers[category])
        return dice.count(number) * number

    if category == CHOICE:
        return sum(dice)

    if category == YACHT:
        if all(d == dice[0] for d in dice):
            return 50

        return 0

    if category == FULL_HOUSE:
        counts = {}
        for d in dice:
            counts[d] = counts.get(d, 0) + 1

        if len(counts) == 2 and 3 in counts.values() and 2 in counts.values():
            return sum(dice)

        return 0

    if category == FOUR_OF_A_KIND:
        counts = {}
        for d in dice:
            counts[d] = counts.get(d, 0) + 1

        for value, count in counts.items():
            if count >= 4:
                return value * 4

        return 0

    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30

        return 0

    if category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30

        return 0

    return 0
