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
    final = [0] * n           # 1 or 2
    for i in range(n):
        if color[i] != -1:
            continue
        # start new component
        comp_nodes = []
        q = deque([i])
        color[i] = 0
        comp_nodes.append(i)
        min_idx = i
        min_color = 0
        while q:
            u = q.popleft()
            if u < min_idx:
                min_idx = u
                min_color = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # mapping to make smallest index 1
        if min_color == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for u in comp_nodes:
            final[u] = map0 if color[u] == 0 else map1

    print("YES")
    print(' '.join(map(str, final)))

if __name__ == "__main__":
    solve()