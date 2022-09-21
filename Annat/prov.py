import numpy as np
x = -0.5
np_logval = np.log(1+x)

def log(arg, amountOfTerms):
    x = arg - 1
    sum = 0
    for i in range(1, amountOfTerms+1):
        if i % 2 == 1:
            sum += (x**i) /i
        else:
            sum -= (x**i) / i
    return sum

leastAmountOfTerms = 0
while True:
    leastAmountOfTerms += 1
    current = abs(np_logval - log(0.5, leastAmountOfTerms))
    if current <= 10**-6:
        break

print(current)
