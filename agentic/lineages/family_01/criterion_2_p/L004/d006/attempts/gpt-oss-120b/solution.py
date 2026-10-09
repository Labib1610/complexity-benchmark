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

    col = [-1] * (n + 1)          # temporary 0/1 colours
    ans = [0] * (n + 1)           # final 1/2 values
    q = deque()

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # new component
        comp = []
        col[start] = 0
        q.append(start)
        while q:
            v = q.popleft()
            comp.append(v)
            for to in adj[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        # decide orientation: smallest index gets value 1
        first = min(comp)
        wanted = col[first]          # colour that must become 1
        for v in comp:
            ans[v] = 1 if col[v] == wanted else 2

    # all done
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()