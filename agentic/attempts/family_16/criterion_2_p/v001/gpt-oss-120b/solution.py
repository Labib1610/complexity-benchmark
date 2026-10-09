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
    second.sort(key=lambda x: x[1], reverse=True)  # decreasing p2
    order = first + second

    time_a = 0
    time_b = 0
    for p1, p2 in order:
        time_a += p1
        if time_b < time_a:
            time_b = time_a
        time_b += p2
    sys.stdout.write(str(time_b))

if __name__ == "__main__":
    solve()