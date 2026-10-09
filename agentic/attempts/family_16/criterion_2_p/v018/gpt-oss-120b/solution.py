import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    early = []   # a <= b
    late = []    # a > b
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        if a <= b:
            early.append((a, b))
        else:
            late.append((a, b))
    early.sort(key=lambda x: x[0])          # increasing a
    late.sort(key=lambda x: x[1], reverse=True)  # decreasing b
    order = early + late

    t1 = 0  # completion time on machine 1
    t2 = 0  # completion time on machine 2
    for a, b in order:
        t1 += a
        if t2 < t1:
            t2 = t1 + b
        else:
            t2 += b
    sys.stdout.write(str(t2))

if __name__ == "__main__":
    solve()