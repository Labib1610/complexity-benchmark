import sys
sys.setrecursionlimit(1 << 25)

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

    colour = [-1] * (n + 1)          # temporary 0/1 colours
    ans = [0] * (n + 1)             # final 1/2 assignment

    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # new component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        while q:
            v = q.popleft()
            cv = colour[v]
            for to in g[v]:
                if colour[to] == -1:
                    colour[to] = cv ^ 1
                    q.append(to)
                    comp.append(to)
                elif colour[to] == cv:
                    print("NO")
                    return
        # component is bipartite
        v0 = min(comp)
        if colour[v0] == 0:
            # 0 -> 1, 1 -> 2
            for x in comp:
                ans[x] = 1 if colour[x] == 0 else 2
        else:
            # 0 -> 2, 1 -> 1
            for x in comp:
                ans[x] = 2 if colour[x] == 0 else 1

    out = ['YES', ' '.join(str(ans[i]) for i in range(1, n + 1))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()