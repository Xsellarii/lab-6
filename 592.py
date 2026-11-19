pos = input().strip()

col = ord(pos[0]) - ord('a')  
row = int(pos[1]) - 1         


for r in range(7, -1, -1):
    line = []
    for c in range(8):
        if r == row and c == col:
            line.append("B")
        elif abs(r - row) == abs(c - col):
            line.append("*")
        else:
            line.append(".")
    print(" ".join(line))