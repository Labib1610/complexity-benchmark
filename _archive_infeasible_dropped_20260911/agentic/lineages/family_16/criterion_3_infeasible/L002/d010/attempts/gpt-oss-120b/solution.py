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
    bad_job = None
    for idx in range(1, j + 1):
        q1 = int(next(it))
        q2 = int(next(it))
        sum1 += q1
        sum2 += q2
        if bad_job is None and q1 + q2 > T:
            bad_job = idx
    out = []
    if bad_job is not None:
        out.append(f"JOB {bad_job}")
    elif sum1 > T:
        out.append("LOAD 1")
    else:
        # Since the problem guarantees impossibility, sum2 must exceed T here
        out.append("LOAD 2")
    sys.stdout.write(out[0])

if __name__ == "__main__":
    solve()