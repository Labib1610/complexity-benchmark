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

    color = [ -1 ] * (n + 1)          # 0 / 1 bipartite colors
    comp_nodes = []                  # list of lists of nodes per component
    comp_colors = []                 # parallel list of colors per node
    ok = True

    from collections import deque
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        q = deque([start])
        color[start] = 0
        nodes = []
        cols = []
        while q:
            v = q.popleft()
            nodes.append(v)
            cols.append(color[v])
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
        comp_nodes.append(nodes)
        comp_colors.append(cols)

    if not ok:
        print("NO")
        return

    # decide which color becomes price 1 in each component
    price = [2] * (n + 1)   # default 2
    for nodes, cols in zip(comp_nodes, comp_colors):
        # find minimal index node in this component
        min_node = min(nodes)
        min_color = color[min_node]
        # assign price 1 to all nodes with this color
        for v, c in zip(nodes, cols):
            if c == min_color:
                price[v] = 1
            else:
                price[v] = 2

    print("YES")
    print(' '.join(str(price[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()