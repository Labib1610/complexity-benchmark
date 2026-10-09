import sys
import itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # enumerate permutations of positions 1..n
    # p[i] = position (1‑based) of operation i
    for perm in itertools.permutations(range(1, n + 1)):
        waste = 0
        for u, v in edges:
            waste += abs(perm[u] - perm[v])
            if waste > B:          # early stop
                break
        if waste <= B:
            # found a feasible schedule
            print("YES")
            print(' '.join(map(str, perm)))
            return

    print("NO")

if __name__ == "__main__":
    solve()