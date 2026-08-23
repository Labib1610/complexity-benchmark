import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u, v = data[idx], data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    res = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for component
        comp = []
        q = deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            comp.append(u)
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                elif color[v] == cu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return
        # orientation
        min_idx = min(comp)
        min_color = color[min_idx]
        if min_color == 0:
            mapping = (1, 2)  # 0->1, 1->2
        else:
            mapping = (2, 1)  # 0->2, 1->1
        for v in comp:
            res[v] = mapping[color[v]]

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, res[1:])))

if __name__ == "__main__":
    solve()