class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(d) for d in row.split()] for row in matrix_string.split("\n")]
        self.n = len(self.matrix)
        self.m = len(self.matrix[0]) if self.n > 0 else 0
    
    def row(self, index):
        if index > self.n:
            return self.matrix[-1]
        
        return self.matrix[index - 1]

    def column(self, index):
        if index > self.m:
            return [self.matrix[i][-1] for i in range(self.n)]
            
        return [self.matrix[i][index - 1] for i in range(self.n)]
