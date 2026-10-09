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
        p1 = int(next(it))
        p2 = int(next(it))
        sum1 += p1
        sum2 += p2
        if job_idx == -1 and p1 + p2 > T:
            job_idx = idx
    if job_idx != -1:
        sys.stdout.write(f"JOB {job_idx}\n")
    elif sum1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    solve()