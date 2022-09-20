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
        # laid out ["row/col", columnDir, rowDir]
        if direction == 0: # left
            return ["row", [0,3,1], [0,3,1]]
        elif direction == 1: # up
            return ["col", [0,3,1], [0,3,1]]
        elif direction == 2: # right
            return ["row", [3,0,-1], [0,3,1]]
        elif direction == 3: # down
            return ["col", [0,3,1], [3,0,-1]]

def merge(number):
    return number*2

pattern = checkDirection(direction)

if pattern[0] == "row":
    for row in range(pattern[2][0], pattern[2][1]+pattern[2][2], pattern[2][2]):
        print("--new row--")
        for col in range(pattern[1][0]+pattern[1][2], pattern[1][1]+pattern[1][2], pattern[1][2]):
            print("--new col--" + str(col))
            current = grid[row][col]
            for i in range(col, pattern[1][0], -(pattern[1][2])):
                cur = grid[row][i]
                print(i)
                if cur == 0:
                    print("skip")
                    pass
                elif grid[row][i-pattern[1][2]] == 0:
                    temp = grid[row][i-pattern[1][2]]
                    grid[row][i-pattern[1][2]] = cur
                    grid[row][i] = temp
                    print("swap")
                elif grid[row][i-pattern[1][2]] == cur:
                    grid[row][i-pattern[1][2]] = merge(cur)
                    grid[row][i] = 0
                    print("merge")
                print(grid[row])         

elif pattern[0] == "col": # ["col", [0,4,1], [4,0,-1]]
    for col in range(pattern[1][0], pattern[1][1]+pattern[1][2], pattern[1][2]):
        print("--new col-- ")
        for row in range(pattern[2][0]+pattern[2][2], pattern[2][1]+pattern[2][2], pattern[2][2]):
            print("--new row-- " + str(row))
            current = grid[row][col]
            for i in range(row, pattern[2][0], -(pattern[2][2])):
                cur = grid[i][col]
                print(i)
                if cur == 0:
                    print("skip")
                    pass
                elif grid[i-pattern[2][2]][col] == 0:
                    temp = grid[i-pattern[2][2]][col]
                    grid[i-pattern[2][2]][col] = cur
                    grid[i][col] = temp
                    print("swap")
                elif grid[i-pattern[2][2]][col] == cur:
                    grid[i-pattern[2][2]][col] = merge(cur)
                    grid[i][col] = 0
                    print("merge")  

    

print("-----------------")
print(grid)
