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

    color = [ -1 ] * (n + 1)          # bipartite color 0/1
    ans = [0] * (n + 1)               # final clearance 1/2
    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start a new component
        q = deque([start])
        color[start] = 0
        comp_nodes = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # choose mapping so that smallest index gets clearance 1
        min_node = min(comp_nodes)
        if not g[min_node]:          # isolated vertex, no constraints
            ans[min_node] = 1
            continue
        # if min_node has color 0, map 0->1,1->2 else reverse
        if color[min_node] == 0:
            map01 = (1, 2)
        else:
            map01 = (2, 1)
        for v in comp_nodes:
            ans[v] = map01[color[v]]
    # any remaining isolated vertices not processed (they have no edges and were not in any component loop)
    for i in range(1, n + 1):
        if ans[i] == 0:
            ans[i] = 1
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()