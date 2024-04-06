from collections import Counter

text = ''
with open('war_and_peace.txt', 'r', encoding='utf-8') as f:
    for l in f:
        text += l.lower()

c = Counter(text.split())
print(c.most_common(50))