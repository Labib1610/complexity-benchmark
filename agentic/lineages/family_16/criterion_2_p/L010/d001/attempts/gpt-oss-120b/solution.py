import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    early = []
    late = []
    for _ in range(n):
        p1 = int(next(it)); p2 = int(next(it))
        if p1 <= p2:
            early.append((p1, p2))
        else:
            late.append((p1, p2))
    early.sort(key=lambda x: x[0])          # ascending p1
    late.sort(key=lambda x: -x[1])          # descending p2
    seq = early + late

    t1 = 0  # completion time on machine 1 (preparation)
    t2 = 0  # completion time on machine 2 (assembly)
    for p1, p2 in seq:
        t1 += p1
        if t2 < t1:
            t2 = t1
        t2 += p2
    print(t2)

if __name__ == "__main__":
    solve()