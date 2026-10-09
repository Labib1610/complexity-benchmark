import sys
sys.setrecursionlimit(1 << 25)

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

    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return

    col = [-1] * (n + 1)          # temporary colours 0/1
    ans = [0] * (n + 1)

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
            for to in adj[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        # decide orientation: make start (the smallest vertex of this component) colour 1
        if col[start] == 0:
            for v in comp:
                ans[v] = 1 if col[v] == 0 else 2
        else:
            for v in comp:
                ans[v] = 2 if col[v] == 0 else 1

    print("YES")
    print(" ".join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()