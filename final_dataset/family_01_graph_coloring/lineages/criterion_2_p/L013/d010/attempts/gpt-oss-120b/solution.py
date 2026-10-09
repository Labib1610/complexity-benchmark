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

    color = [-1] * n          # 0 or 1
    answer = [0] * n
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
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide orientation for lexicographically smallest sequence
        min_idx = min(comp)
        # if min_idx currently has color 0, keep mapping 0->1,1->2
        # else swap
        if color[min_idx] == 0:
            for v in comp:
                answer[v] = 1 if color[v] == 0 else 2
        else:
            for v in comp:
                answer[v] = 1 if color[v] == 1 else 2

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()