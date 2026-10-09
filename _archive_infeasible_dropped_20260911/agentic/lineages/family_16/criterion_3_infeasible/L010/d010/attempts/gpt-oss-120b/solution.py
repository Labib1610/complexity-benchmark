import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    total1 = 0
    total2 = 0
    job_idx = None
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if job_idx is None and p1 + p2 > T:
            job_idx = idx
        total1 += p1
        total2 += p2
    out = []
    if job_idx is not None:
        out.append(f"JOB {job_idx}")
    elif total1 > T:
        out.append("LOAD 1")
    else:
        out.append("LOAD 2")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()