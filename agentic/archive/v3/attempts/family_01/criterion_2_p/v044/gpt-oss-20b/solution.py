import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # 0 or 1
    comp_id = [0] * (n + 1)
    comp_min = []                   # min vertex index per component
    bipartite = True
    comp_cnt = 0

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # new component
        q = deque([start])
        color[start] = 0
        comp_id[start] = comp_cnt
        min_idx = start
        while q:
            u = q.popleft()
            if u < min_idx:
                min_idx = u
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    comp_id[v] = comp_cnt
                    q.append(v)
                else:
                    if color[v] == cu:
                        bipartite = False
                        break
            if not bipartite:
                break
        if not bipartite:
            break
        comp_min.append(min_idx)
        comp_cnt += 1

    if not bipartite:
        sys.stdout.write("NO\n")
        return

    # Determine flip for each component
    flip = [0] * comp_cnt
    for cid, minv in enumerate(comp_min):
        if color[minv] == 1:
            flip[cid] = 1

    out = []
    for i in range(1, n + 1):
        final_color = color[i] ^ flip[comp_id[i]]
        out.append(str(final_color + 1))  # 0->1, 1->2

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(out) + "\n")

if __name__ == "__main__":
    solve()