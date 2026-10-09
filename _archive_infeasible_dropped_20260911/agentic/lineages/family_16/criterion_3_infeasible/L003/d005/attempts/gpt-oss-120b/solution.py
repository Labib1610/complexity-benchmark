import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    col_sum = [0, 0]  # stage 1, stage 2
    job_idx = -1

    for idx in range(1, j + 1):
        d1 = int(next(it))
        d2 = int(next(it))
        col_sum[0] += d1
        col_sum[1] += d2
        if job_idx == -1 and d1 + d2 > T:
            job_idx = idx

    out = []
    if job_idx != -1:
        out.append(f"JOB {job_idx}")
    else:
        if col_sum[0] > T:
            out.append("LOAD 1")
        else:
            out.append("LOAD 2")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()