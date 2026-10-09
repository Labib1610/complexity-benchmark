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
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # simple BFS ordering
    from collections import deque
    visited = [False] * n
    order = []
    q = deque([0])
    visited[0] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    # assign positions according to order
    pos = [0] * n
    for idx, node in enumerate(order):
        pos[node] = idx + 1  # positions are 1-indexed

    # compute total length
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
                if total > B:
                    break
        if total > B:
            break

    if total <= B:
        print("YES")
        print(' '.join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()