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
    
    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        
    # Subtree sizes computation
    sz = [0] * (n + 1)
    
    def get_sizes(u, p):
        s = 1
        for v in adj[u]:
            if v != p:
                s += get_sizes(v, u)
        sz[u] = s
        return s

    def build_layout(u, p, parent_side):
        # parent_side: 'NONE', 'LEFT', 'RIGHT'
        children = [v for v in adj[u] if v != p]
        children.sort(key=lambda x: sz[x], reverse=True)
        
        if parent_side == 'NONE':
            # Root: partition children into L and R
            # c0 -> R (coeff 0), c1 -> L (coeff 0), c2 -> R (coeff 1), c3 -> L (coeff 1), ...
            L_children = []
            R_children = []
            for i, c in enumerate(children):
                if i % 2 == 0:
                    R_children.append(c)
                else:
                    L_children.append(c)
            
            # L_children from left to right: c1, c3, c5... (furthest from u to closest)
            # R_children from left to right: ...c4, c2, c0 (closest to u to furthest)
            res = []
            for c in L_children:
                res.extend(build_layout(c, u, 'RIGHT'))
            res.append(u)
            for c in reversed(R_children):
                res.extend(build_layout(c, u, 'LEFT'))
            return res

        elif parent_side == 'LEFT':
            # Parent is to the left of T_u
            # c0 -> R (coeff 0), c1 -> L (coeff 1), c2 -> R (coeff 1), c3 -> L (coeff 2), ...
            L_children = []
            R_children = []
            for i, c in enumerate(children):
                if i % 2 == 0:
                    R_children.append(c)
                else:
                    L_children.append(c)
            
            # In L: c1 has coeff 1 (closest to u), c3 has coeff 2, etc.
            # So from left to right: ...c5, c3, c1
            # In R: c0 has coeff 0 (furthest from u), c2 has coeff 1, etc.
            # So from left to right: ...c4, c2, c0
            res = []
            for c in reversed(L_children):
                res.extend(build_layout(c, u, 'RIGHT'))
            res.append(u)
            for c in reversed(R_children):
                res.extend(build_layout(c, u, 'LEFT'))
            return res

        else: # parent_side == 'RIGHT'
            # Symmetric to 'LEFT': mirror the layout
            # Parent is to the right of T_u
            L_children = []
            R_children = []
            for i, c in enumerate(children):
                if i % 2 == 0:
                    L_children.append(c)
                else:
                    R_children.append(c)
            
            # In L: c0 has coeff 0 (furthest from u, so at far left)
            # from left to right: c0, c2, c4...
            # In R: c1 has coeff 1 (closest to u)
            # from left to right: c1, c3, c5...
            res = []
            for c in L_children:
                res.extend(build_layout(c, u, 'RIGHT'))
            res.append(u)
            for c in R_children:
                res.extend(build_layout(c, u, 'LEFT'))
            return res

    def evaluate_root(r):
        get_sizes(r, 0)
        order = build_layout(r, 0, 'NONE')
        pos = [0] * (n + 1)
        for p, node in enumerate(order, 1):
            pos[node] = p
        cost = sum(abs(pos[u] - pos[v]) for u, v in edges)
        return cost, pos

    # Find centroids to test
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
    
    candidates = list(centroids)
    if n <= 1000:
        candidates = list(range(1, n + 1))
    else:
        # Add high-degree nodes
        deg_nodes = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
        candidates.extend(deg_nodes[:30])
        candidates = list(set(candidates))

    best_cost = float('inf')
    best_pos = None
    
    for r in candidates:
        cost, pos = evaluate_root(r)
        if cost < best_cost:
            best_cost = cost
            best_pos = pos
        if best_cost <= B:
            break
            
    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()