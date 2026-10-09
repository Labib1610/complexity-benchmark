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

    comp = [0] * (n + 1)          # component id, 0 = unvisited
    col = [0] * (n + 1)           # 0 / 1 inside component
    verts = []                    # list of vertex lists per component
    from collections import deque

    comp_cnt = 0
    for start in range(1, n + 1):
        if comp[start]:
            continue
        comp_cnt += 1
        q = deque([start])
        comp[start] = comp_cnt
        col[start] = 0
        cur = []
        ok = True
        while q:
            v = q.popleft()
            cur.append(v)
            for to in adj[v]:
                if not comp[to]:
                    comp[to] = comp_cnt
                    col[to] = col[v] ^ 1
                    q.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        verts.append(cur)

    # orientation per component: 0 = as coloured, 1 = flipped
    orient = [-1] * (comp_cnt + 1)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        if ans[i]:
            continue
        cid = comp[i]
        # decide orientation using vertex i (the smallest index of this component)
        if col[i] == 0:
            o = 0          # colour 0 -> shift 1
        else:
            o = 1          # colour 1 -> shift 1
        orient[cid] = o
        # assign all vertices of this component
        for v in verts[cid - 1]:
            if o == 0:
                ans[v] = 1 if col[v] == 0 else 2
            else:
                ans[v] = 1 if col[v] == 1 else 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()