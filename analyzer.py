from pathlib import Path


TOP_N = 10


total_counts = {}

def analyze_file(path):
    counts = {}
    with open(path, encoding="utf-8") as f:
        words = f.read().split()
        words = [word.strip(".,';:\"!@#$%^&*()_+-=").lower() for word in words]
    print(f"{path.name} has {len(words)} words")
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts  

for path in Path("data").glob("*.txt"):
    counts = analyze_file(path)
    for word, count in counts.items():
        if word in total_counts:
            total_counts[word] += count
        else:
            total_counts[word] = count  
print(f"All files: {sum(total_counts.values())} words")
print(f"Top {TOP_N} words:")
sorted_counts = (sorted(total_counts.items(), key=lambda x: x[1], reverse=True))
for word, count in sorted_counts[:TOP_N]:
    print(f"{word}: {count}")

