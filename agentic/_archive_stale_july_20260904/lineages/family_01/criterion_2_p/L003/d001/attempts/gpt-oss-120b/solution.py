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

    color = [-1] * (n + 1)          # 0 or 1
    result = [0] * (n + 1)          # final 1/2 values
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        min_node = start
        while q:
            u = q.popleft()
            if u < min_node:
                min_node = u
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation: make min_node have value 1 (color 0)
        if color[min_node] == 1:
            # flip colors in this component
            for v in comp:
                color[v] ^= 1
        # map to 1/2
        for v in comp:
            result[v] = 1 if color[v] == 0 else 2

    print("YES")
    print(' '.join(str(result[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()