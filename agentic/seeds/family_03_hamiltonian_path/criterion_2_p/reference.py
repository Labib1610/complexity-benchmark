import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    edge_set = set()
    indegree = [0] * (n + 1)

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        edge_set.add((u, v))
        indegree[v] += 1

    # Kahn's algorithm: at every step exactly one vertex must have in-degree 0
    queue = deque()
    for v in range(1, n + 1):
        if indegree[v] == 0:
            queue.append(v)

    order = []
    while queue:
        if len(queue) != 1:
            print("NO")
            return
        v = queue.popleft()
        order.append(v)
        for u in adj[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                queue.append(u)

    if len(order) != n:
        print("NO")
        return

    # Verify every consecutive pair is an edge
    for i in range(n - 1):
        if (order[i], order[i + 1]) not in edge_set:
            print("NO")
            return

    print("YES")
    print(' '.join(map(str, order)))

main()
