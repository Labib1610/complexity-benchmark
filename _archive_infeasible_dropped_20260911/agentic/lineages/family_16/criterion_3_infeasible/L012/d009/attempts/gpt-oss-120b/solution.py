import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))

    p1 = []
    p2 = []

    # read all pairs, also look for a job that exceeds T alone
    job_index = -1
    for idx in range(1, j + 1):
        a = int(next(it))
        b = int(next(it))
        p1.append(a)
        p2.append(b)
        if job_index == -1 and a + b > T:
            job_index = idx  # 1‑based

    if job_index != -1:
        sys.stdout.write(f"JOB {job_index}")
        return

    total_p1 = sum(p1)
    if total_p1 > T:
        sys.stdout.write("LOAD 1")
        return

    total_p2 = sum(p2)
    # by problem guarantee this must be > T now
    sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()