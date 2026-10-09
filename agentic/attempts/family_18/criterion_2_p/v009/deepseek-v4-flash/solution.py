import sys
sys.setrecursionlimit(300000)

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
    
    # Find centroid decomposition or use DP for min linear arrangement on trees
    # We'll use the known algorithm: 
    # For each node, compute subtree sizes, then place nodes in DFS order 
    # to minimize sum of edge lengths.
    
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
    
    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    # Greedy placement: assign positions by DFS order, 
    # but to minimize total length, we should place subtrees contiguously.
    # This is the classic "minimum linear arrangement" for trees:
    # Use a DFS that visits children in order of subtree size (largest first)
    # to keep large subtrees close.
    
    pos = [0] * n
    current = 1
    
    def dfs(u, p):
        nonlocal current
        pos[u] = current
        current += 1
        # sort children by subtree size descending
        children = [v for v in adj[u] if v != p]
        children.sort(key=lambda x: -size[x])
        for v in children:
            dfs(v, u)
    
    dfs(0, -1)
    
    total_length = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total_length += abs(pos[u] - pos[v])
    
    if total_length <= B:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()