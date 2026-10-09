import sys
sys.setrecursionlimit(1 << 25)

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

    col = [-1] * (n + 1)          # 0 / 1 bipartite colour
    ans = [0] * (n + 1)           # final 1 / 2 values
    from collections import deque

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        col[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in g[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        # decide orientation: smallest index gets value 1
        root = min(comp)
        flip = (col[root] == 1)   # if root colour is 1 we need to flip
        for v in comp:
            if flip:
                ans[v] = 1 if col[v] == 1 else 2
            else:
                ans[v] = 1 if col[v] == 0 else 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()