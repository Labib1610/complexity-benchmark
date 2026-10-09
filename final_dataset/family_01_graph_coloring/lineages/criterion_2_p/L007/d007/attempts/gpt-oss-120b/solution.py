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
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    col = [0] * (n + 1)          # 0 -> basis 1, 1 -> basis 2

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # start BFS from the smallest vertex of this component
        dq = deque([start])
        visited[start] = True
        col[start] = 0            # basis 1 for the smallest vertex
        while dq:
            u = dq.popleft()
            cu = col[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    col[v] = cu ^ 1
                    dq.append(v)
                elif col[v] == cu:
                    # same colour on an edge -> not bipartite
                    sys.stdout.write("NO")
                    return

    # all edges satisfied, output lexicographically smallest colouring
    out = ["YES\n"]
    out.append(' '.join(str(col[i] + 1) for i in range(1, n + 1)))
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()