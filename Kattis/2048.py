grid = []
for i in range(4):
    line = input().split(" ")
    for i in range(4):
        line[i] = int(line[i])
    grid.append(line)
direction = int(input())

print("----------------------")

def checkDirection(direction):
    if direction in [0,1,2,3]:
        if direction == 0:
            return ["row", [0,4,1], [0,4,1]]

pattern = checkDirection(direction)

if pattern[0] == "row":
    for row in range(pattern[2][0], pattern[2][1]):
        for col in range(pattern[1][0]+pattern[1][2], pattern[1][1]):
            current = grid[row][col]
            for i in range(col-pattern[1][2], pattern[1][0]-pattern[1][2], -pattern[1][2]):
                print(grid[row][i])
            print("--new col--")

elif pattern[0] == "col":
    for col in range(4):
        for row in range(4):
            pass

    


# print(grid, pattern)
