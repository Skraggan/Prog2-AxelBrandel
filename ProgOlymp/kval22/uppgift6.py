n = 2
m = 3
grid = []
for i in range(n):
    grid.append([c for c in input(f"Rad {i+1} ? ")])

def control(grid, val_grid):
    for r in range(n):
        for c in range(m):
            count = 0
            if c != 0:
                if val_grid[r][c-1] < val_grid[r][c]: count += 1
                print("a")
            if c != m:
                if val_grid[r][c+1] < val_grid[r][c]: count += 1
                print("b")
            if r != 0:
                if val_grid[r-1][c] < val_grid[r][c]: count += 1
                print("c")
            if r != n:
                if val_grid[r+1][c] < val_grid[r][c]: count += 1
                print("d")

            if count != grid[r][c]: 
                print(r, c, count, grid[r][c])
                return False
    return True
            

for i in range(1, n*m+1):
    val_grid = [[0 for c in range(m)] for k in range(n)]
    val_grid[0][0] = i

print(control(grid, [[3,5,6], [2, 1, 4]]))
    