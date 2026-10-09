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

    colour = [-1] * (n + 1)          # -1 = unvisited, 0/1 = bipartite colour
    answer = [0] * (n + 1)           # final s_i (1 or 2)

    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start a new component
        q = deque([start])
        colour[start] = 0
        comp_vertices = [start]
        ok = True
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp_vertices.append(to)
                elif colour[to] == cv:
                    # conflict -> not bipartite
                    print("NO")
                    return
        # choose mapping so that smallest index gets s=1
        min_v = min(comp_vertices)
        if colour[min_v] == 0:
            # colour 0 -> 1, colour 1 -> 2
            for v in comp_vertices:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            # swap
            for v in comp_vertices:
                answer[v] = 2 if colour[v] == 0 else 1

    # all components processed
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()