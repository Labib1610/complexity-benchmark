import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    phase1_sum = 0
    phase2_sum = 0
    # store first exceeding job if any
    job_exceed = None
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if job_exceed is None and p1 + p2 > T:
            job_exceed = idx
        phase1_sum += p1
        phase2_sum += p2
    if job_exceed is not None:
        sys.stdout.write(f"JOB {job_exceed}")
    else:
        if phase1_sum > T:
            sys.stdout.write("LOAD 1")
        else:
            # by problem guarantee, phase2_sum > T
            sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()