import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n          # 0 or 1
    res = [0] * n             # final 1 or 2

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS for component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif cv == cu:
                    print("NO")
                    return
        # determine mapping so that smallest node gets 1
        min_node = min(comp_nodes)
        min_color = color[min_node]
        # mapping: if min_color==0 -> 0->1,1->2 else swap
        if min_color == 0:
            for u in comp_nodes:
                res[u] = 1 if color[u] == 0 else 2
        else:
            for u in comp_nodes:
                res[u] = 1 if color[u] == 1 else 2

    print("YES")
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()