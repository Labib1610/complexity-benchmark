import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    first = []   # a <= b
    second = []  # a > b
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        if a <= b:
            first.append((a, b))
        else:
            second.append((a, b))
    first.sort(key=lambda x: x[0])          # increasing a
    second.sort(key=lambda x: -x[1])        # decreasing b
    order = first + second

    t1 = 0  # finish time on Surveyor (machine 1)
    t2 = 0  # finish time on Harvester (machine 2)
    for a, b in order:
        t1 += a
        if t2 < t1:
            t2 = t1
        t2 += b
    print(t2)

if __name__ == "__main__":
    solve()