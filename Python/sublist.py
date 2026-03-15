SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
        
    if len(list_one) == len(list_two):
        return UNEQUAL
    
    list_one = "  ".join(str(x) for x in list_one)
    list_two = "  ".join(str(x) for x in list_two)
    if list_one in list_two:
        return SUBLIST
    
    if list_two in list_one:
        return SUPERLIST
    
    return UNEQUAL
