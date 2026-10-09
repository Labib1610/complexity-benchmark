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
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # -1 = unvisited, else 0/1
    ans = [0] * (n + 1)

    for v in range(1, n + 1):
        if color[v] != -1:
            continue
        if not adj[v]:                     # isolated vertex
            ans[v] = 1
            color[v] = 0
            continue

        # new component, v is its smallest vertex
        q = deque([v])
        color[v] = 0
        comp = [v]
        ok = True
        while q:
            x = q.popleft()
            cx = color[x]
            for nb in adj[x]:
                if color[nb] == -1:
                    color[nb] = 1 - cx
                    q.append(nb)
                    comp.append(nb)
                elif color[nb] == cx:
                    print("NO")
                    return
        # assign modes: colour of v gets 1
        col_one = color[v]
        for u in comp:
            ans[u] = 1 if color[u] == col_one else 2

    # all components processed without conflict
    print("YES")
    sys.stdout.write(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()