inp1 = input()
inp2 = input()
amountOfComs, cost = inp1.split()
eachComListensString = inp2.split()
for i in eachComListensString:

currentBestProfit = 0

for i in range(0, amountOfComs):
    currentProfit = 0
    for n in range(i, amountOfComs):
        if eachComListens[n] > cost:
            currentProfit += eachComListens[n] - cost
        else:
            break
    if currentProfit > currentBestProfit:
        currentBestProfit = currentProfit

print(currentBestProfit)

