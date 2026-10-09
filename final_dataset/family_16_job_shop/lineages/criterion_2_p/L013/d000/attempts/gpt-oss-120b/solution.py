import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    jobs = [(data[i], data[i + 1]) for i in range(1, 2 * n + 1, 2)]

    a = []  # p1 <= p2
    b = []  # p1 >  p2
    for p1, p2 in jobs:
        if p1 <= p2:
            a.append((p1, p2))
        else:
            b.append((p1, p2))

    a.sort(key=lambda x: x[0])          # increasing p1
    b.sort(key=lambda x: -x[1])         # decreasing p2
    order = a + b

    time1 = 0
    time2 = 0
    for p1, p2 in order:
        time1 += p1
        if time2 < time1:
            time2 = time1
        time2 += p2

    print(time2)


if __name__ == "__main__":
    solve()