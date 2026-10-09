import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
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
    early.sort(key=lambda x: x[0])          # increasing p1
    late.sort(key=lambda x: -x[1])           # decreasing p2
    seq = early + late

    E = 0
    C = 0
    for p1, p2 in seq:
        C += p1
        if E < C:
            E = C
        E += p2
    print(E)

if __name__ == "__main__":
    solve()