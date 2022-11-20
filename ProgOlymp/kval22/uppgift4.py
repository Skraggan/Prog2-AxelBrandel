import numpy as np

n = int(input("n ? "))

final_grid = []
for i in range(n):
    final_grid.append([c for c in input(f"Rad {i+1} ? ")])

order = []
colors = []

current_grid = [["." for c in range(n)] for r in range(n)]

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
                        try:
                            if current_grid[r][i] == ".":
                                current_grid[r][i] = color
                        except IndexError:
                            print(r, i)
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

final_grid = np.array(final_grid)
current_grid = np.array(current_grid)

print(final_grid)
print(current_grid)   
print()
print(f"Order: {final_order}")
print(f"Colors: {final_colors}")