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
        # start new component, ensure start gets color 0 (type 1)
        q = deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                elif color[v] == cu:
                    print("NO")
                    return

    # construct answer: type 1 for color 0, type 2 for color 1
    ans = ['1' if color[i] == 0 else '2' for i in range(1, n + 1)]
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()