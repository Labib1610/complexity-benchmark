import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
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

    color = [-1] * (n + 1)          # 0 or 1
    ans = [0] * (n + 1)
    from collections import deque

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # BFS this component
        q = deque([start])
        color[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
        # decide flip so that smallest vertex gets color 0 (=> shift 1)
        min_v = min(comp)
        if color[min_v] == 1:
            # flip whole component
            for v in comp:
                color[v] ^= 1
        # store answer
        for v in comp:
            ans[v] = color[v] + 1   # 0->1, 1->2

    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()