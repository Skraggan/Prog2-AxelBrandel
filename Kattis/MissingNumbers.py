n = int(input())
numbers = []
missing = []
failed = False

for i in range(n):
    inp = int(input())
    numbers.append(inp)
numbers.sort()

for i in range(1, numbers[-1]+1):
    if i not in numbers:
        missing.append(i)
        failed = True

if failed:
    for i in missing:
        print(i)
else:
    print("good job")

