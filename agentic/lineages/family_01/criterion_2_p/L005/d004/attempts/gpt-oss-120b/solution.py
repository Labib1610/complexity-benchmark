import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    comp_id = [-1] * n          # component number
    col = [-1] * n              # 0 / 1 inside component
    components = []              # list of vertex lists per component
    ok = True

    for start in range(n):
        if comp_id[start] != -1:
            continue
        # new component
        cid = len(components)
        q = deque([start])
        comp_id[start] = cid
        col[start] = 0
        verts = [start]

        while q and ok:
            v = q.popleft()
            cv = col[v]
            for nb in adj[v]:
                if comp_id[nb] == -1:
                    comp_id[nb] = cid
                    col[nb] = cv ^ 1
                    q.append(nb)
                    verts.append(nb)
                else:
                    if col[nb] == cv:
                        ok = False
                        break
        if not ok:
            break
        components.append(verts)

    if not ok:
        sys.stdout.write("NO")
        return

    # orientation[c] = colour (0/1) that gets power 1
    orientation = [-1] * len(components)
    ans = [0] * n

    for i in range(n):
        cid = comp_id[i]
        if orientation[cid] == -1:
            orientation[cid] = col[i]          # give this vertex power 1
        ans[i] = 1 if col[i] == orientation[cid] else 2

    out = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()