import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    j = next(it)
    T = next(it)

    sum1 = 0
    sum2 = 0

    for idx in range(1, j + 1):
        p1 = next(it)
        p2 = next(it)
        if p1 + p2 > T:
            sys.stdout.write(f"JOB {idx}\n")
            return
        sum1 += p1
        sum2 += p2

    if sum1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        # guaranteed that some certificate exists, so sum2 > T
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    solve()