import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))

    sum1 = 0
    sum2 = 0
    bad_job = 0  # 0 means none found yet

    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        sum1 += p1
        sum2 += p2
        if not bad_job and p1 + p2 > T:
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