import sys
from collections import deque

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

    colour = [-1] * (n + 1)          # 0 / 1
    answer = [0] * (n + 1)           # final values 1/2
    q = deque()

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # start new component
        colour[start] = 0
        q.append(start)
        comp = [start]
        min_vertex = start

        while q:
            v = q.popleft()
            for to in adj[v]:
                if colour[to] == -1:
                    colour[to] = colour[v] ^ 1
                    q.append(to)
                    comp.append(to)
                    if to < min_vertex:
                        min_vertex = to
                elif colour[to] == colour[v]:
                    print("NO")
                    return

        # decide orientation: smallest vertex must become 1
        if colour[min_vertex] == 0:
            # 0 -> 1, 1 -> 2
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            # swap
            for v in comp:
                answer[v] = 2 if colour[v] == 0 else 1

    # isolated vertices (no edges) are already handled: they form a component,
    # min_vertex gets colour 0, thus value 1.

    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()