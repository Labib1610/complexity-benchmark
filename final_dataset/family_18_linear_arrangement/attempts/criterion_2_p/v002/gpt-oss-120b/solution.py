import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    def order_by_dfs():
        order = []
        visited = [False] * (n + 1)
        stack = [(1, 0)]
        while stack:
            u, p = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            order.append(u)
            for v in adj[u][::-1]:
                if v != p:
                    stack.append((v, u))
        return order

    def order_by_bfs():
        from collections import deque
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return order

    def check(order):
        pos = [0] * (n + 1)
        for idx, node in enumerate(order, 1):
            pos[node] = idx
        total = 0
        for u in range(1, n + 1):
            for v in adj[u]:
                if u < v:
                    total += abs(pos[u] - pos[v])
                    if total > B:
                        return None
        return pos[1:]

    for get_order in (order_by_dfs, order_by_bfs):
        order = get_order()
        res = check(order)
        if res is not None:
            print("YES")
            print(' '.join(map(str, res)))
            return

    print("NO")

if __name__ == "__main__":
    solve()