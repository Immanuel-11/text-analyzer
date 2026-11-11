with open("data/note1.txt", encoding="utf-8") as f:
    words = f.read().split()
    words = [word.strip(".,';:\"!@#$%^&*()_+-=").lower() for word in words]
print(f"note1.txt has {len(words)} words")
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
for word, count in counts.items():
    print(f"{word}: {count}")

