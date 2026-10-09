import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    sums = [0, 0]  # sum for stage 1 and 2
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {idx}")
            return
        sums[0] += p1
        sums[1] += p2
    if sums[0] > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    solve()