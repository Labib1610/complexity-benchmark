import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    first = []   # d1 <= d2
    second = []  # d1 > d2
    for _ in range(n):
        d1 = int(next(it))
        d2 = int(next(it))
        if d1 <= d2:
            first.append((d1, d2))
        else:
            second.append((d1, d2))
    first.sort(key=lambda x: x[0])          # ascending d1
    second.sort(key=lambda x: x[1], reverse=True)  # descending d2
    order = first + second

    time_a = 0
    time_b = 0
    for d1, d2 in order:
        time_a += d1
        if time_b < time_a:
            time_b = time_a
        time_b += d2
    print(time_b)

if __name__ == "__main__":
    solve()