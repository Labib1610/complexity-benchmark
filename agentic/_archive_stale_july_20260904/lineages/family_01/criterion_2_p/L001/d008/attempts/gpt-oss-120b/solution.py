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
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # 0 / 1 bipartite colors
    comp_id = [-1] * (n + 1)
    comps = []                      # list of (nodes list, min_node)
    q = deque()
    cid = 0
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q.append(start)
        color[start] = 0
        comp_nodes = []
        min_node = start
        while q:
            v = q.popleft()
            comp_nodes.append(v)
            if v < min_node:
                min_node = v
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return
        comps.append((comp_nodes, min_node))
        cid += 1

    # decide final values (1 or 2) for each bipartite side
    res = [0] * (n + 1)
    for nodes, min_node in comps:
        # which side gets value 1 ?
        # we want the smallest index node in this component to be 1
        if color[min_node] == 0:
            side_one = 0
        else:
            side_one = 1
        for v in nodes:
            res[v] = 1 if color[v] == side_one else 2

    print("YES")
    print(' '.join(str(res[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()