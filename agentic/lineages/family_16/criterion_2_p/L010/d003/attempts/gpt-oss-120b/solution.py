import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    list1 = []  # d1 <= d2
    list2 = []  # d1 > d2
    for _ in range(n):
        d1 = int(next(it))
        d2 = int(next(it))
        if d1 <= d2:
            list1.append((d1, d2))
        else:
            list2.append((d1, d2))
    list1.sort(key=lambda x: x[0])          # ascending d1
    list2.sort(key=lambda x: -x[1])         # descending d2
    order = list1 + list2

    t1 = 0
    t2 = 0
    for d1, d2 in order:
        t1 += d1
        if t2 < t1:
            t2 = t1
        t2 += d2
    sys.stdout.write(str(t2))

if __name__ == "__main__":
    solve()