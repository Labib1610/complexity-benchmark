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
        p1 = int(next(it)); p2 = int(next(it))
        if p1 <= p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    first.sort(key=lambda x: x[0])          # ascending p1
    second.sort(key=lambda x: -x[1])        # descending p2
    order = first + second

    t1 = 0  # completion time on solver
    t2 = 0  # completion time on tracer
    for p1, p2 in order:
        t1 += p1
        t2 = max(t2, t1) + p2
    print(t2)

if __name__ == "__main__":
    solve()