import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    color = [ -1 ] * (n + 1)   # 0/1 parity
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation: smallest index gets shift 1
        min_v = min(comp)
        p = color[min_v]          # parity that should map to 1
        for v in comp:
            ans[v] = 1 if color[v] == p else 2

    print("YES")
    sys.stdout.write(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()