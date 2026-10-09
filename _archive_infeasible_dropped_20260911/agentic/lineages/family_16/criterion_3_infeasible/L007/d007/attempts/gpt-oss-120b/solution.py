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
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        # check JOB condition for this item
        if p1 + p2 > T:
            print(f"JOB {idx}")
            return
        p1_list.append(p1)
        p2_list.append(p2)

    sum1 = sum(p1_list)
    sum2 = sum(p2_list)

    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")
    else:
        # According to the problem statement, exactly one condition is impossible,
        # so this branch should never be reached.
        pass

if __name__ == "__main__":
    solve()