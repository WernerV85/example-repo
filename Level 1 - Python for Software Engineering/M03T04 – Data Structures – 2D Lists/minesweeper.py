

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

    #for new_row, new_kolom in buur_cells:
    #    nuwe_ry, nuwe_kolom = row + new_row, kolom + new_kolom

    
    #if minesweeper_grid[nuwe_ry][nuwe_kolom] == "#":
    #            mine_count += 1
    
    
    for ro in range(buur_cells):
        row += 1
        for kol in range(buur_cells):
            if minesweeper_grid[ro][kol] == "#":
                mine_count += 1
                kolom += 1
    return mine_count


#print(mine)         
print(minesweeper_grid)
