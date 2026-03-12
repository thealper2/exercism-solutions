def find(search_list, value):
    n = len(search_list)
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2
        if value < search_list[mid]:
            r = mid - 1
        elif value > search_list[mid]:
            l = mid + 1
        else:
            return mid

    raise ValueError("value not in array")
    
