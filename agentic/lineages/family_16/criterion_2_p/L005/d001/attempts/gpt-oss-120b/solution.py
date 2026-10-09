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
        t1 = int(next(it)); t2 = int(next(it))
        if t1 <= t2:
            first.append((t1, t2))
        else:
            second.append((t1, t2))
    first.sort(key=lambda x: x[0])          # ascending t1
    second.sort(key=lambda x: -x[1])        # descending t2
    seq = first + second

    time1 = 0
    time2 = 0
    for t1, t2 in seq:
        time1 += t1
        if time2 < time1:
            time2 = time1 + t2
        else:
            time2 += t2
    sys.stdout.write(str(time2))

if __name__ == "__main__":
    solve()