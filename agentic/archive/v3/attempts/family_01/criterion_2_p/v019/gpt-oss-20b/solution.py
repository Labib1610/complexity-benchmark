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

    color = [-1] * (n + 1)          # internal bipartite colors 0/1
    res = [0] * (n + 1)             # final colors 1/2

    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        # BFS to color component
        comp_nodes = []
        dq = deque([i])
        color[i] = 0
        comp_nodes.append(i)
        bipartite = True
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    comp_nodes.append(v)
                    dq.append(v)
                elif color[v] == cu:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            sys.stdout.write("NO")
            return
        # decide orientation: make first node i be color 1
        if color[i] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp_nodes:
            res[v] = map0 if color[v] == 0 else map1

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(res[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()