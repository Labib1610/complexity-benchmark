import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        
    root = 1
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = []
    
    q = deque([root])
    parent[root] = -1
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                children[u].append(v)
                q.append(v)
                
    size = [1] * (n + 1)
    for u in reversed(order):
        for v in children[u]:
            size[u] += size[v]
            
    ans = [0] * (n + 1)
    cur = 1
    
    for u in order:
        ans[u] = cur
        cur += size[u]
        
    total_cost = 0
    for u in order:
        for v in children[u]:
            total_cost += size[v] * (size[u] - size[v] - 1)
            
    if total_cost <= B:
        print("YES")
        print(" ".join(map(str, ans[1:])))
    else:
        print("NO")

if __name__ == '__main__':
    solve()