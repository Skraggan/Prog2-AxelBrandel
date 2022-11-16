n = 5
order = []
colors = []

final_grid = [["V","V","V","V","V"],
              [".",".","S",".","S"],
              ["V","V","V","V","S"],
              ["V","V","V","V","V"],
              [".",".","S",".","S"]]

current_grid = [[".",".",".",".","."],
                [".",".",".",".","."],
                [".",".",".",".","."],
                [".",".",".",".","."],
                [".",".",".",".","."]]

while final_grid != current_grid:
    for r in range(n):
        color = ""
        for c in range(n):
            if c != n-1:
                if current_grid[r][c] != ".":
                    continue
                else:
                    current_color = final_grid[r][c]
                    if color == "":
                        color = current_color
                    if current_color == color:
                        continue
                    else:
                        color = ""
                        break
            else:
                if final_grid[r][c] == color or current_grid[r][c] != ".":
                    order.insert(0, r+1)
                    colors.insert(0, color)
                    for i in range(n):
                        if current_grid[r][i] == ".":
                            current_grid[r][i] = color
                    color = ""

    for c in range(n):
        color = ""
        for r in range(n):
            if r != n-1:
                if current_grid[r][c] != ".":
                    continue
                else:
                    current_color = final_grid[r][c]
                    if color == "":
                        color = current_color
                    if current_color == color:
                        continue
                    else:
                        color = ""
                        break
            else:
                if final_grid[r][c] == color or current_grid[r][c] != ".":
                    col = "ABCDEFGHI"[c]
                    order.insert(0, col)
                    colors.insert(0, color)
                    for i in range(n):
                        if current_grid[i][c] == ".":
                            current_grid[i][c] = color
                    color = ""

final_order = []
final_colors = []

for i in range(len(colors)):
    if colors[i] == "S" or colors[i] == "V":
        final_order.append(order[i])
        final_colors.append(colors[i])

print(final_grid)
print(current_grid)   
print(final_order, final_colors)



