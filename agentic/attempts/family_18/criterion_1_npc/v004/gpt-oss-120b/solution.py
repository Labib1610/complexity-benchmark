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
    # Brute-force all permutations
    for perm in itertools.permutations(range(n)):
        # position of each module (0-indexed)
        pos = [0] * n
        for idx, mod in enumerate(perm):
            pos[mod] = idx
        total = 0
        ok = True
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                ok = False
                break
        if ok:
            # output positions as 1-indexed permutation of modules
            # need to print position of module i (1..n)
            out = [str(pos[i] + 1) for i in range(n)]
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(out))
            return
    sys.stdout.write("NO")

if __name__ == "__main__":
    solve()