ettor = int(input("Antal ettor ? "))
tvåor = int(input("Antal tvåor ? "))
treor = int(input("Antal treor ? "))
fyror = int(input("Antal fyror ? "))
actual_values = [0, 0, 0, 0]

total_styrka = ettor*1 + tvåor*2 + treor*3 + fyror*4
target_styrka = int(total_styrka/2)

for i in range(ettor+1):
    for j in range(tvåor+1):
        for k in range(treor+1):
            for l in range(fyror+1):
                if i + j*2 + k*3 + l*4 == target_styrka:
                    actual_values = [i, j, k, l]

print()
print(f"Svar: {actual_values[0]} {actual_values[1]} {actual_values[2]} {actual_values[3]}")

