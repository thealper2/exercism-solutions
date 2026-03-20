def convert(input_grid):
    if not input_grid:
        return ""
    
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    if not all(len(row) % 3 == 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    
    if not all(len(row) == len(input_grid[0]) for row in input_grid):
        raise ValueError("Input grid has inconsistent row lengths")
    
    digits = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9"
    }
    
    num_rows = len(input_grid) // 4
    result_rows = []
    
    for row_group in range(num_rows):
        start_row = row_group * 4
        cell_rows = input_grid[start_row:start_row + 4]
        
        num_cols = len(cell_rows[0]) // 3
        
        result = []
        
        for col in range(num_cols):
            start_col = col * 3
            
            cell = ""
            for row in range(4):
                cell += cell_rows[row][start_col:start_col + 3]
            
            if cell in digits:
                result.append(digits[cell])
            else:
                result.append("?")
        
        result_rows.append("".join(result))
    
    return ",".join(result_rows)
