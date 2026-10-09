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
    # store first violating job if any
    job_violation = None
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if job_violation is None and p1 + p2 > T:
            job_violation = idx
        sum1 += p1
        sum2 += p2
    out = []
    if job_violation is not None:
        out.append(f"JOB {job_violation}")
    elif sum1 > T:
        out.append("LOAD 1")
    else:
        out.append("LOAD 2")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()