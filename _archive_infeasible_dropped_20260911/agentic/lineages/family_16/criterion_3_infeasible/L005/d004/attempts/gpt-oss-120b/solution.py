import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))

    total1 = 0
    total2 = 0

    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            sys.stdout.write(f"JOB {idx}\n")
            return
        total1 += p1
        total2 += p2

    if total1 > T:
        sys.stdout.write("LOAD 1\n")
    else:
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    solve()