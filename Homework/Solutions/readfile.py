file = open("randomwords.txt")

#How many words in this file start with b?
#Are there any duplicate words?
#Reprint these words in alphabetical order
filelist = file.readlines()
wordlist = []
for word in filelist: 
    wordlist.append(word.replace("\n", "")) 
bCount = 0
for i in wordlist:
    if i[0] == "b":
        bCount = bCount + 1

print("This many words start with b ", bCount)

uniques = []
duplicates =[]
for i in wordlist:
    if i not in uniques:
        uniques.append(i)
    else:
        duplicates.append(i)


print(duplicates)
wordlist.sort()
print(wordlist)

file.close()
