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

    comp = [0] * (n + 1)          # component id
    color = [0] * (n + 1)         # bipartite color 0/1
    comp_vertices = []           # list of vertices per component
    comp_cnt = 0
    from collections import deque

    for v in range(1, n + 1):
        if comp[v]:
            continue
        comp_cnt += 1
        q = deque([v])
        comp[v] = comp_cnt
        color[v] = 0
        cur = [v]
        ok = True
        while q:
            x = q.popleft()
            for nb in adj[x]:
                if not comp[nb]:
                    comp[nb] = comp_cnt
                    color[nb] = color[x] ^ 1
                    q.append(nb)
                    cur.append(nb)
                elif color[nb] == color[x]:
                    print("NO")
                    return
        comp_vertices.append(cur)

    # orientation: for each component, -1 not set, else mapping of color0 -> shift (1 or 2)
    orient = [-1] * (comp_cnt + 1)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        cid = comp[i]
        if orient[cid] == -1:
            # set orientation so that vertex i gets shift 1
            if color[i] == 0:
                orient[cid] = 1   # color0 -> 1, color1 -> 2
            else:
                orient[cid] = 2   # color0 -> 2, color1 -> 1
        # assign shift
        if color[i] == 0:
            ans[i] = orient[cid]
        else:
            ans[i] = 3 - orient[cid]   # opposite shift (1<->2)

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()