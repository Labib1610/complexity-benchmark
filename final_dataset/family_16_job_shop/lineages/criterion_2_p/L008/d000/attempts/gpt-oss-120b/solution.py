import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    jobs = [(data[i], data[i + 1]) for i in range(1, 2 * n, 2)]

    g1 = []  # a <= b
    g2 = []  # a >  b
    for a, b in jobs:
        if a <= b:
            g1.append((a, b))
        else:
            g2.append((a, b))

    g1.sort(key=lambda x: x[0])          # increasing a
    g2.sort(key=lambda x: x[1], reverse=True)  # decreasing b

    order = g1 + g2

    time_a = 0
    time_b = 0
    for a, b in order:
        time_a += a
        if time_b < time_a:
            time_b = time_a
        time_b += b

    sys.stdout.write(str(time_b))

if __name__ == "__main__":
    solve()