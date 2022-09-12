characters = [*str(input())]
sentence = str(input()).split(" ")
pairs = {}
success = True

def check(character, word):
    if character in pairs.keys():
        if pairs[character] == word:
            return True
        else:
            return False
    else:
        if word in pairs.values():
            return False
        else:
            pairs[character] = word
            return True

if len(characters) == len(sentence):
    for i in range(len(characters)):
        if not check(characters[i], sentence[i]):
            success = False
            break
else:
    success = False

print(success)