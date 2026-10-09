import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    color = [ -1 ] * (n + 1)          # 0 / 1 parity for bipartite check
    comp_id = [ -1 ] * (n + 1)
    comps = []                        # list of nodes per component
    ok = True

    from collections import deque
    cid = 0
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # new component
        q = deque([start])
        color[start] = 0
        comp_nodes = []
        while q:
            v = q.popleft()
            comp_nodes.append(v)
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                elif color[to] == color[v]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
        for v in comp_nodes:
            comp_id[v] = cid
        comps.append(comp_nodes)
        cid += 1

    if not ok:
        print("NO")
        return

    # Build answer with lexicographically smallest assignment
    ans = [0] * (n + 1)
    for nodes in comps:
        # find smallest index in this component
        min_node = min(nodes)
        # parity of that node decides mapping
        if color[min_node] == 0:
            # parity 0 -> grade 1, parity 1 -> grade 2
            for v in nodes:
                ans[v] = 1 if color[v] == 0 else 2
        else:
            # swap
            for v in nodes:
                ans[v] = 2 if color[v] == 0 else 1

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()