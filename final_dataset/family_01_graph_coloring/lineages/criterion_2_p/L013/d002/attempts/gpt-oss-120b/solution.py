import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    colour = [-1] * (n + 1)          # -1 unvisited, 0/1 bipartite colours
    ans = [0] * (n + 1)

    stack = []
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # new component
        component = []
        min_vertex = start
        colour[start] = 0
        stack.append(start)

        while stack:
            x = stack.pop()
            component.append(x)
            if x < min_vertex:
                min_vertex = x
            cx = colour[x]
            for y in adj[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    stack.append(y)
                elif colour[y] == cx:
                    sys.stdout.write("NO")
                    return

        side_of_min = colour[min_vertex]
        for v in component:
            ans[v] = 1 if colour[v] == side_of_min else 2

    out = ["YES\n", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()