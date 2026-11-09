from collections import Counter

text = "the quick brown fox jumps over the lazy dog"

# word freq
words = text.split()
word_freq = Counter(words)

#Character freq
char_freq = Counter(text.replace(" ", ""))

print("Word Frequency: ")
for word, count in word_freq.items():
    print(f"{word}: {count}")

print("\nCharacter Frequency: ")
for char, count in char_freq.items():
    print(f"{char}: {count}")