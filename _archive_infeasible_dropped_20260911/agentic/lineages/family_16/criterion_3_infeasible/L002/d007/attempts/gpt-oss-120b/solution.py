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
        # check JOB condition for this element
        if p1 + p2 > T:
            print(f"JOB {idx}")
            return
        sum1 += p1
        sum2 += p2
    # check LOAD conditions
    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")
    else:
        # According to the problem statement this situation cannot occur.
        # Still, output a fallback (should never be needed).
        print("LOAD 1")

if __name__ == "__main__":
    solve()