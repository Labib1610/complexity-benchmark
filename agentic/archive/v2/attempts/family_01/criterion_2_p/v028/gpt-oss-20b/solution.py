import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
    color = [0] * (n + 1)          # 0 or 1
    result = [0] * (n + 1)         # final channels 1 or 2

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS for this component
        q = deque([start])
        visited[start] = True
        color[start] = 0
        component_nodes = [start]
        is_bipartite = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = cu ^ 1
                    q.append(v)
                    component_nodes.append(v)
                else:
                    if color[v] == cu:
                        is_bipartite = False
                        break
            if not is_bipartite:
                break
        if not is_bipartite:
            print("NO")
            return

        # Ensure lexicographically smallest: make the smallest index node 1
        min_node = min(component_nodes)
        if color[min_node] == 1:   # currently would give channel 2
            # flip entire component
            for v in component_nodes:
                color[v] ^= 1

        # set result channels
        for v in component_nodes:
            result[v] = color[v] + 1   # 0->1, 1->2

    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()