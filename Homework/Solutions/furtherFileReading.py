"""
A list of words is given in a file words.txt
For this file, please give the number of times each word appears, in the form {word:number}
Please display the longest word
How many words are in the list? (Don't peek) What percentage of the words are unique?
"""

file = open("words.txt")
words = file.readlines()
file.close()
longestWordLength = 0
longestWord = ""
wordFrequency = {}
for i in words:
    i = i.replace("\n", "")
    if i not in wordFrequency.keys():
        wordFrequency[i] = 1
    else:
        wordFrequency[i] = wordFrequency[i] + 1
    if len(i) > longestWordLength:
        longestWordLength = len(i)
        longestWord = i

totalDictLength = len(words)
uniqueWords = 0
for key, value in wordFrequency.items():
    if value == 1:
        uniqueWords = uniqueWords + 1 
print(wordFrequency)
print(longestWord)
print((uniqueWords/totalDictLength)*100)

