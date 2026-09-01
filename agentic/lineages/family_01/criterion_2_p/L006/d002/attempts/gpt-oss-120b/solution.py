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

    col = [-1] * n            # provisional colour 0/1
    comp = [-1] * n           # component id
    comp_cnt = 0

    # BFS for bipartiteness and colouring
    for start in range(n):
        if col[start] != -1:
            continue
        dq = deque([start])
        col[start] = 0
        comp[start] = comp_cnt
        while dq:
            u = dq.popleft()
            cu = col[u]
            for w in adj[u]:
                if col[w] == -1:
                    col[w] = 1 - cu
                    comp[w] = comp_cnt
                    dq.append(w)
                elif col[w] == cu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return
        comp_cnt += 1

    orientation = [-1] * comp_cnt   # which colour (0/1) becomes pressure 1
    ans = [0] * n

    for i in range(n):
        cid = comp[i]
        if orientation[cid] == -1:
            orientation[cid] = col[i]          # make this colour = 1
        ans[i] = 1 if col[i] == orientation[cid] else 2

    out = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()