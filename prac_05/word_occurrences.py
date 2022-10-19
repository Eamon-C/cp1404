"""
CP1404 prac
word_occurrences.py
Estimate: 30min
Actual: 40min
"""

text = input("Text: ")
word_to_count = {}
words = text.split()
for word in sorted(words):
    word_count = word_to_count.pop(word, 0)
    word_to_count[word] = word_count + 1

max_len = max(len(word) for word in word_to_count)

for word, word_count in word_to_count.items():
    print(f"{word:{max_len}}: {word_count}")
