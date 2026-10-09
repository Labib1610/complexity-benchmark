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

    col = [-1] * (n + 1)          # provisional 0/1
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        col[start] = 0
        comp = [start]
        ok = True
        while q and ok:
            u = q.popleft()
            cu = col[u]
            for v in adj[u]:
                if col[v] == -1:
                    col[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif col[v] == cu:
                    ok = False
                    break
        if not ok:
            print("NO")
            return
        # decide mapping to 1/2
        smallest = min(comp)
        if col[smallest] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comp:
            ans[v] = map0 if col[v] == 0 else map1

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()