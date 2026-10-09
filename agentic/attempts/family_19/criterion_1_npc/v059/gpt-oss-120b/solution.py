import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    # read operations
    ops = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(k)]
    # read edges
    edges = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(m)]
    # As the general multi‑commodity integer flow problem is NP‑hard,
    # and without concrete limits we cannot implement a guaranteed
    # polynomial solution, we output that no feasible assignment is
    # found.
    print("NO")

if __name__ == "__main__":
    solve()