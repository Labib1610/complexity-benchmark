import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(input_data[idx]); idx += 1
    
    neg = []  # d < 0
    nonneg = []  # d >= 0
    
    for _ in range(j):
        p1 = int(input_data[idx]); idx += 1
        p2 = int(input_data[idx]); idx += 1
        d = p1 - p2
        if d < 0:
            neg.append((p2, p1, d))
        else:
            nonneg.append((d, p2, p1))
    
    neg.sort(key=lambda x: x[0])  # sort by p2 ascending
    nonneg.sort(key=lambda x: -x[0])  # sort by d descending
    
    g = 0
    X = 0
    
    for p2, p1, d in neg:
        X += p1
        g = max(p2, g - d)
    
    for d, p2, p1 in nonneg:
        X += p1
        g = max(p2, g - d)
    
    print(X + g)

solve()