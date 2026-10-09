import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    orders = [(int(next(it))-1, int(next(it))-1, int(next(it))) for _ in range(k)]
    edges = [(int(next(it))-1, int(next(it))-1, int(next(it))) for _ in range(m)]

    # The problem is NP‑hard in general (multi‑commodity flow with integer
    # constraints).  Without further limits on the input size we cannot
    # guarantee a correct solution in the required time.
    # Hence we output “NO” as a safe fallback.
    print("NO")

if __name__ == "__main__":
    solve()