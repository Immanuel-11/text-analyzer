TOP_N = 3
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
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print(f"Top {TOP_N} words:")
for word, count in sorted_counts[:TOP_N]:
    print(f"{word}: {count}")

