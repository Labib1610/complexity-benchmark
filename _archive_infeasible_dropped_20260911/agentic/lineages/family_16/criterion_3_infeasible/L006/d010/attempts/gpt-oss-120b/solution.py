import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    p1_list = []
    p2_list = []
    for _ in range(j):
        p1 = int(next(it)); p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)

    # Type A: isolated job
    for idx, (p1, p2) in enumerate(zip(p1_list, p2_list), 1):
        if p1 + p2 > T:
            print(f"JOB {idx}")
            return

    # Type B component 1: load 1
    max_prefix = 0
    cur = 0
    for p1 in p1_list:
        cur += p1
        if cur > max_prefix:
            max_prefix = cur
    if max_prefix > T:
        print("LOAD 1")
        return

    # Type B component 2: load 2
    total_p2 = sum(p2_list)
    if total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    solve()