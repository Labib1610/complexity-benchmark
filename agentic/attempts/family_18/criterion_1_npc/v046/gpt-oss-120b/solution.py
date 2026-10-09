import sys, itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        edges.append((x, y))
        adj[x].append(y)
        adj[y].append(x)

    # brute force all permutations (feasible for small n)
    for perm in itertools.permutations(range(n)):
        pos = [0] * n
        for idx, node in enumerate(perm):
            pos[node] = idx + 1  # positions are 1‑based
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                break
        if total <= B:
            # output positions per module (1‑based)
            ans = [str(pos[i]) for i in range(n)]
            sys.stdout.write("YES\n" + " ".join(ans))
            return
    sys.stdout.write("NO")

if __name__ == "__main__":
    solve()