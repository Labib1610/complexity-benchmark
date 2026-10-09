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
    
    # Try multiple orderings
    orderings = []
    
    # DFS order
    parent = [-1]*n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    orderings.append(order)
    
    # BFS order
    order = []
    q = deque([0])
    parent = [-1]*n
    parent[0] = 0
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)
    orderings.append(order)
    
    # Reverse DFS order
    orderings.append(orderings[0][::-1])
    # Reverse BFS order
    orderings.append(orderings[1][::-1])
    
    # Also try a "zigzag" order: take DFS order and interleave from ends
    dfs_order = orderings[0]
    zigzag = []
    l, r = 0, n-1
    while l <= r:
        if l == r:
            zigzag.append(dfs_order[l])
            break
        zigzag.append(dfs_order[l])
        zigzag.append(dfs_order[r])
        l += 1
        r -= 1
    orderings.append(zigzag)
    
    for order in orderings:
        pos = [0]*n
        for slot, node in enumerate(order, start=1):
            pos[node] = slot
        total = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    total += abs(pos[u] - pos[v])
        if total <= B:
            print("YES")
            print(" ".join(str(pos[i]) for i in range(n)))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()