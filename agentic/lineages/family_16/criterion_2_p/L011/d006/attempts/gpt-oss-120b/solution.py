import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    early = []
    late = []
    it = 1
    for _ in range(n):
        p = data[it]; q = data[it+1]; it += 2
        if p <= q:
            early.append((p, q))
        else:
            late.append((p, q))
    early.sort(key=lambda x: x[0])          # increasing p
    late.sort(key=lambda x: -x[1])          # decreasing q
    seq = early + late

    t1 = 0  # finish time on Prepare worker
    t2 = 0  # finish time on Finalize worker
    for p, q in seq:
        t1 += p
        if t2 < t1:
            t2 = t1
        t2 += q
    sys.stdout.write(str(t2))

if __name__ == "__main__":
    solve()