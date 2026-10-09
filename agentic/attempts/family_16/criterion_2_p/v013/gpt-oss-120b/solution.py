import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    L = []
    R = []
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            L.append((p1, p2))
        else:
            R.append((p1, p2))
    L.sort(key=lambda x: x[0])          # ascending p1
    R.sort(key=lambda x: x[1], reverse=True)  # descending p2
    order = L + R

    t1 = 0
    t2 = 0
    for p1, p2 in order:
        t1 += p1
        if t2 < t1:
            t2 = t1
        t2 += p2
    sys.stdout.write(str(t2))

if __name__ == "__main__":
    solve()