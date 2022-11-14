import math

n = 3
m = 0
total = n + m
green = 0
rest = 0

if n % 2 == 0:
    green = 20
    if m == 0:
        rest = 0
    else:
        rest = math.ceil(m / n) * 10

elif n % 2 == 1:
    if m >= n:
        m_temp = m+1
        n_temp = n-1
        green = 0
        rest = math.ceil((m_temp+n_temp)/n_temp)*10
    else:
        if m == 0:
            rest = 0
            green = math.ceil(n/2)*10

time = rest + green
print(time)