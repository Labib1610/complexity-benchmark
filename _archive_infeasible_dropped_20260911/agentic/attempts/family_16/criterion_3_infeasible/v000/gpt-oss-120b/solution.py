import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    j, T = data[0], data[1]
    sum1 = 0
    sum2 = 0
    job_idx = -1

    idx = 2
    for i in range(1, j + 1):
        p1 = data[idx]
        p2 = data[idx + 1]
        idx += 2

        sum1 += p1
        sum2 += p2

        if job_idx == -1 and p1 + p2 > T:
            job_idx = i

    out = []
    if job_idx != -1:
        out.append(f"JOB {job_idx}")
    elif sum1 > T:
        out.append("LOAD 1")
    else:  # sum2 > T must hold by problem guarantee
        out.append("LOAD 2")
    sys.stdout.write(out[0])

if __name__ == "__main__":
    solve()