import sys
sys.setrecursionlimit(1 << 25)

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

    colour = [-1] * (n + 1)          # 0 / 1
    ans = [0] * (n + 1)
    from collections import deque

    for start in range(1, n + 1):
        if colour[start] != -1:
            continue
        # new component
        q = deque([start])
        colour[start] = 0
        comp = [start]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif colour[v] == colour[u]:
                    print("NO")
                    return
        # assign values: colour of start gets 1
        col_start = colour[start]
        for v in comp:
            ans[v] = 1 if colour[v] == col_start else 2

    # all done
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()