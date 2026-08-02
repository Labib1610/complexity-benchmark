import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    color = [-1] * n          # 0 or 1 during DFS
    ans = [0] * n             # final vault numbers (1 or 2)
    stack = []

    for start in range(n):
        if color[start] != -1:
            continue
        # new component
        comp_nodes = []
        stack.append(start)
        color[start] = 0
        comp_nodes.append(start)
        is_bipartite = True
        while stack:
            u = stack.pop()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                    comp_nodes.append(v)
                elif color[v] == cu:
                    is_bipartite = False
                    break
            if not is_bipartite:
                break
        if not is_bipartite:
            print("NO")
            return
        # determine orientation
        min_node = min(comp_nodes)
        min_color = color[min_node]
        # mapping: if min_color==0 -> color0->1, color1->2
        # else -> color0->2, color1->1
        if min_color == 0:
            for v in comp_nodes:
                ans[v] = 1 if color[v] == 0 else 2
        else:
            for v in comp_nodes:
                ans[v] = 2 if color[v] == 0 else 1

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()