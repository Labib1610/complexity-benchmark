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

    color = [-1] * (n + 1)          # 0 or 1
    shift = [0] * (n + 1)           # final answer (1 or 2)
    visited = [False] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS to check bipartite and collect component
        comp = []
        q = deque([start])
        visited[start] = True
        color[start] = 0
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = color[u] ^ 1
                    q.append(v)
                else:
                    if color[v] == color[u]:
                        print("NO")
                        return
        # determine orientation: smallest index gets shift 1
        min_idx = min(comp)
        if color[min_idx] == 1:
            # flip colors
            for v in comp:
                shift[v] = 2 if color[v] == 1 else 1
        else:
            for v in comp:
                shift[v] = 1 if color[v] == 0 else 2

    print("YES")
    print(' '.join(str(shift[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()