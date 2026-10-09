import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    p1 = []
    p2 = []
    job_idx = -1
    for idx in range(1, j + 1):
        a = int(next(it))
        b = int(next(it))
        p1.append(a)
        p2.append(b)
        if job_idx == -1 and a + b > T:
            job_idx = idx
    if job_idx != -1:
        print(f"JOB {job_idx}")
        return
    sum_p1 = sum(p1)
    sum_p2 = sum(p2)
    if sum_p1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    solve()