import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    times = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        times.append((p1, p2))
        idx += 2

    # Johnson's rule for two-machine flow shop
    group1 = []
    group2 = []
    for p1, p2 in times:
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))

    group1.sort(key=lambda x: x[0])
    group2.sort(key=lambda x: -x[1])

    order = group1 + group2

    m1_free = 0
    m2_free = 0
    for p1, p2 in order:
        start1 = m1_free
        end1 = start1 + p1
        start2 = max(end1, m2_free)
        end2 = start2 + p2
        m1_free = end1
        m2_free = end2

    print(m2_free)

solve()