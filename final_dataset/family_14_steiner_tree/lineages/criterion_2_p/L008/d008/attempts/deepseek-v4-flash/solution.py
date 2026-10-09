import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    R = int(next(it))
    S = int(next(it))
    P = int(next(it))

    required = [int(next(it)) - 1 for _ in range(P)]
    req = [False] * R
    for v in required:
        req[v] = True

    adj = [[] for _ in range(R)]
    edges = []
    for _ in range(S):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    degree = [len(adj[i]) for i in range(R)]
    visited = [False] * R
    from collections import deque

    # Remove all leaves that are not required
    q = deque()
    for i in range(R):
        if degree[i] == 1 and not req[i]:
            q.append(i)
            visited[i] = True

    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                degree[v] -= 1
                if degree[v] == 1 and not req[v]:
                    visited[v] = True
                    q.append(v)

    # Now count total weight of edges where both endpoints are not removed
    total = 0
    for u, v, w in edges:
        if not visited[u] and not visited[v]:
            total += w

    print(total)

if __name__ == "__main__":
    solve()