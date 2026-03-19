def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def gamestate(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if not (x_count == o_count or x_count == o_count + 1):
        if x_count > o_count + 1:
            raise ValueError("Wrong turn order: X went twice")

        elif o_count > x_count:
            raise ValueError("Wrong turn order: O started")

    x_wins = check_winner(board, 'X')
    o_wins = check_winner(board, 'O')

    if x_wins and x_count != o_count + 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if o_wins and x_count != o_count:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_wins and o_wins:
        raise ValueError("Impossible board: both player can't win")

    if x_wins or o_wins:
        return "win"
    elif x_count + o_count == 9:
        return "draw"
    else:
        return "ongoing"
