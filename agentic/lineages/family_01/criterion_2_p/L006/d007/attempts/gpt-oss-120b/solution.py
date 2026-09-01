import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    col = [-1] * n          # 0 / 1
    from collections import deque
    for start in range(n):
        if col[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        col[start] = 0
        comp = [start]
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
        # make smallest index vertex colour 0 (=> mode 1)
        mn = min(comp)
        if col[mn] == 1:
            for v in comp:
                col[v] ^= 1

    # all good
    print("YES")
    ans = [str(c + 1) for c in col]
    print(' '.join(ans))

if __name__ == "__main__":
    solve()