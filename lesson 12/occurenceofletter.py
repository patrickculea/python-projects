word = input("please can you enter a word.")
char = input("please can you give me a charachter, I will tell you how many times the charachter appears in the word after.")
i = 0
count = 0
while i < len(word):
    if(word [i] == char):
        count += 1
    i += 1

print(f"{char} has appeared {count} number of times in {word}")