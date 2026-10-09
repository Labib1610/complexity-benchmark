import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    T = int(next(it))
    p1 = []
    p2 = []
    for _ in range(n):
        p1.append(int(next(it)))
        p2.append(int(next(it)))
    # Check isolated job
    for i, (a, b) in enumerate(zip(p1, p2), 1):
        if a + b > T:
            print(f"JOB {i}")
            return
    # Check load 1
    if sum(p1) > T:
        print("LOAD 1")
    else:
        # By problem guarantee, this must be true
        print("LOAD 2")

if __name__ == "__main__":
    solve()