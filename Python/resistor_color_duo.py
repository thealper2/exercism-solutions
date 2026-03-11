def value(colors):
    COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    return int(str(COLORS.index(colors[0])) + str(COLORS.index(colors[1])))
