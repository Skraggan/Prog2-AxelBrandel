chapter_info = [int(x) for x in input().split(" ")]
chapter_pages = []
chapter_dependecies = []

while len(chapter_pages) != chapter_info[0]:
    temp = input().split(" ")
    for i in temp:
        chapter_pages.append(int(i))

for i in range(chapter_info[1]):
    chapter_dependecies.append([int(x) for x in input().split(" ")])


for i in range(chapter_info[1]):
    chapters_read = []
    
    for n in range(chapter_info[1]):

    