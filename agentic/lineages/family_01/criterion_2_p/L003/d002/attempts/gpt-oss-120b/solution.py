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

    col = [0] * (n + 1)          # 0 = uncoloured, 1 or 2
    for start in range(1, n + 1):
        if col[start]:
            continue
        # start new component
        q = deque([start])
        col[start] = 1
        comp = []
        while q:
            v = q.popleft()
            comp.append(v)
            cv = col[v]
            for to in adj[v]:
                if col[to] == 0:
                    col[to] = 3 - cv
                    q.append(to)
                elif col[to] == cv:
                    print("NO")
                    return
        # choose orientation for lexicographically smallest result
        mn = min(comp)
        if col[mn] == 2:
            for v in comp:
                col[v] = 3 - col[v]

    # all good
    print("YES")
    out = ' '.join(str(col[i]) for i in range(1, n + 1))
    print(out)

if __name__ == "__main__":
    solve()