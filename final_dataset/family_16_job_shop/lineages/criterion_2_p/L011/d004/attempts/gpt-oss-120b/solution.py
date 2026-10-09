import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    jobs = []
    for _ in range(n):
        a = int(next(it)); b = int(next(it))
        if a <= b:
            jobs.append((0, a, a, b))   # (group, key, a, b)
        else:
            jobs.append((1, -b, a, b))
    jobs.sort()
    t1 = 0  # completion time on Main Stage
    t2 = 0  # completion time on Review Room
    for _, _, a, b in jobs:
        t1 += a
        if t2 < t1:
            t2 = t1
        t2 += b
    print(t2)

if __name__ == "__main__":
    solve()