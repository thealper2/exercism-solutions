def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    next_gen = [[0 for _ in range(cols)] for _ in range(rows)]

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    live_neighbors += matrix[ni][nj]

            if matrix[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    next_gen[i][j] = 1
                else:
                    next_gen[i][j] = 0

            else:
                if live_neighbors == 3:
                    next_gen[i][j] = 1
                else:
                    next_gen[i][j] = 0

    return next_gen
