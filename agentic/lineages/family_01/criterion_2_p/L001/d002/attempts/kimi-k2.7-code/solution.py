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
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)  # 0 = unvisited, 1/2 = hall

    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        stack = [i]
        color[i] = 1
        while stack:
            v = stack.pop()
            cv = color[v]
            opp = 3 - cv
            for to in adj[v]:
                ct = color[to]
                if ct == 0:
                    color[to] = opp
                    stack.append(to)
                elif ct == cv:
                    sys.stdout.write("NO")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color[1:])))

solve()