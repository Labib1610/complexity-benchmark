import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
forbidden_pairs = set()
for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    forbidden_pairs.add((u, v))

if m == 0:
    print("YES")
    print(' '.join(map(str, range(1, k + 1))))
else:
    for mask in range(1, 1 << n):
        if bin(mask).count('1') != k:
            continue
        pins = [i + 1 for i in range(n) if (mask >> i) & 1]
        
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                pair = (pins[i], pins[j]) if pins[i] < pins[j] else (pins[j], pins[i])
                if pair in forbidden_pairs:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, pins)))
            sys.exit()
    
    print("NO")