class Queen:
    def __init__(self, row, column):
        self.row = self._validate_row(row)
        self.column = self._validate_column(column)

    def _validate_row(self, row):
        if row < 0:
            raise ValueError("row not positive")

        if row > 7:
            raise ValueError("row not on board")
            
        return row

    def _validate_column(self, column):
        if column < 0:
            raise ValueError("column not positive")

        if column > 7:
            raise ValueError("column not on board")

        return column
    
    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        q1x, q1y = self.row, self.column
        q2x, q2y = another_queen.row, another_queen.column

        if q1x == q2x or q1y == q2y:
            return True
        
        if abs(q1x - q2x) == abs(q1y - q2y):
            return True

        return False
