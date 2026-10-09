import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    j = next(it)
    T = next(it)

    total1 = 0
    total2 = 0
    bad_job = None

    for idx in range(1, j + 1):
        p1 = next(it)
        p2 = next(it)
        if bad_job is None and p1 + p2 > T:
            bad_job = idx
        total1 += p1
        total2 += p2

    if bad_job is not None:
        sys.stdout.write(f"JOB {bad_job}")
    elif total1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()