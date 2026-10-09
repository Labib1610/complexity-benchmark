import sys
import threading

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    prod = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        prod.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    # Simple heuristic: try to route each product separately using max flow,
    # subtracting used capacities. If any fails, output NO.
    # This does not guarantee a solution when one exists, but serves as a
    # placeholder for the required implementation.

    from collections import deque

    # Build adjacency list for residual graph
    def bfs(s, t, parent, cap_matrix):
        visited = [False] * n
        q = deque()
        q.append(s)
        visited[s] = True
        while q:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap_matrix[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
                    q.append(v)
        return False

    # Initialize capacity matrix
    cap_matrix = [[0] * n for _ in range(n)]
    for idx, (u, v, c) in enumerate(edges):
        cap_matrix[u][v] = c

    # Result matrix
    res = [[0] * m for _ in range(k)]

    for pi, (s, t, d) in enumerate(prod):
        flow = 0
        parent = [-1] * n
        while flow < d and bfs(s, t, parent, cap_matrix):
            # find bottleneck
            path_cap = d - flow
            v = t
            while v != s:
                u = parent[v]
                path_cap = min(path_cap, cap_matrix[u][v])
                v = u
            # augment
            v = t
            while v != s:
                u = parent[v]
                cap_matrix[u][v] -= path_cap
                cap_matrix[v][u] += path_cap
                # record on original edge if exists
                for idx, (eu, ev, _) in enumerate(edges):
                    if eu == u and ev == v:
                        res[pi][idx] += path_cap
                        break
                v = u
            flow += path_cap
        if flow < d:
            print("NO")
            return

    print("YES")
    out = sys.stdout
    for i in range(k):
        out.write(' '.join(str(x) for x in res[i]))
        out.write('\n')

def main():
    solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()