import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    j = next(it)
    T = next(it)

    sum1 = 0
    sum2 = 0
    bad_job = 0

    for idx in range(1, j + 1):
        p1 = next(it)
        p2 = next(it)
        sum1 += p1
        sum2 += p2
        if bad_job == 0 and p1 + p2 > T:
            bad_job = idx

    out = []
    if bad_job:
        out = f"JOB {bad_job}"
    elif sum1 > T:
        out = "LOAD 1"
    else:
        out = "LOAD 2"

    sys.stdout.write(out + "\n")

if __name__ == "__main__":
    solve()