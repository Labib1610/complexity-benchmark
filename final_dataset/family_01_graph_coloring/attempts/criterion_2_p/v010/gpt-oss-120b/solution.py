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

    side = [-1] * (n + 1)          # 0 / 1 bipartite side
    comp_id = [-1] * (n + 1)       # component index
    comps = []                     # list of vertex lists per component

    for v in range(1, n + 1):
        if side[v] != -1:
            continue
        q = deque([v])
        side[v] = 0
        cur = []
        cid = len(comps)
        while q:
            u = q.popleft()
            comp_id[u] = cid
            cur.append(u)
            for w in adj[u]:
                if side[w] == -1:
                    side[w] = side[u] ^ 1
                    q.append(w)
                elif side[w] == side[u]:
                    print("NO")
                    return
        comps.append(cur)

    ans = [0] * (n + 1)
    used = [False] * len(comps)

    for i in range(1, n + 1):
        if ans[i]:
            continue
        cid = comp_id[i]
        if used[cid]:
            continue
        # orient component so that vertex i gets period 1
        if side[i] == 0:
            map0, map1 = 1, 2
        else:
            map0, map1 = 2, 1
        for v in comps[cid]:
            ans[v] = map0 if side[v] == 0 else map1
        used[cid] = True

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()