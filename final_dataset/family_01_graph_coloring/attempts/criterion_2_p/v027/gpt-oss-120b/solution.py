import sys
sys.setrecursionlimit(1 << 25)

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

    color = [-1] * (n + 1)          # 0 or 1
    ans = [0] * (n + 1)             # final bands 1/2
    stack = []
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # new component
        comp_nodes = []
        min_node = start
        color[start] = 0
        stack.append(start)
        ok = True
        while stack:
            u = stack.pop()
            comp_nodes.append(u)
            if u < min_node:
                min_node = u
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
        # decide orientation: make min_node have band 1
        if color[min_node] == 0:
            # 0 -> 1, 1 -> 2
            for v in comp_nodes:
                ans[v] = 1 if color[v] == 0 else 2
        else:
            # swap
            for v in comp_nodes:
                ans[v] = 1 if color[v] == 1 else 2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()