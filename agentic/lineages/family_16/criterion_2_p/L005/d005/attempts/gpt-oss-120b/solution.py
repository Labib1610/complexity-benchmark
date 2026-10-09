import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    early = []   # t1 <= t2
    late = []    # t1 > t2
    for _ in range(n):
        t1 = int(next(it)); t2 = int(next(it))
        if t1 <= t2:
            early.append((t1, t2))
        else:
            late.append((t1, t2))
    early.sort(key=lambda x: x[0])          # ascending t1
    late.sort(key=lambda x: x[1], reverse=True)  # descending t2
    order = early + late

    time_a = 0   # finish time on Alpha (machine 1)
    time_b = 0   # finish time on Beta (machine 2)
    for t1, t2 in order:
        time_a += t1               # Alpha finishes this job
        start_b = time_a if time_a > time_b else time_b
        time_b = start_b + t2      # Beta finishes this job
    print(time_b)

if __name__ == "__main__":
    solve()