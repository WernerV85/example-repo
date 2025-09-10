

minesweeper_grid = [["-" , "#", "-", "-", "#"],
                    ["#" , "#", "-", "-", "#"],
                    ["-" , "-", "#", "#", "-"],
                    ["#" , "-", "-", "-", "-"],
                    ["-" , "-", "#", "-", "-"]]

def minesweep_solve (minesweeper_grid, row, kolom):
    row = len(minesweeper_grid)
    kolom = len(minesweeper_grid[row])

    buur_cells = [(-1, -1), (-1, 0), (-1, +1),
                  (0, -1),        , (0, +1),
                  (+1, -1), (+1, 0), (+1, +1)]

    for ro in range(row):
        for kol in range(kolom):
            print(f'Board has', {row}, 'and', {kolom})