import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
    ans = [0] * (n + 1)              # final shifts 1/2

    for v in range(1, n + 1):
        if colour[v] != -1:
            continue
        # start new component, give v colour 0
        q = deque([v])
        colour[v] = 0
        comp = [v]
        ok = True
        while q:
            x = q.popleft()
            cx = colour[x]
            for y in g[x]:
                if colour[y] == -1:
                    colour[y] = cx ^ 1
                    q.append(y)
                    comp.append(y)
                elif colour[y] == cx:
                    print("NO")
                    return
        # orient so that v (colour 0) gets shift 1
        target = colour[v]   # always 0 here
        for u in comp:
            ans[u] = 1 if colour[u] == target else 2

    out = ['YES', ' '.join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()