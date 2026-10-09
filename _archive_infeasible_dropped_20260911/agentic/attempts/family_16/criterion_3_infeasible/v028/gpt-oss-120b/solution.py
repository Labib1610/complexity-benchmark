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
    job_idx = 1
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            sys.stdout.write(f"JOB {job_idx}")
            return
        sum1 += p1
        sum2 += p2
        job_idx += 1
    if sum1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()