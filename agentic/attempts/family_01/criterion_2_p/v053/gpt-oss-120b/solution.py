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

    visited = [False] * (n + 1)
    col = [0] * (n + 1)          # temporary 0/1 colour
    ans = [0] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        # BFS this component
        q = deque([start])
        visited[start] = True
        col[start] = 0
        comp = [start]
        while q:
            x = q.popleft()
            cx = col[x]
            for y in adj[x]:
                if not visited[y]:
                    visited[y] = True
                    col[y] = cx ^ 1
                    q.append(y)
                    comp.append(y)
                elif col[y] == cx:
                    print("NO")
                    return
        # decide orientation: smallest index vertex gets final colour 1
        min_v = min(comp)   # actually start, but keep for clarity
        if col[min_v] == 0:
            for v in comp:
                ans[v] = 1 if col[v] == 0 else 2
        else:
            for v in comp:
                ans[v] = 1 if col[v] == 1 else 2

    # all good
    out = ["YES", " ".join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()