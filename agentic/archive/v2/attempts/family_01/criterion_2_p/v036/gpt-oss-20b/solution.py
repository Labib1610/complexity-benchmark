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

    color = [-1] * (n + 1)   # -1 unvisited, 0/1 colors
    ans = [0] * n

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS component
        queue = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while queue and ok:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    queue.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    ok = False
                    break
        if not ok:
            print("NO")
            return

        comp_nodes.sort()
        list_a = [1 if color[v] == 0 else 2 for v in comp_nodes]
        list_b = [2 if color[v] == 0 else 1 for v in comp_nodes]
        if list_a < list_b:
            for v, val in zip(comp_nodes, list_a):
                ans[v - 1] = val
        else:
            for v, val in zip(comp_nodes, list_b):
                ans[v - 1] = val

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()