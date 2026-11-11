with open("data/note1.txt", encoding="utf-8") as f:
    text = f.read().split()

print(f"Number of words: {len(text)}")

