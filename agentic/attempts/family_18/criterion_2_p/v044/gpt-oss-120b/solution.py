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
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))

    # If n is small, brute‑force all permutations
    if n <= 10:
        nodes = list(range(n))
        for perm in itertools.permutations(nodes):
            pos = [0] * n
            for slot, node in enumerate(perm):
                pos[node] = slot  # 0‑based positions
            total = 0
            for u, v in edges:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
            if total <= B:
                # output 1‑based slot numbers for modules 1..n
                ans = [pos[i] + 1 for i in range(n)]
                sys.stdout.write("YES\n")
                sys.stdout.write(" ".join(map(str, ans)))
                return
        sys.stdout.write("NO")
        return

    # For larger n use a simple heuristic: place nodes by a DFS order
    sys.setrecursionlimit(10**6)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    order = []
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)

    pos = [0] * n
    for slot, node in enumerate(order):
        pos[node] = slot

    total = sum(abs(pos[u] - pos[v]) for u, v in edges)
    if total <= B:
        ans = [pos[i] + 1 for i in range(n)]
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, ans)))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()