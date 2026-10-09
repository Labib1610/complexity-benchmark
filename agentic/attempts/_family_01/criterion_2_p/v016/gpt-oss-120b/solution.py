import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    colour = [-1] * (n + 1)          # -1 = unvisited, 0 / 1 = bfs colours
    answer = [0] * (n + 1)           # final modes 1 / 2

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue

        # BFS of one component
        q = deque([start])
        colour[start] = 0
        component = [start]

        while q:
            u = q.popleft()
            cu = colour[u]
            for v in g[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)
                    component.append(v)
                elif colour[v] == cu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return

        # orient component so that its smallest vertex gets mode 1
        p = min(component)                 # smallest index in this component
        flip = (colour[p] == 1)             # need to swap colours?
        if not flip:
            for v in component:
                answer[v] = 1 + colour[v]   # 0->1, 1->2
        else:
            for v in component:
                answer[v] = 2 - colour[v]   # 0->2, 1->1

    # all components processed successfully
    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()