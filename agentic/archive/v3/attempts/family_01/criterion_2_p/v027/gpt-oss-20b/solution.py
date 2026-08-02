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

    color = [-1] * (n + 1)
    s = [0] * (n + 1)
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        bipartite = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            print("NO")
            return
        # determine orientation
        min_node = min(comp_nodes)
        if color[min_node] == 0:
            # original: 0->1, 1->2
            for node in comp_nodes:
                s[node] = 1 if color[node] == 0 else 2
        else:
            # flipped: 0->2, 1->1
            for node in comp_nodes:
                s[node] = 2 if color[node] == 0 else 1

    print("YES")
    print(' '.join(str(s[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()