import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Root the tree at node 1
    parent = [0]*(n+1)
    children = [[] for _ in range(n+1)]
    stack = [1]
    parent[1] = 0
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                children[u].append(v)
                stack.append(v)
    
    # Compute subtree sizes
    size = [0]*(n+1)
    for u in reversed(order):
        size[u] = 1
        for v in children[u]:
            size[u] += size[v]
    
    # Sort children by subtree size (descending)
    for u in range(1, n+1):
        children[u].sort(key=lambda x: -size[x])
    
    # Assign positions using DFS
    pos = [0]*(n+1)
    current = 1
    stack = [1]
    while stack:
        u = stack.pop()
        pos[u] = current
        current += 1
        for v in children[u]:
            stack.append(v)
    
    # Calculate total length
    total = 0
    for u in range(2, n+1):
        total += abs(pos[u] - pos[parent[u]])
    
    if total <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(1, n+1)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()