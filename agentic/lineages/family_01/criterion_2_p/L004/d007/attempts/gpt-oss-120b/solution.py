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
    for i in range(n):
        if color[i] != -1:
            continue
        # BFS this component
        q = deque([i])
        color[i] = 0
        comp = [i]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide flip to make smallest index = 1
        min_idx = min(comp)
        if color[min_idx] == 1:          # currently 1, need flip
            for v in comp:
                color[v] ^= 1

    # all components bipartite
    print("YES")
    # map 0->1, 1->2
    res = ['1' if c == 0 else '2' for c in color]
    print(' '.join(res))

if __name__ == "__main__":
    solve()