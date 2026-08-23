import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    color = [0] * (n + 1)  # provisional bipartite color 0/1
    result = [0] * (n + 1)  # final 1/2 assignment

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS for this component
        queue = deque([start])
        visited[start] = True
        color[start] = 0
        comp_nodes = [start]
        is_bipartite = True
        while queue:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = cu ^ 1
                    queue.append(v)
                    comp_nodes.append(v)
                else:
                    if color[v] == cu:
                        is_bipartite = False
                        break
            if not is_bipartite:
                break
        if not is_bipartite:
            print("NO")
            return
        # Determine orientation: make smallest node color 1
        # Smallest node in comp_nodes is start (since we iterate in order)
        if color[start] == 0:
            # map 0->1, 1->2
            for v in comp_nodes:
                result[v] = 1 if color[v] == 0 else 2
        else:
            # map 0->2, 1->1
            for v in comp_nodes:
                result[v] = 2 if color[v] == 0 else 1

    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()