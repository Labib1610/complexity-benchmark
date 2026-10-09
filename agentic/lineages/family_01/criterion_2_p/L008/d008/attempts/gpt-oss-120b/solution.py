import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:                     # self‑loop → impossible
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * n          # -1 = unvisited, 0/1 = bipartite colour
    answer = [1] * n           # default 1 (isolated vertices stay 1)

    for start in range(n):
        if colour[start] != -1 or not adj[start]:
            continue            # already processed or isolated
        q = deque([start])
        colour[start] = 0
        component = [start]

        while q:
            v = q.popleft()
            cv = colour[v]
            for nb in adj[v]:
                if colour[nb] == -1:
                    colour[nb] = cv ^ 1
                    q.append(nb)
                    component.append(nb)
                elif colour[nb] == cv:
                    print("NO")
                    return

        # make the smallest index of the component have c = 1
        min_vertex = min(component)
        flip = colour[min_vertex]          # 0 → keep, 1 → swap sides
        for v in component:
            answer[v] = (colour[v] ^ flip) + 1   # 0→1, 1→2 after possible flip

    print("YES")
    sys.stdout.write(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()