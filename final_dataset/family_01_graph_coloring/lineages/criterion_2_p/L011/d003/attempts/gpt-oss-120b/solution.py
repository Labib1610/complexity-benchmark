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

    colour = [-1] * (n + 1)          # -1 = unvisited, else 0/1
    comp_id = -1
    comp_vertices = []               # list of lists
    comp_min = []                    # smallest vertex per component

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        comp_id += 1
        q = deque([start])
        colour[start] = 0
        cur_vertices = []
        cur_min = start

        while q:
            x = q.popleft()
            cur_vertices.append(x)
            if x < cur_min:
                cur_min = x
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = colour[x] ^ 1
                    q.append(y)
                elif colour[y] == colour[x]:
                    print("NO")
                    return
        comp_vertices.append(cur_vertices)
        comp_min.append(cur_min)

    # build answer
    ans = [0] * (n + 1)
    for cid, verts in enumerate(comp_vertices):
        p = comp_min[cid]
        col_of_p = colour[p]
        for v in verts:
            ans[v] = 1 if colour[v] == col_of_p else 2

    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()