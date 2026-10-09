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
        u = int(next(it))
        v = int(next(it))
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    col = [0] * (n + 1)          # 0 -> output 1, 1 -> output 2

    for i in range(1, n + 1):
        if not visited[i]:
            dq = deque([i])
            visited[i] = True
            col[i] = 0            # force smallest vertex to be 1
            while dq:
                v = dq.popleft()
                cv = col[v]
                for to in adj[v]:
                    if not visited[to]:
                        visited[to] = True
                        col[to] = cv ^ 1
                        dq.append(to)
                    elif col[to] == cv:
                        print("NO")
                        return

    # all good
    print("YES")
    out = ['1' if col[i] == 0 else '2' for i in range(1, n + 1)]
    print(' '.join(out))

if __name__ == "__main__":
    solve()