count = input().split(" ")
whole = [1, 1, 2, 2, 2, 8]
change = ""

for i in range(6):
    change += str((whole[i]-int(count[i]))) + " "

print(change)
