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
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Root the tree at 1
    parent = [0]*(n+1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
    
    size = [1]*(n+1)
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    min_cost = 0
    for u in range(2, n+1):
        s = size[u]
        min_cost += s * (n - s)
    
    if min_cost > B:
        print("NO")
        return
    
    # Generate preorder labels
    label = [0]*(n+1)
    counter = 1
    stack = [(1, 0)]
    while stack:
        u, state = stack.pop()
        if state == 0:
            label[u] = counter
            counter += 1
            # push children in reverse order
            children = [v for v in adj[u] if v != parent[u]]
            for v in reversed(children):
                stack.append((v, 1))
                stack.append((v, 0))
    
    print("YES")
    print(" ".join(str(label[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    solve()