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
    job_idx = -1
    for idx in range(1, j + 1):
        d1 = int(next(it))
        d2 = int(next(it))
        sum1 += d1
        sum2 += d2
        if job_idx == -1 and d1 + d2 > T:
            job_idx = idx
    out = []
    if job_idx != -1:
        out.append(f"JOB {job_idx}")
    else:
        if sum1 > T:
            out.append("LOAD 1")
        else:
            out.append("LOAD 2")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()