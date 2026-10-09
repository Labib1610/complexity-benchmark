import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    deadline = T + 1
    p1_list = []
    p2_list = []
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)
        if 1 + p1 + p2 > deadline:
            print(f"JOB {idx}")
            return
    sum1 = sum(p1_list)
    sum2 = sum(p2_list)
    if 1 + sum1 > deadline:
        print("LOAD 1")
    else:
        # guaranteed that at least one certificate exists
        print("LOAD 2")

if __name__ == "__main__":
    solve()