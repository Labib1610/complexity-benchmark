import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * n          # -1 = unvisited, 0/1 = colour
    chosen = []                # vertices of the larger colour class of each component

    for start in range(n):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        part = [[], []]        # vertices of colour 0 and 1
        part[0].append(start)
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    part[colour[to]].append(to)
                    q.append(to)
        # take the larger side
        if len(part[0]) >= len(part[1]):
            chosen.extend(part[0])
        else:
            chosen.extend(part[1])

    if len(chosen) < k:
        sys.stdout.write("NO")
    else:
        sys.stdout.write("YES\n")
        out = [str(v + 1) for v in chosen[:k]]
        sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    solve()