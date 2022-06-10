words = input().split(" ")
palindrome = input()
palindromes_list = []

for w in words:
    rev_list = reversed(w)
    rev_word = "".join(rev_list)
    if rev_word == w:
        palindromes_list.append(w)

occurrences = palindromes_list.count(palindrome)
print(palindromes_list)
print(f"Found palindrome {occurrences} times")
