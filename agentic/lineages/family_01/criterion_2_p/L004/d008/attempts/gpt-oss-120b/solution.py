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

    col = [-1] * (n + 1)          # parity 0/1, -1 = unvisited
    ans = [0] * (n + 1)           # final values 1/2

    from collections import deque

    for start in range(1, n + 1):
        if col[start] != -1:
            continue
        # new component
        q = deque([start])
        col[start] = 0
        comp = [start]
        ok = True
        while q:
            v = q.popleft()
            for to in adj[v]:
                if col[to] == -1:
                    col[to] = col[v] ^ 1
                    q.append(to)
                    comp.append(to)
                elif col[to] == col[v]:
                    print("NO")
                    return
        # decide mapping so that smallest index gets value 1
        smallest = min(comp)
        if col[smallest] == 0:
            for v in comp:
                ans[v] = 1 if col[v] == 0 else 2
        else:
            for v in comp:
                ans[v] = 1 if col[v] == 1 else 2

    # all good
    print("YES")
    print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()