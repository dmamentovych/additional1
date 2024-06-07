import random
import re

with open('text.txt', 'r', encoding="utf-8") as file:
    text = file.read()

text = text.lower()

tokens = re.findall(r"\b\w+\b|[.,!?;]", text)

word_dict = {}
for i in range(len(tokens) - 1):
    word = tokens[i]
    next_word = tokens[i + 1]
    if word not in word_dict:
        word_dict[word] = []
    word_dict[word].append(next_word)

generated_text = []

current_word = random.choice(list(word_dict.keys()))
generated_text.append(current_word)

for _ in range(200 - 1):  
    next_words = word_dict.get(current_word)
    if not next_words:
        break
    next_word = random.choice(next_words)
    generated_text.append(next_word)
    current_word = next_word

print(' '.join(generated_text))