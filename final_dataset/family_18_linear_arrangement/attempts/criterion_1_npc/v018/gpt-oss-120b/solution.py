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

    # If n is too large for brute force, we give up (problem constraints guarantee small n)
    if n > 9:
        print("NO")
        return

    positions = list(range(1, n + 1))
    for perm in itertools.permutations(positions):
        # perm[i] is position of module i (0‑based)
        total = 0
        for u, v in edges:
            total += abs(perm[u] - perm[v])
            if total > B:
                break
        if total <= B:
            print("YES")
            print(' '.join(map(str, perm)))
            return
    print("NO")

if __name__ == "__main__":
    solve()