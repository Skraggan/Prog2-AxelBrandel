while True:
    inp = input().split(" ")
    if int(inp[0]) >= int(inp[1]):
        print(int(inp[0])-int(inp[1]))
    else:
        print(int(inp[1])-int(inp[0]))