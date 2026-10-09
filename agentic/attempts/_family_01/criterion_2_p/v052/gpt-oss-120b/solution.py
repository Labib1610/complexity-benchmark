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
        adj[u].append(v)
        adj[v].append(u)

    colour = [-1] * n          # -1 = unvisited, 0/1 = bipartite colour
    answer = [0] * n

    for start in range(n):
        if colour[start] != -1:
            continue

        # BFS for this component
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
                    print("NO")
                    return

        # orient component to make its smallest index vertex equal 1
        min_v = min(comp)
        if colour[min_v] == 0:
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 1 if colour[v] == 1 else 2

    print("YES")
    sys.stdout.write(' '.join(map(str, answer)) + '\n')


if __name__ == "__main__":
    solve()