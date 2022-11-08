antal_ord = 4
mening = "hej vad heter du"

ord = mening.split(" ")
ord.reverse()

for o in range(len(ord)):
    if len(ord[o]) > 2:
        for i in range(len(ord[o])):
            if i > len(ord[o])-3:
                break
            elif ord[o][i+1] not in ["a","e","i","o","u","y"] and ord[o][i+2] not in ["a","e","i","o","u","y"]:
                ord[o] = ord[o][:i] + ord[o][i+1:]

for i in range(len(ord)):
    ord[i] = ord[i][::-1]

string = ""
for o in ord:
    string += o
    if not o == ord[-1]: string += " "

print(string)