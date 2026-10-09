import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    front = []
    back = []
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        if p1 <= p2:
            front.append((p1, p2))
        else:
            back.append((p1, p2))
    front.sort(key=lambda x: x[0])          # increasing p1
    back.sort(key=lambda x: x[1], reverse=True)  # decreasing p2
    order = front + back

    t1 = t2 = 0
    for p1, p2 in order:
        t1 += p1
        if t2 < t1:
            t2 = t1 + p2
        else:
            t2 += p2
    sys.stdout.write(str(t2))

if __name__ == "__main__":
    solve()