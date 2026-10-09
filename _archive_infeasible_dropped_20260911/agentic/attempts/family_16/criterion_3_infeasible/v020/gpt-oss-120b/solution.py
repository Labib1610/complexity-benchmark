import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    j, T = data[0], data[1]
    sum1 = sum2 = 0
    idx = 2
    job_violation = None

    for i in range(1, j + 1):
        p1 = data[idx]
        p2 = data[idx + 1]
        idx += 2

        if job_violation is None and p1 + p2 > T:
            job_violation = i

        sum1 += p1
        sum2 += p2

    if job_violation is not None:
        sys.stdout.write(f"JOB {job_violation}")
    elif sum1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()