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

    col = [-1] * (n + 1)          # temporary 0/1 colours
    answer = [0] * (n + 1)        # final values 1/2
    visited = [False] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        col[start] = 0
        visited[start] = True
        nodes0 = []
        nodes1 = []
        min_vertex = start
        min_colour = 0

        while q:
            v = q.popleft()
            if col[v] == 0:
                nodes0.append(v)
            else:
                nodes1.append(v)
            if v < min_vertex:
                min_vertex = v
                min_colour = col[v]
            for nb in adj[v]:
                if not visited[nb]:
                    visited[nb] = True
                    col[nb] = col[v] ^ 1
                    q.append(nb)
                else:
                    if col[nb] == col[v]:
                        print("NO")
                        return

        # decide orientation: make min_vertex value 1
        if min_colour == 0:
            for v in nodes0:
                answer[v] = 1
            for v in nodes1:
                answer[v] = 2
        else:
            for v in nodes0:
                answer[v] = 2
            for v in nodes1:
                answer[v] = 1

    # output
    print("YES")
    print(' '.join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()