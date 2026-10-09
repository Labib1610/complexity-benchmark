import sys
import random

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    # Quick feasibility check
    # For each edge, min length is at least 1, if connected then at least 1.
    min_total = 0
    for u, v in edges:
        if u == v:
            continue
        min_total += 1
    if min_total > B:
        print("NO")
        return

    # Try many random permutations
    attempts = 2000
    for _ in range(attempts):
        perm = list(range(n))
        random.shuffle(perm)
        pos = [0] * n
        for i, node in enumerate(perm):
            pos[node] = i
        total = 0
        ok = True
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                ok = False
                break
        if ok:
            print("YES")
            print(" ".join(str(pos[i] + 1) for i in range(n)))
            return

    # Fallback: try greedy BFS / DFS layouts
    # Use degree ordering sometimes helps
    for start in range(n):
        order = [start]
        visited = [False]*n
        visited[start] = True
        # BFS
        q = [start]
        while q:
            node = q.pop(0)
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    order.append(nei)
                    q.append(nei)
        if len(order) < n:
            # disconnected graph, add remaining
            for i in range(n):
                if not visited[i]:
                    order.append(i)
        pos = [0]*n
        for i, node in enumerate(order):
            pos[node] = i
        total = 0
        ok = True
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                ok = False
                break
        if ok:
            print("YES")
            print(" ".join(str(pos[i] + 1) for i in range(n)))
            return

    # If all fails
    print("NO")

if __name__ == "__main__":
    solve()