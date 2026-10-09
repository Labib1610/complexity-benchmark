import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    side = [-1] * n          # 0 / 1 inside component
    comp = [-1] * n          # component id
    comps = []               # list of vertex lists per component
    from collections import deque

    comp_cnt = 0
    for v in range(n):
        if side[v] != -1:
            continue
        q = deque([v])
        side[v] = 0
        comp[v] = comp_cnt
        verts = [v]
        ok = True
        while q:
            x = q.popleft()
            for y in adj[x]:
                if side[y] == -1:
                    side[y] = side[x] ^ 1
                    comp[y] = comp_cnt
                    q.append(y)
                    verts.append(y)
                elif side[y] == side[x]:
                    print("NO")
                    return
        comps.append(verts)
        comp_cnt += 1

    orientation = [None] * comp_cnt   # 0: side0->1, 1: side0->2
    ans = [0] * n

    for i in range(n):
        c = comp[i]
        if orientation[c] is None:
            # we want colour 1 for vertex i
            orientation[c] = 0 if side[i] == 0 else 1
        if orientation[c] == 0:
            ans[i] = 1 if side[i] == 0 else 2
        else:
            ans[i] = 2 if side[i] == 0 else 1

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()