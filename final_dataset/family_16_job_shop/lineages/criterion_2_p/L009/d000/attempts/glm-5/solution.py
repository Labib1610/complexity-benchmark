import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    A = []
    B = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        if p1 <= p2:
            A.append((p1, p2))
        else:
            B.append((p1, p2))
    A.sort(key=lambda x: x[0])
    B.sort(key=lambda x: x[1], reverse=True)
    order = A + B
    t1 = 0
    t2 = 0
    for p1, p2 in order:
        t1 += p1
        if t1 > t2:
            t2 = t1 + p2
        else:
            t2 += p2
    print(t2)

solve()