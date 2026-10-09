import sys
sys.setrecursionlimit(300000)

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
    
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    
    # compute subtree sizes
    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    min_cost = sum(size[v] for v in range(n) if v != 0)
    
    if min_cost > B:
        print("NO")
        return
    
    # assign hours via DFS preorder
    hour = [0] * n
    cur = 1
    stack = [0]
    while stack:
        u = stack.pop()
        hour[u] = cur
        cur += 1
        for v in adj[u]:
            if v != parent[u]:
                stack.append(v)
    
    print("YES")
    print(" ".join(str(hour[i]) for i in range(n)))

if __name__ == "__main__":
    solve()