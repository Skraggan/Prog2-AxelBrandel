antal_påsar = int(input("Antal påsar ? "))
personer = int(input("Antal personer ? "))
påsar = []
for i in range(antal_påsar):
    påsar.append(int(input(f"Påse {i+1} räcker till ? ")))
svar = 0

while personer > 0:
    temp = 0
    ten = False
    for i in range(len(påsar)):
        if påsar[i] >= 10:
            ten = True
            personer = personer - 10
            påsar[i] = påsar[i]-10
            break
        else:
            if påsar[i] > temp:
                temp = påsar[i]
    if ten == False:
        påsar[påsar.index(temp)] -= temp
        personer -= temp
    svar += 1

print(f"Svar: {svar}")