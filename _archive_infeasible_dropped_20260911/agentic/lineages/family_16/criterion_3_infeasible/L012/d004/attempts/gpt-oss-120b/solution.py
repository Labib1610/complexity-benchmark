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
        p = int(next(it))
        q = int(next(it))
        if p + q > T:
            sys.stdout.write(f"JOB {idx}")
            return
        sum1 += p
        sum2 += q
    if sum1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()