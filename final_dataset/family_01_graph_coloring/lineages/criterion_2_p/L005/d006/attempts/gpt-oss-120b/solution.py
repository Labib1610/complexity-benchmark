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

    col = [-1] * n          # temporary bipartite colour 0/1
    answer = [0] * n        # final values 1/2
    q = deque()

    for start in range(n):
        if col[start] != -1:
            continue
        # new component
        comp = []
        side0 = []
        side1 = []
        col[start] = 0
        q.append(start)
        while q:
            v = q.popleft()
            comp.append(v)
            if col[v] == 0:
                side0.append(v)
            else:
                side1.append(v)
            for to in adj[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        # decide which side gets value 1
        min_v = min(comp)
        if min_v in side0:
            for v in side0:
                answer[v] = 1
            for v in side1:
                answer[v] = 2
        else:
            for v in side1:
                answer[v] = 1
            for v in side0:
                answer[v] = 2

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()