inp1 = input()
inp2 = input()
amountOfComs, cost = inp1.split()
eachComListens = inp2.split()
amountOfComs, cost = int(amountOfComs), int(cost)
for i in range(0, len(eachComListens)):
    eachComListens[i] = int(eachComListens[i])

currentBestProfit = 0

for i in range(0, amountOfComs):
    currentProfit = 0
    for n in range(i, amountOfComs):
        if eachComListens[n] > cost:
            currentProfit += eachComListens[n] - cost
    if currentProfit > currentBestProfit:
        currentBestProfit = currentProfit

print(currentBestProfit)

