import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    j, T = data[0], data[1]
    idx = 2
    total1 = 0
    total2 = 0
    for i in range(1, j + 1):
        p1 = data[idx]
        p2 = data[idx + 1]
        idx += 2
        if p1 + p2 > T:
            sys.stdout.write(f"JOB {i}")
            return
        total1 += p1
        total2 += p2
    if total1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()