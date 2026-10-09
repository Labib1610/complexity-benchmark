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

    color = [-1] * (n + 1)          # 0 or 1 for bipartition
    ans = [0] * (n + 1)             # final values 1 or 2

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        min_node = start
        while q:
            u = q.popleft()
            if u < min_node:
                min_node = u
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation: node with smallest index gets value 1
        if color[min_node] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp_nodes:
            ans[v] = map0 if color[v] == 0 else map1

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()