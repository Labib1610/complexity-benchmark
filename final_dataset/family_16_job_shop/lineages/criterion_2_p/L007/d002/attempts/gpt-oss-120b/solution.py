import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    first = []
    second = []
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    first.sort(key=lambda x: x[0])          # increasing p1
    second.sort(key=lambda x: -x[1])        # decreasing p2
    schedule = first + second

    t1 = 0  # completion time on calligrapher
    t2 = 0  # completion time on bookbinder
    for p1, p2 in schedule:
        t1 += p1
        t2 = max(t2, t1) + p2
    sys.stdout.write(str(t2))

if __name__ == "__main__":
    solve()