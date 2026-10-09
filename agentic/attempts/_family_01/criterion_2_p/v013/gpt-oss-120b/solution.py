import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    colour = [-1] * (n + 1)          # -1 = unvisited, else 0/1
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start is the smallest index of its component
        dq = deque([start])
        colour[start] = 0
        component_vertices = [start]

        while dq:
            v = dq.popleft()
            cv = colour[v]
            for to in g[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    dq.append(to)
                    component_vertices.append(to)
                elif colour[to] == cv:
                    sys.stdout.write("NO")
                    return

        # orientation already makes start -> colour 0 -> shift 1
        for v in component_vertices:
            answer[v] = colour[v] + 1

    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()