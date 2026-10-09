import sys
from collections import deque

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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = two sides
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start is the smallest vertex of its component
        colour[start] = 0
        q = deque([start])
        component = [start]
        while q:
            u = q.popleft()
            cu = colour[u]
            for w in adj[u]:
                if colour[w] == -1:
                    colour[w] = cu ^ 1
                    q.append(w)
                    component.append(w)
                elif colour[w] == cu:
                    sys.stdout.write("NO")
                    return
        # assign final values: colour 0 -> 1, colour 1 -> 2
        for v in component:
            answer[v] = 1 if colour[v] == 0 else 2

    # all vertices processed, graph is bipartite
    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()