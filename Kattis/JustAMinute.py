n = int(input())
measurements = []
sum = [0,0]

for i in range(n):
    inp = input()
    minutes, seconds = inp.split(" ")
    measurements.append([int(minutes), int(seconds)])

for i in measurements:
    sum[0] += i[0]
    sum[1] += i[1]

answer = (sum[1]/60)/sum[0]

if answer <= 1:
    print("measurement error")
else: print(answer)