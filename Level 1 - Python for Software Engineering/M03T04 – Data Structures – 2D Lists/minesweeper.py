

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
        for kol in range(kol):
            if minesweeper_grid[ro][kol] == "-":
                mine_count = 0
                for new_ro in range(buur_cells):
                    for new_kol in range(buur_cells):
                        if new_ro == "#" and new_kol == "#":
                            continue
                    nnew_row , nnew_kol = ro + new_ro, kol + new_kol
                    if 0 <= nnew_row < row and 0 <= nnew_kol < kolom and minesweeper_grid[nnew_row][nnew_kol] == -1:
                        mine_count += 1
                minesweeper_grid[ro][kol] = mine_count

         
print(minesweeper_grid)
