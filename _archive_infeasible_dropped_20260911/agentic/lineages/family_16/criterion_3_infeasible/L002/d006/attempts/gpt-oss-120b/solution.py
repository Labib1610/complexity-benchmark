import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))

    sum_p1 = 0
    sum_p2 = 0
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            sys.stdout.write(f"JOB {idx}")
            return
        sum_p1 += p1
        sum_p2 += p2

    if sum_p1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()