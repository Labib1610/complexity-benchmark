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
    edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2
        
    if n == 1:
        print("YES")
        print("1")
        return

    # Compute subtree sizes for a rooted tree
    sz = [0] * (n + 1)
    
    def get_layout(root):
        # 1. Compute tree structure from root using BFS/iterative DFS
        parent = [0] * (n + 1)
        order_bfs = []
        visited = [False] * (n + 1)
        visited[root] = True
        queue = [root]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            order_bfs.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        
        children = [[] for _ in range(n + 1)]
        for u in order_bfs[1:]:
            children[parent[u]].append(u)
            
        for u in reversed(order_bfs):
            s = 1
            for v in children[u]:
                s += sz[v]
            sz[u] = s
            # Sort children by subtree size ascending
            children[u].sort(key=lambda x: sz[x])
            
        # 2. Build layout recursively
        # For the root node, we can distribute children to left and right
        # For any other node u, u will be at the boundary (say left), and all its children to the right.
        def build_child(u):
            # Returns list of vertices in layout with u at the beginning (leftmost)
            res = [u]
            for v in children[u]:
                res.extend(build_child(v))
            return res

        left_nodes = []
        right_nodes = []
        # Alternate children between left and right to balance
        # Put smaller children closer to root
        for i, v in enumerate(children[root]):
            sub_layout = build_child(v)
            if i % 2 == 0:
                # Place to right: root of sub is at the beginning of sub_layout, closest to `root`
                right_nodes.extend(sub_layout)
            else:
                # Place to left: root of sub must be closest to `root`, so reverse sub_layout
                left_nodes.extend(reversed(sub_layout))
                
        # Full layout: reversed(left_nodes) + [root] + right_nodes
        full_layout = list(reversed(left_nodes)) + [root] + right_nodes
        return full_layout

    def eval_cost(layout):
        pos = [0] * (n + 1)
        for p, u in enumerate(layout, 1):
            pos[u] = p
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost, pos

    # Find centroid candidates
    sz_c = [0] * (n + 1)
    def find_centroids():
        order_bfs = []
        visited = [False] * (n + 1)
        visited[1] = True
        queue = [1]
        parent = [0] * (n + 1)
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            order_bfs.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        for u in reversed(order_bfs):
            s = 1
            for v in adj[u]:
                if v != parent[u]:
                    s += sz_c[v]
            sz_c[u] = s
            
        centroids = []
        for u in range(1, n + 1):
            is_c = True
            for v in adj[u]:
                if v != parent[u]:
                    if sz_c[v] > n // 2:
                        is_c = False
                        break
                else:
                    if n - sz_c[u] > n // 2:
                        is_c = False
                        break
            if is_c:
                centroids.append(u)
        return centroids

    centroids = find_centroids()
    candidates = list(centroids)
    
    # Add high-degree nodes as candidates
    deg_nodes = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
    for u in deg_nodes[:min(20, n)]:
        if u not in candidates:
            candidates.append(u)
            
    best_cost = float('inf')
    best_pos = None

    for root in candidates:
        layout = get_layout(root)
        cost, pos = eval_cost(layout)
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