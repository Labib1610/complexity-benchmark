import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    colour = [-1] * (n + 1)          # temporary 0/1
    ans = [0] * (n + 1)              # final 1/2

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        colour[start] = 0
        comp = []
        while q:
            x = q.popleft()
            comp.append(x)
            for y in g[x]:
                if colour[y] == -1:
                    colour[y] = colour[x] ^ 1
                    q.append(y)
                elif colour[y] == colour[x]:
                    print("NO")
                    return
        # orient so that smallest vertex gets final colour 1
        v0 = min(comp)
        base = colour[v0]
        for v in comp:
            ans[v] = 1 if colour[v] == base else 2

    # all good
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()