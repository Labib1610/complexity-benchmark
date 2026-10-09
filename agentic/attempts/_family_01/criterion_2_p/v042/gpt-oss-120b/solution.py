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

    color = [-1] * (n + 1)          # 0 or 1
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
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
        # ensure the smallest index in component gets color 0 (=> vault 1)
        # start is the smallest because we iterate increasing and start uncolored
        if color[start] == 1:
            for v in comp:
                color[v] ^= 1

    # build answer
    ans = [str(color[i] + 1) for i in range(1, n + 1)]
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()