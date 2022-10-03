import math
inp = input().split(" ")
for i in range(2): inp[i] = int(inp[i])
test_numbers = []
for i in range(inp[1]):
    test_numbers.append(int(input()))
numbers = [x for x in range(2, inp[0]+1)]

for i in numbers:
    print(i)
    if i > math.sqrt(inp[0]):
        break
    for n in numbers:
        if i == n:
            continue 
        else:
            if n % i == 0:
                numbers.remove(n)

print(len(numbers))
for i in test_numbers:
    if i in numbers:
        print(1)
    else:
        print(0)