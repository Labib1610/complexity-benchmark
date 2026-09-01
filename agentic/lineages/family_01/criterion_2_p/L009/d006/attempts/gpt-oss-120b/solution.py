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

    col = [-1] * (n + 1)          # 0 or 1, -1 = unvisited
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        col[start] = 0
        comp = []
        while q:
            v = q.popleft()
            comp.append(v)
            for nb in adj[v]:
                if col[nb] == -1:
                    col[nb] = 1 - col[v]
                    q.append(nb)
                elif col[nb] == col[v]:
                    print("NO")
                    return
        # make smallest index vertex have colour 0 (value 1)
        minv = min(comp)
        if col[minv] == 1:
            for v in comp:
                col[v] ^= 1
        for v in comp:
            ans[v] = col[v] + 1   # 0->1, 1->2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()