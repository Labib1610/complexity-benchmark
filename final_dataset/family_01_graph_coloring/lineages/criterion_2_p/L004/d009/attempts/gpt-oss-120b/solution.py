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

    if m == 0:
        # all 1s is lexicographically smallest
        print("YES")
        print(" ".join(["1"] * n))
        return

    visited = [False] * (n + 1)
    colour = [-1] * (n + 1)          # 0 or 1
    answer = [0] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        visited[start] = True
        colour[start] = 0
        comp = [start]
        min_vertex = start

        while q:
            v = q.popleft()
            if v < min_vertex:
                min_vertex = v
            for to in adj[v]:
                if not visited[to]:
                    visited[to] = True
                    colour[to] = colour[v] ^ 1
                    q.append(to)
                    comp.append(to)
                else:
                    if colour[to] == colour[v]:
                        print("NO")
                        return

        # decide mapping so that min_vertex gets value 1
        if colour[min_vertex] == 0:
            # 0 -> 1, 1 -> 2
            for x in comp:
                answer[x] = 1 if colour[x] == 0 else 2
        else:
            # flip
            for x in comp:
                answer[x] = 2 if colour[x] == 0 else 1

    print("YES")
    print(" ".join(str(answer[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()