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

    col = [-1] * (n + 1)          # -1 unvisited, else 0/1
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS for this component
        q = deque([start])
        col[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for nb in adj[v]:
                if col[nb] == -1:
                    col[nb] = col[v] ^ 1
                    q.append(nb)
                    comp.append(nb)
                elif col[nb] == col[v]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print("NO")
            return

        # decide orientation: smallest index gets value 1
        v_min = min(comp)
        side_one = col[v_min]          # colour that will become 1
        for v in comp:
            ans[v] = 1 if col[v] == side_one else 2

    # all components processed
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()