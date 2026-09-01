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

    col = [-1] * (n + 1)          # temporary 0/1 colours
    ans = [0] * (n + 1)           # final powers 1/2

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        col[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            for w in adj[v]:
                if col[w] == -1:
                    col[w] = col[v] ^ 1
                    q.append(w)
                    comp.append(w)
                elif col[w] == col[v]:
                    print("NO")
                    return
        # decide orientation
        mn = min(comp)
        side0 = []
        side1 = []
        for v in comp:
            if col[v] == 0:
                side0.append(v)
            else:
                side1.append(v)
        if mn in side0:
            for v in side0:
                ans[v] = 1
            for v in side1:
                ans[v] = 2
        else:
            for v in side0:
                ans[v] = 2
            for v in side1:
                ans[v] = 1

    # all vertices coloured
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()