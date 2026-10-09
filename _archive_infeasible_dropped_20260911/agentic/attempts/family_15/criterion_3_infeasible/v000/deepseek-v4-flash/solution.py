k = int(input())
seq1 = input().strip()
others = [input().strip() for _ in range(k - 1)]

print("BLOCK")
for c in sorted(set(seq1)):
    for idx, s in enumerate(others, start=2):
        if c not in s:
            print(c, idx)
            break