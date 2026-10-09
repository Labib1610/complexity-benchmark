import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)   # 0 or 1
    side = [[], []]          # vertices of each color

    from collections import deque
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        # start new component, assign color 0
        dq = deque([start])
        color[start] = 0
        side[0].append(start)
        while dq:
            u = dq.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    side[color[v]].append(v)
                    dq.append(v)
                # else: graph is guaranteed bipartite, no need to check conflict

    if len(side[0]) >= k:
        ans = side[0][:k]
    elif len(side[1]) >= k:
        ans = side[1][:k]
    else:
        print("NO")
        return

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()