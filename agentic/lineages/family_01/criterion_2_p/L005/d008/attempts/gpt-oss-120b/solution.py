import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    color = [-1] * n          # 0 or 1 for bipartition
    answer = [0] * n          # final values 1 or 2
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = color[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return
        # decide which side gets value 1
        min_vertex = min(comp)
        # if min_vertex currently has color 0, keep mapping 0->1,1->2 else swap
        if color[min_vertex] == 0:
            for v in comp:
                answer[v] = 1 if color[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 1 if color[v] == 1 else 2

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()