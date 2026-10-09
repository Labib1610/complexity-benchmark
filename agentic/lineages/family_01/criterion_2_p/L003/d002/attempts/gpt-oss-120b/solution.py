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

    visited = [False] * (n + 1)
    colour = [0] * (n + 1)          # temporary 0/1
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        visited[start] = True
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = colour[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    colour[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif colour[v] == cu:
                    # not bipartite
                    print("NO")
                    return
        # orient to make smallest index vertex get value 1
        if colour[start] == 0:
            for v in comp:
                answer[v] = 1 if colour[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 2 if colour[v] == 0 else 1

    # all components processed
    print("YES")
    sys.stdout.write(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()