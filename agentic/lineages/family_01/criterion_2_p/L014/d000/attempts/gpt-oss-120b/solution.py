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

    color = [-1] * n          # provisional 0/1
    answer = [0] * n          # final 1/2

    for start in range(n):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            cv = color[v]
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                elif color[to] == cv:
                    print("NO")
                    return
        # decide orientation to make smallest index node = 1
        min_node = min(comp)
        flip = color[min_node] == 1
        for node in comp:
            c = color[node] ^ (1 if flip else 0)
            answer[node] = 1 if c == 0 else 2

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()