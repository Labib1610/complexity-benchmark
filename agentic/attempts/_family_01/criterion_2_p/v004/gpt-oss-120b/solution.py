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

    color = [-1] * n          # temporary 0/1 colors
    result = [0] * n          # final 1/2 values
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == cu:
                    print("NO")
                    return
        # decide flip based on smallest index vertex
        min_v = min(comp)
        if color[min_v] == 1:          # we want it to be 0 (=> shift 1)
            for v in comp:
                color[v] ^= 1
        # map to 1/2
        for v in comp:
            result[v] = 1 if color[v] == 0 else 2

    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()