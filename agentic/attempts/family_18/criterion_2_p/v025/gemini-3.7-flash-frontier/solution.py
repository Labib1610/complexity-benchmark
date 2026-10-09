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
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    # Find centroids to test
    sz = [0] * (n + 1)
    
    def get_sizes(u, p):
        s = 1
        for v in adj[u]:
            if v != p:
                s += get_sizes(v, u)
        sz[u] = s
        return s

    get_sizes(1, 0)
    
    centroids = []
    def find_centroids(u, p):
        is_centroid = True
        for v in adj[u]:
            if v != p:
                if sz[v] > n // 2:
                    is_centroid = False
                find_centroids(v, u)
        if is_centroid and (n - sz[u] <= n // 2):
            centroids.append(u)

    find_centroids(1, 0)
    
    # Also if n is small, we can test all vertices; if large, test centroids and candidates
    candidates = list(set(centroids))
    if n <= 2000:
        candidates = list(range(1, n + 1))
    elif len(candidates) < 10:
        # Add some high degree vertices
        deg_nodes = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
        candidates = list(set(candidates + deg_nodes[:50]))

    def get_subtree_info(u, p):
        # returns (size, internal_cost, sorted_children_info)
        sub_sz = 1
        int_cost = 0
        children = []
        for v in adj[u]:
            if v != p:
                c_sz, c_cost, c_children = get_subtree_info(v, u)
                children.append((c_sz, c_cost, v, c_children))
                sub_sz += c_sz
                int_cost += c_cost
        
        children.sort(key=lambda x: x[0])
        prefix_sum = 0
        for c_sz, c_cost, v, _ in children:
            int_cost += (1 + prefix_sum)
            prefix_sum += c_sz
            
        return sub_sz, int_cost, children

    def eval_root(R):
        children = []
        for v in adj[R]:
            c_sz, c_cost, c_children = get_subtree_info(v, R)
            children.append((c_sz, c_cost, v, c_children))
        
        children.sort(key=lambda x: x[0])
        
        # Left: children[0], children[2], ...
        # Right: children[1], children[3], ...
        total_cost = 0
        left_pref = 0
        right_pref = 0
        left_children = []
        right_children = []
        
        for i, (c_sz, c_cost, v, c_children) in enumerate(children):
            total_cost += c_cost
            if i % 2 == 0:
                total_cost += (1 + left_pref)
                left_pref += c_sz
                left_children.append((c_sz, c_cost, v, c_children))
            else:
                total_cost += (1 + right_pref)
                right_pref += c_sz
                right_children.append((c_sz, c_cost, v, c_children))
                
        return total_cost, left_children, right_children

    best_cost = float('inf')
    best_root_data = None
    best_root = None

    for R in candidates:
        cost, left_children, right_children = eval_root(R)
        if cost < best_cost:
            best_cost = cost
            best_root_data = (left_children, right_children)
            best_root = R

    if best_cost > B:
        print("NO")
        return

    print("YES")
    
    order = []
    
    def build_tree(u, children, direction):
        if direction == 'R':
            order.append(u)
            for c_sz, c_cost, v, c_children in children:
                build_tree(v, c_children, 'R')
        else:
            for c_sz, c_cost, v, c_children in reversed(children):
                build_tree(v, c_children, 'L')
            order.append(u)

    left_children, right_children = best_root_data
    
    # Build left
    for c_sz, c_cost, v, c_children in reversed(left_children):
        build_tree(v, c_children, 'L')
        
    order.append(best_root)
    
    # Build right
    for c_sz, c_cost, v, c_children in right_children:
        build_tree(v, c_children, 'R')

    pos = [0] * (n + 1)
    for bay, node in enumerate(order, 1):
        pos[node] = bay

    print(*(pos[1:]))

if __name__ == '__main__':
    solve()