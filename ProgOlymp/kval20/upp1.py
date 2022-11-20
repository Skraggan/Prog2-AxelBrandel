n = 432
island = 1
lost = []
curr_lost = 0
while True:
    if len(lost) < 2:
        curr_lost =+ 1 
    else:
        curr_lost = lost[island-2] + lost[island-3]

    if n - curr_lost <= 0:
        break
    else:
        lost.append(curr_lost)
        n = n - curr_lost
        island += 1

print(island)
