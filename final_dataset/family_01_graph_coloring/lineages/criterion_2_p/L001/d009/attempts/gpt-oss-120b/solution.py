import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    comp = [-1] * (n + 1)          # component id of each vertex
    colour = [0] * (n + 1)        # base colour 0 / 1
    min_node_of_comp = []         # smallest index in each component
    cid = 0
    ok = True

    for start in range(1, n + 1):
        if comp[start] != -1:
            continue
        # BFS of a new component
        q = deque([start])
        comp[start] = cid
        colour[start] = 0
        cur_min = start

        while q and ok:
            v = q.popleft()
            if v < cur_min:
                cur_min = v
            cv = colour[v]
            for nb in adj[v]:
                if comp[nb] == -1:
                    comp[nb] = cid
                    colour[nb] = cv ^ 1
                    q.append(nb)
                else:
                    # edge inside component, must connect different colours
                    if colour[nb] == cv:
                        ok = False
                        break
        if not ok:
            break
        min_node_of_comp.append(cur_min)
        cid += 1

    if not ok:
        sys.stdout.write("NO")
        return

    # decide orientation: flip if smallest vertex has colour 1
    flip = [0] * cid
    for c in range(cid):
        flip[c] = colour[min_node_of_comp[c]]   # 0 -> keep, 1 -> flip

    ans = [0] * (n + 1)
    for v in range(1, n + 1):
        effective = colour[v] ^ flip[comp[v]]
        ans[v] = 1 if effective == 0 else 2

    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()