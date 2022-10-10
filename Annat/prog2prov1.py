try:
    amount_of_integers = int(input())
    integers = []
    for i in range(amount_of_integers):
        integers.append(int(input()))
    for i in range(amount_of_integers-1, -1, -1):
        print(integers[i])
except:
    print("Fel inmatning!")