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

    color = [-1] * (n + 1)          # 0 or 1 relative colors
    ans = [0] * (n + 1)             # final colors 1 or 2

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        comp = [start]
        bipartite = True
        while q:
            u = q.popleft()
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    q.append(w)
                    comp.append(w)
                elif color[w] == cu:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            print("NO")
            return

        min_node = min(comp)
        min_color = color[min_node]
        for node in comp:
            ans[node] = 1 if color[node] == min_color else 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()