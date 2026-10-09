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
    impossible_job = -1
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        sum1 += p1
        sum2 += p2
        if impossible_job == -1 and p1 + p2 > T:
            impossible_job = idx
    if impossible_job != -1:
        print(f"JOB {impossible_job}")
    else:
        # exactly one of the loads is impossible
        if sum1 > T:
            print("LOAD 1")
        else:
            print("LOAD 2")

if __name__ == "__main__":
    solve()