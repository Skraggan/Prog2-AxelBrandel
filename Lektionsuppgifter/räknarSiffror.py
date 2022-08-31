numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
count = 0
inp = input("Skriv vad som helst: ")

for i in inp:
    if i in numbers:
        count += 1

print("Det finns " + str(count) + " siffra/siffror i ditt svar!")