import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    it = 2
    for _ in range(m):
        u = data[it]; v = data[it + 1]; it += 2
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = two colours
    ans = [0] * (n + 1)             # final values 1 or 2

    stack = []
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # new component
        component = []
        min_v = start
        colour[start] = 0
        stack.append(start)

        while stack:
            v = stack.pop()
            component.append(v)
            if v < min_v:
                min_v = v
            cv = colour[v]
            for nb in adj[v]:
                if colour[nb] == -1:
                    colour[nb] = cv ^ 1
                    stack.append(nb)
                elif colour[nb] == cv:
                    sys.stdout.write("NO")
                    return

        flip = colour[min_v]          # 0 -> keep, 1 -> invert
        for v in component:
            final = colour[v] ^ flip
            ans[v] = 1 if final == 0 else 2

    # all vertices processed without conflict
    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()