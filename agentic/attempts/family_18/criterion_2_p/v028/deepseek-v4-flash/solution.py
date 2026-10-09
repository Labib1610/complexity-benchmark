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
    
    # Try multiple orderings
    orders = []
    
    # 1. DFS preorder from node 0
    parent = [-1]*n
    order = []
    stack = [0]
    parent[0] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    orders.append(order)
    
    # 2. BFS order
    order = []
    q = deque([0])
    parent = [-1]*n
    parent[0] = -2
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)
    orders.append(order)
    
    # 3. Reverse of DFS preorder
    parent = [-1]*n
    order = []
    stack = [0]
    parent[0] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    orders.append(order[::-1])
    
    # 4. Reverse BFS
    order = []
    q = deque([0])
    parent = [-1]*n
    parent[0] = -2
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)
    orders.append(order[::-1])
    
    # Also try starting from each node? Too slow. But we can try a few.
    # Try starting from node with max degree
    deg = [len(adj[i]) for i in range(n)]
    start = max(range(n), key=lambda i: deg[i])
    for s in [start]:
        parent = [-1]*n
        order = []
        stack = [s]
        parent[s] = -2
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)
        orders.append(order)
    
    # Try BFS from max degree
    for s in [start]:
        order = []
        q = deque([s])
        parent = [-1]*n
        parent[s] = -2
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        orders.append(order)
    
    seen = set()
    for order in orders:
        # assign positions: order[0] -> 1, order[1] -> 2, ...
        pos = [0]*n
        for i, node in enumerate(order):
            pos[node] = i+1
        # compute cost
        cost = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    cost += abs(pos[u] - pos[v])
        if cost <= B:
            print("YES")
            print(" ".join(str(pos[i]) for i in range(n)))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()