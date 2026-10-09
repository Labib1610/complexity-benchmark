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
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {idx}")
            return
        sum1 += p1
        sum2 += p2
    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")
    else:
        # According to problem statement this should never happen
        # but we include a fallback.
        print("JOB 1")

if __name__ == "__main__":
    solve()