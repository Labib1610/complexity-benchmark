import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    j, T = data[0], data[1]
    idx = 2
    sum1 = 0
    sum2 = 0
    # scan tasks
    for i in range(1, j + 1):
        p1 = data[idx]
        p2 = data[idx + 1]
        idx += 2
        sum1 += p1
        sum2 += p2
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    # no task bottleneck -> stage bottleneck
    if sum1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    solve()