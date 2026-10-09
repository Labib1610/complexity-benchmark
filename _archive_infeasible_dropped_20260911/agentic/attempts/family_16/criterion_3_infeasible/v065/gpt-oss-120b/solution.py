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
    job_err = None
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if job_err is None and p1 + p2 > T:
            job_err = idx
        sum1 += p1
        sum2 += p2
    out = []
    if job_err is not None:
        out.append(f"JOB {job_err}")
    else:
        if sum1 > T:
            out.append("LOAD 1")
        else:
            out.append("LOAD 2")
    sys.stdout.write(out[0])

if __name__ == "__main__":
    solve()