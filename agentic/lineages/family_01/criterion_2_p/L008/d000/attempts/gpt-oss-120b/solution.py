import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    colour = [-1] * (n + 1)          # 0 / 1
    comp_id = [-1] * (n + 1)
    comps = []                         # each: (vertices list)

    from collections import deque
    ok = True
    cid = 0
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        q = deque([start])
        colour[start] = 0
        verts = []
        comp_id[start] = cid
        while q:
            v = q.popleft()
            verts.append(v)
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    comp_id[to] = cid
                    q.append(to)
                elif colour[to] == colour[v]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
        comps.append(verts)
        cid += 1

    if not ok:
        sys.stdout.write("NO")
        return

    answer = [0] * (n + 1)
    oriented = [False] * cid

    for i in range(1, n + 1):
        if answer[i]:
            continue
        c = comp_id[i]
        # decide orientation so that i gets shift 1
        if colour[i] == 0:
            orient = 0          # colour 0 -> 1
        else:
            orient = 1          # colour 1 -> 1
        oriented[c] = True
        for v in comps[c]:
            if orient == 0:
                answer[v] = 1 if colour[v] == 0 else 2
            else:
                answer[v] = 1 if colour[v] == 1 else 2

    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()