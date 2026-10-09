import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        
    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    # Find centroids
    sz = [0] * (n + 1)
    def get_sizes(u, p):
        sz[u] = 1
        for v in adj[u]:
            if v != p:
                get_sizes(v, u)
                sz[u] += sz[v]
    get_sizes(1, 0)
    
    centroids = []
    def find_centroids(u, p):
        is_centroid = True
        for v in adj[u]:
            if v != p:
                find_centroids(v, u)
                if sz[v] > n // 2:
                    is_centroid = False
        if n - sz[u] > n // 2:
            is_centroid = False
        if is_centroid:
            centroids.append(u)
    find_centroids(1, 0)

    def evaluate_root(root):
        subtree_sz = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        
        # Iterative or DFS to build tree rooted at `root`
        order = []
        stack = [(root, 0)]
        parent = [0] * (n + 1)
        while stack:
            u, p = stack.pop()
            order.append(u)
            parent[u] = p
            for v in adj[u]:
                if v != p:
                    children[u].append(v)
                    stack.append((v, u))
        
        for u in reversed(order):
            s = 1
            for v in children[u]:
                s += subtree_sz[v]
            subtree_sz[u] = s
            # Sort children descending by subtree size
            children[u].sort(key=lambda x: subtree_sz[x], reverse=True)
        
        # Build layout
        # For non-root, if facing_right=True, u is on the right of its children
        def build_layout_right(u):
            # children ordered descending away from u, so closest child is children[u][0]
            # to be placed to the left: farther children first, then closer, then u
            res = []
            for v in reversed(children[u]):
                res.extend(build_layout_right(v))
            res.append(u)
            return res

        def build_layout_left(u):
            # u is on the left of its children
            # closest child is children[u][0]
            # u, then closer children, then farther children
            res = [u]
            for v in children[u]:
                res.extend(build_layout_left(v))
            return res

        # Root partitions children into L and R
        # L goes to the left of root, R goes to the right of root
        L = children[root][0::2]
        R = children[root][1::2]
        
        layout = []
        for v in reversed(L):
            layout.extend(build_layout_right(v))
        layout.append(root)
        for v in R:
            layout.extend(build_layout_left(v))
            
        pos = [0] * (n + 1)
        for i, u in enumerate(layout):
            pos[u] = i + 1
            
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
            
        return cost, pos

    best_cost = float('inf')
    best_pos = None

    candidate_roots = set(centroids)
    if n <= 1000:
        candidate_roots = range(1, n + 1)
    else:
        # Also add high-degree nodes just in case
        deg_nodes = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
        for u in deg_nodes[:10]:
            candidate_roots.add(u)

    for r in candidate_roots:
        cost, pos = evaluate_root(r)
        if cost < best_cost:
            best_cost = cost
            best_pos = pos
            if best_cost <= B:
                break

    if best_cost <= B:
        print("YES")
        print(*(best_pos[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()