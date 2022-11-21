krypto = [c for c in "32312410"]
pos_variations = []
final_variations = []
doubles = []

for i in range(len(krypto)):
    if i != len(krypto)-1:
        temp = krypto[i] + krypto[i+1]
        if int(temp) <= 27:
            pos_variations.append([krypto[i], temp])
            doubles.append(i)
        else:
            pos_variations.append([krypto[i]])
    else: pos_variations.append([krypto[i]])

print(pos_variations, doubles)

vals = [0 for c in range(len(doubles))]
while True:
    temp = []
    double_count = 0
    for i in range(len(pos_variations)):
        if len(pos_variations[i]) == 1:
            temp.append(pos_variations[i][0])
            continue
        else:
            if double_count == len(vals):
                if vals[double_count] == 0:
                    temp.append(pos_variations[i][0])
                    vals[double_count] = 1