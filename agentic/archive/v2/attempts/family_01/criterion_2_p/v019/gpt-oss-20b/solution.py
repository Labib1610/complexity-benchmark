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

    color = [-1] * (n + 1)  # -1 unvisited, 0 or 1 bipartite color
    result = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS to check bipartite and collect component
        q = deque([start])
        comp_nodes = []
        color[start] = 0
        comp_nodes.append(start)
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # Determine orientation for lexicographic minimality
        min_node = min(comp_nodes)
        min_side = color[min_node]
        # side_to_color: 0->1 if min_side==0 else 0->2
        if min_side == 0:
            side0 = 1
            side1 = 2
        else:
            side0 = 2
            side1 = 1
        for v in comp_nodes:
            result[v] = side0 if color[v] == 0 else side1

    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()