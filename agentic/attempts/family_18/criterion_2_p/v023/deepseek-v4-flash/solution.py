import sys
from collections import deque

def solve():
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

    # If B < n-1, impossible because each edge contributes at least 1
    if B < n - 1:
        print("NO")
        return

    # Try DFS preorder from every possible root
    for root in range(n):
        # Iterative DFS preorder
        order = []
        parent = [-1] * n
        stack = [root]
        parent[root] = root
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)
        # Now order is a preorder traversal
        # Assign numbers: order[0] gets 1, order[1] gets 2, ...
        num = [0] * n
        for i, node in enumerate(order):
            num[node] = i + 1

        # Compute total wait time
        total = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    total += abs(num[u] - num[v])
        if total <= B:
            print("YES")
            print(" ".join(str(num[i]) for i in range(n)))
            return

    # If no root works, try BFS order from each root
    for root in range(n):
        order = []
        parent = [-1] * n
        q = deque([root])
        parent[root] = root
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        num = [0] * n
        for i, node in enumerate(order):
            num[node] = i + 1
        total = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    total += abs(num[u] - num[v])
        if total <= B:
            print("YES")
            print(" ".join(str(num[i]) for i in range(n)))
            return

    print("NO")

if __name__ == "__main__":
    solve()