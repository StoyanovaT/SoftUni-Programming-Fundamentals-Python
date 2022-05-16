word1 = input()
word2 = input()
last_printed = ''

for l in range(len(word1) + 1):
    new_word = word2[:l] + word1[l:len(word1)]
    if new_word not in (word1, word2, last_printed):
        print(new_word)
        last_printed = new_word

print(word2)