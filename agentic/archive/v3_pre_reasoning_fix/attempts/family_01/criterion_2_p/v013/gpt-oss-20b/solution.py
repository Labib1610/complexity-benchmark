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
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)   # 0 or 1
    ans = [0] * (n + 1)      # 1 or 2

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS for this component
        comp_nodes = []
        q = deque([start])
        color[start] = 0
        comp_nodes.append(start)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # Decide flip based on smallest index
        min_idx = min(comp_nodes)
        flip = 0 if color[min_idx] == 0 else 1
        for node in comp_nodes:
            ans[node] = (color[node] ^ flip) + 1

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()