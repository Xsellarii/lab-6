text = input()
text_lower = text.lower()

counts = [text_lower.count(ch) for ch in "abcdefghijklmnopqrstuvwxyz"]
print(*counts)