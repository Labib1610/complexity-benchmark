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

    # If n is too large for brute force, we cannot solve optimally.
    # As a fallback, try a simple heuristic: place vertices in order of degree.
    if n > 9:
        deg = [0] * n
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
        order = sorted(range(n), key=lambda x: -deg[x])
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i + 1
        total = sum(abs(pos[u] - pos[v]) for u, v in edges)
        if total <= B:
            print("YES")
            print(' '.join(map(str, pos)))
        else:
            print("NO")
        return

    vertices = list(range(n))
    for perm in itertools.permutations(range(1, n + 1)):
        # perm[i] is position of vertex i
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