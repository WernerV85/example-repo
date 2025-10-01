

minesweeper_grid = [["-" , "#", "-", "-", "#"],
                    ["#" , "#", "-", "-", "#"],
                    ["-" , "-", "#", "#", "-"],
                    ["#" , "-", "-", "-", "-"],
                    ["-" , "-", "#", "-", "-"]]

def minesweep_solve (minesweeper_grid, row, kolom):
    row = len(minesweeper_grid)
    kolom = len(minesweeper_grid[0])
    mine_count = 0
    
    buur_cells = [(-1, -1), (-1, 0), (-1, +1),
                  (0, -1),           (0, +1),
                  (+1, -1), (+1, 0), (+1, +1)]
    
    for ro in range(row):
        for kol in range(kolom):
            if minesweeper_grid[ro][kol] == "-":
                mine_count = 0
                for new_ro, new_kol in buur_cells:
                    nnew_row , nnew_kol = ro + new_ro, kol + new_kol
                    if 0 <= nnew_row < row and 0 <= nnew_kol < kolom:
                        if minesweeper_grid[nnew_row][nnew_kol] == "#":
                            mine_count += 1
                minesweeper_grid[ro][kol] = mine_count

                print(mine_count)
    
    
minesweep_solve(minesweeper_grid, 5, 5)
for row in minesweeper_grid:
    print(row)  
# Expected output:
# [2, '#', 2, 1, '#']   
