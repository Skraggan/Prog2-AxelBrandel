chapter_info = [int(x) for x in input().split(" ")]
chapter_pages = []
chapter_dependecies = []
pages_read = 0
culminating_chapters = []

def check_dependant_chapters(chapter, dependencies):
    curr = chapter
    chapters = [chapter]
    active = True
    while active:
        active = False
        for i in dependencies:
            if curr == i[1]:
                active = True
                curr = i[0]
                chapters.append(curr)
    return chapters
        
while len(chapter_pages) != chapter_info[0]:
    temp = input().split(" ")
    for i in temp:
        chapter_pages.append(int(i))

for i in range(chapter_info[1]):
    chapter_dependecies.append([int(x) for x in input().split(" ")])

for i in range(chapter_info[1]):
    culminating_chapters.append(chapter_dependecies[i][1])
    if chapter_dependecies[i][0] in culminating_chapters:
        culminating_chapters.remove(chapter_dependecies[i][0])

for i in range(len(culminating_chapters)):
    chapters_read_1 = []
    chapters_read_1.append(check_dependant_chapters(culminating_chapters[i], chapter_dependecies))
    for n in range(len(culminating_chapters)):
        if n == i:
            continue
        chapters_read_2 = []
        chapters_read_2.append(check_dependant_chapters(culminating_chapters[n], chapter_dependecies))
        
        # Takes all the read chapters into one dimension and without any duplicates
        chapters_read_total = [el for arr in (chapters_read_1+chapters_read_2) for el in arr]
        chapters_read_total = list(dict.fromkeys(chapters_read_total))

        temp = 0
        for j in chapters_read_total:
            temp += chapter_pages[j-1]
        if temp <= pages_read or pages_read == 0:
            pages_read = temp

        # print(f"{chapters_read_total}, {temp}")

# print(chapter_pages)
print(pages_read)