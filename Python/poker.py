lush = len(set(suits)) == 1
    value_counts = Counter(values)
    counts = sorted(value_counts.values(), reverse=True)
    unique_values = sorted(value_counts.keys(), reverse=True)
    
    if is_straight and is_flush:
        rank = 8
        tie_breaker = [values[0]]
    
    elif counts == [4, 1]:
        rank = 7
        four_value = [v for v, c in value_counts.items() if c == 4][0]
        kicker = [v for v, c in value_counts.items() if c == 1][0]
        tie_breaker = [four_value, kicker]
    
    elif counts == [3, 2]:
        rank = 6
        three_value = [v for v, c in value_counts.items() if c == 3][0]
        two_value = [v for v, c in value_counts.items() if c == 2][0]
        tie_breaker = [three_value, two_value]
    
    elif is_flush:
     from collections import Counter


def rank_hand(hand):
    cards = hand.split()
    values = []
    suits = []
    
    for card in cards:
        value = card[:-1]
        suit = card[-1]
        
        if value == 'J':
            value = 11
        elif value == 'Q':
            value = 12
        elif value == 'K':
            value = 13
        elif value == 'A':
            value = 14
        else:
            value = int(value)
        
        values.append(value)
        suits.append(suit)
    
    values.sort(reverse=True)
    
    is_straight = False
    if values == [14, 5, 4, 3, 2]:
        is_straight = True
        values = [5, 4, 3, 2, 1]
    else:
        is_straight = all(values[i] - 1 == values[i+1] for i in range(4))
    
    is_f   rank = 5
        tie_breaker = values
    
    elif is_straight:
        rank = 4
        tie_breaker = [values[0]]
    
    elif counts == [3, 1, 1]:
        rank = 3
        three_value = [v for v, c in value_counts.items() if c == 3][0]
        kickers = sorted([v for v, c in value_counts.items() if c == 1], reverse=True)
        tie_breaker = [three_value] + kickers
    
    elif counts == [2, 2, 1]:
        rank = 2
        pairs = sorted([v for v, c in value_counts.items() if c == 2], reverse=True)
        kicker = [v for v, c in value_counts.items() if c == 1][0]
        tie_breaker = pairs + [kicker]
    
    elif counts == [2, 1, 1, 1]:
        rank = 1
        pair_value = [v for v, c in value_counts.items() if c == 2][0]
        kickers = sorted([v for v, c in value_counts.items() if c == 1], reverse=True)
        tie_breaker = [pair_value] + kickers
    
    else:
        rank = 0
        tie_breaker = values
    
    return (rank, tie_breaker)

def best_hands(hands):
    ranked_hands = [(hand, rank_hand(hand)) for hand in hands]
    best_rank = max(rank for _, rank in ranked_hands)
    return [hand for hand, rank in ranked_hands if rank == best_rank]
