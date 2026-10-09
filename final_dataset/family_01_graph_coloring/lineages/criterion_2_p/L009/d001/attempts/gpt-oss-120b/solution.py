import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        g[u].append(v)
        g[v].append(u)

    color = [-1] * n          # 0 or 1
    comp_nodes = []           # list of nodes per component
    ok = True

    from collections import deque
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        nodes = [start]
        while q:
            v = q.popleft()
            for to in g[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    nodes.append(to)
                elif color[to] == color[v]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
        comp_nodes.append(nodes)

    if not ok:
        print("NO")
        return

    # Build answer with lexicographically smallest assignment
    ans = [0] * n
    for nodes in comp_nodes:
        # find smallest index in this component
        min_node = min(nodes)
        # if min_node currently has color 0, we map color0->1, else flip
        flip = (color[min_node] == 1)
        for v in nodes:
            c = color[v] ^ flip
            ans[v] = 1 if c == 0 else 2

    # isolated vertices not visited? they are in comp_nodes as singletons already
    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()