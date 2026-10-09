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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = colour
    answer = [0] * (n + 1)

    stack = []
    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # new component, start is its smallest vertex
        colour[start] = 0
        stack.append(start)
        component = [start]

        while stack:
            v = stack.pop()
            cv = colour[v]
            for nb in adj[v]:
                if colour[nb] == -1:
                    colour[nb] = cv ^ 1
                    stack.append(nb)
                    component.append(nb)
                elif colour[nb] == cv:
                    sys.stdout.write("NO")
                    return

        flip = colour[start]          # make start (the smallest) colour 0
        for v in component:
            answer[v] = (colour[v] ^ flip) + 1   # 0->1 , 1->2

    out = ["YES\n", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()