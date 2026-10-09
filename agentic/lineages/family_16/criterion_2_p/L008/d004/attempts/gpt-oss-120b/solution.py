import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    group1 = []          # p1 <= p2
    group2 = []          # p1 >  p2
    total_p2 = 0
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        total_p2 += p2
        if p1 <= p2:
            group1.append((p1, p2))
        else:
            group2.append((p1, p2))

    group1.sort(key=lambda x: x[0])          # increasing p1
    group2.sort(key=lambda x: -x[1])         # decreasing p2

    buf = 0
    idle = 0
    for p1, p2 in group1:
        buf -= p1
        if buf < 0:
            idle += -buf
            buf = 0
        buf += p2
    for p1, p2 in group2:
        buf -= p1
        if buf < 0:
            idle += -buf
            buf = 0
        buf += p2

    print(idle + total_p2)

if __name__ == "__main__":
    solve()