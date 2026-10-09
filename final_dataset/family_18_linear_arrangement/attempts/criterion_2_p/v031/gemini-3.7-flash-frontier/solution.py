import sys

def solve():
    sys.setrecursionlimit(300000)
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
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2
        
    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    # Find subtree sizes from arbitrary root to find centroids
    sz = [0] * (n + 1)
    def get_sz(u, p):
        s = 1
        for v in adj[u]:
            if v != p:
                s += get_sz(v, u)
        sz[u] = s
        return s
    
    get_sz(1, 0)
    
    centroids = []
    def find_centroids(u, p):
        is_centroid = True
        for v in adj[u]:
            if v != p:
                if sz[v] > n // 2:
                    is_centroid = False
                find_centroids(v, u)
        if n - sz[u] > n // 2:
            is_centroid = False
        if is_centroid:
            centroids.append(u)
            
    find_centroids(1, 0)
    
    # Generate candidate roots
    if n <= 300:
        candidates = list(range(1, n + 1))
    else:
        cand_set = set(centroids)
        for c in centroids:
            for v in adj[c]:
                cand_set.add(v)
        candidates = list(cand_set)

    def layout_from_root(root):
        sub_sz = [0] * (n + 1)
        tree_children = [[] for _ in range(n + 1)]
        
        def dfs_prep(u, p):
            s = 1
            for v in adj[u]:
                if v != p:
                    tree_children[u].append(v)
                    s += dfs_prep(v, u)
            sub_sz[u] = s
            tree_children[u].sort(key=lambda x: sub_sz[x])
            return s
        
        dfs_prep(root, 0)
        
        def layout_subtree(u):
            # Returns list of vertices with u at the beginning (left)
            res = [u]
            for v in tree_children[u]:
                res.extend(layout_subtree(v))
            return res

        left_nodes = []
        right_nodes = []
        
        r_children = tree_children[root]
        # Alternate children to left and right
        left_ch = r_children[0::2]
        right_ch = r_children[1::2]
        
        # For left children, we want smallest closest to root,
        # and root of subtree closest to root (at right of subtree block)
        for v in reversed(left_ch):
            block = layout_subtree(v)
            block.reverse()
            left_nodes.extend(block)
            
        for v in right_ch:
            block = layout_subtree(v)
            right_nodes.extend(block)
            
        order = left_nodes + [root] + right_nodes
        return order

    best_order = None
    min_cost = float('inf')

    for r in candidates:
        order = layout_from_root(r)
        pos = [0] * (n + 1)
        for i, u in enumerate(order):
            pos[u] = i + 1
        
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
            if cost > B and cost > min_cost:
                break
                
        if cost < min_cost:
            min_cost = cost
            best_order = order
            if min_cost <= B:
                break

    if min_cost <= B:
        pos = [0] * (n + 1)
        for i, u in enumerate(best_order):
            pos[u] = i + 1
        print("YES")
        print(*(pos[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()