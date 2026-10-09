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

    # Precompute adjacency list for possible pruning (optional)
    # Brute-force all permutations (feasible for n up to ~8-9)
    positions = list(range(n))
    for perm in itertools.permutations(positions):
        # perm[i] = position (0‑based) of artifact i
        total = 0
        for u, v in edges:
            total += abs(perm[u] - perm[v])
            if total > B:
                break
        if total <= B:
            # convert to 1‑based bay indices
            ans = [p + 1 for p in perm]
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(map(str, ans)))
            return
    sys.stdout.write("NO")

if __name__ == "__main__":
    solve()