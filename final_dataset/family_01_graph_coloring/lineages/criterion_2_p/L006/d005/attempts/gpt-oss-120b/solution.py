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
        if u == v:          # loop makes condition impossible
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n          # 0 or 1
    for i in range(n):
        if color[i] != -1:
            continue
        # start new component, set i to color 0 to get lexicographically minimal
        dq = deque([i])
        color[i] = 0
        while dq:
            v = dq.popleft()
            cv = color[v]
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = cv ^ 1
                    dq.append(to)
                elif color[to] == cv:
                    print("NO")
                    return

    # construct answer: color 0 -> 1, color 1 -> 2
    ans = ['1' if c == 0 else '2' for c in color]
    print("YES")
    print(' '.join(ans))

if __name__ == "__main__":
    solve()