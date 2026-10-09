import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    p1_list = []
    p2_list = []
    job_idx = None
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)
        if job_idx is None and p1 + p2 > T:
            job_idx = idx
    if job_idx is not None:
        print(f"JOB {job_idx}")
        return
    total_p1 = sum(p1_list)
    if total_p1 > T:
        print("LOAD 1")
        return
    total_p2 = sum(p2_list)
    # By problem guarantee, this must be > T
    print("LOAD 2")

if __name__ == "__main__":
    solve()