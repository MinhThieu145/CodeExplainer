def cavityMap(grid):
    # chuyển thành list do string immutable
    grid = [list(x) for x in grid]
    
    # loop qua từng element 
    for i in range(1, len(grid) -1):
        
        for j in range(1,len(grid[i]) - 1):
            # check phía trước, phía sau, bên trái và bên phải, nếu tất cả đều nhỏ hơn thì đk thỏa mãn
            if grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i + 1][j] and grid[i][j] > grid[i][j- 1] and grid[i][j] > grid[i - 1][j] :
                grid[i][j] = "X"