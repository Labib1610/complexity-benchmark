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
        d1 = int(next(it)); d2 = int(next(it))
        if d1 <= d2:
            front.append((d1, d2))
        else:
            back.append((d1, d2))
    front.sort(key=lambda x: x[0])          # increasing d1
    back.sort(key=lambda x: x[1], reverse=True)  # decreasing d2
    order = front + back

    t1 = 0  # completion time on machine 1
    t2 = 0  # completion time on machine 2
    for d1, d2 in order:
        t1 += d1
        t2 = max(t2, t1) + d2
    sys.stdout.write(str(t2))

if __name__ == "__main__":
    solve()