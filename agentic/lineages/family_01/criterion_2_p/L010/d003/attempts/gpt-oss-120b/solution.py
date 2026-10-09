import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * (n + 1)          # temporary 0 / 1
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS of one component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif colour[v] == cu:
                    # not bipartite
                    sys.stdout.write("NO")
                    return
        # choose orientation: smallest index gets final colour 1
        min_vertex = min(comp)
        flip = colour[min_vertex]          # 0 -> keep, 1 -> swap
        for v in comp:
            answer[v] = (colour[v] ^ flip) + 1

    # all components processed successfully
    out = ["YES", " ".join(str(answer[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()