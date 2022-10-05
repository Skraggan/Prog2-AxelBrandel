count = [int(i) for i in input().split(" ")]
change = ""

for i in range(6):
    change += str(([1, 1, 2, 2, 2, 8][i]-count[i])) + " "

print(change)
