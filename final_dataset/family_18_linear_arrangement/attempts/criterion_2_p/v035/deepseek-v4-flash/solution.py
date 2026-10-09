import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Try DFS preorder from each possible root (but root 0 is fine)
    def compute_order(order):
        pos = [0]*n
        for idx, node in enumerate(order):
            pos[node] = idx+1
        total = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    total += abs(pos[u] - pos[v])
        return total, pos
    
    # DFS preorder
    def dfs_preorder(root):
        visited = [False]*n
        order = []
        stack = [root]
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            order.append(u)
            # push neighbors in reverse order for consistent preorder
            for v in reversed(adj[u]):
                if not visited[v]:
                    stack.append(v)
        return order
    
    # BFS order
    def bfs_order(root):
        visited = [False]*n
        order = []
        q = deque([root])
        visited[root] = True
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return order
    
    # Try DFS from each node as root (small n, but we can limit)
    for root in range(n):
        order = dfs_preorder(root)
        if len(order) == n:
            total, pos = compute_order(order)
            if total <= B:
                print("YES")
                print(" ".join(str(x) for x in pos))
                return
    
    # Try BFS from each node
    for root in range(n):
        order = bfs_order(root)
        if len(order) == n:
            total, pos = compute_order(order)
            if total <= B:
                print("YES")
                print(" ".join(str(x) for x in pos))
                return
    
    print("NO")

if __name__ == "__main__":
    solve()