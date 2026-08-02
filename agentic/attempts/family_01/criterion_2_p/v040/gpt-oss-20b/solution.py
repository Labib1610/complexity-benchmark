import sys
from collections import deque

def solve() -> None:
    input = sys.stdin.readline
    n_m = input().split()
    if not n_m:
        return
    n, m = map(int, n_m)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)  # 0 unvisited, 1 or 2 colored

    for start in range(1, n + 1):
        if color[start]:
            continue
        # BFS for component
        q = deque([start])
        color[start] = 1
        comp_nodes = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if not color[v]:
                    color[v] = 3 - cu
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
        # Ensure lexicographically smallest: make smallest index node color 1
        min_idx = min(comp_nodes)
        if color[min_idx] == 2:
            for node in comp_nodes:
                color[node] = 3 - color[node]

    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()