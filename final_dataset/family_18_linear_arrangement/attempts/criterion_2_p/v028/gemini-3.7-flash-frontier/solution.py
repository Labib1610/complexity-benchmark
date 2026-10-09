import sys

# Increase recursion depth just in case
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
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # Find centroid(s) and candidate roots
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
        # Add high-degree vertices and neighbors of centroids
        for c in centroids:
            for v in adj[c]:
                candidates.append(v)
        # Add top degree nodes
        deg_nodes = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
        candidates.extend(deg_nodes[:50])
        candidates = list(set(candidates))

    best_cost = float('inf')
    best_root = None

    def evaluate_root(root):
        # Compute subtree sizes rooted at root
        sub_sz = [0] * (n + 1)
        stack = [(root, 0, False)]
        order = []
        while stack:
            u, p, visited = stack.pop()
            if visited:
                s = 1
                for v in adj[u]:
                    if v != p:
                        s += sub_sz[v]
                sub_sz[u] = s
            else:
                order.append((u, p))
                stack.append((u, p, True))
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, False))

        # Calculate cost
        total_cost = 0
        for u, p in order:
            children = [v for v in adj[u] if v != p]
            children.sort(key=lambda x: sub_sz[x], reverse=True)
            if u == root:
                # Alternate distribution
                # Multipliers: 0, 0, 1, 1, 2, 2, ...
                for i, c in enumerate(children):
                    mult = i // 2
                    total_cost += mult * sub_sz[c] + 1
            else:
                for i, c in enumerate(children):
                    mult = i
                    total_cost += mult * sub_sz[c] + 1
        return total_cost

    for r in candidates:
        cost = evaluate_root(r)
        if cost < best_cost:
            best_cost = cost
            best_root = r
            if best_cost <= B:
                break

    if best_cost > B:
        print("NO")
        return

    print("YES")
    
    # Construct the actual layout with best_root
    root = best_root
    sub_sz = [0] * (n + 1)
    
    stack = [(root, 0, False)]
    while stack:
        u, p, visited = stack.pop()
        if visited:
            s = 1
            for v in adj[u]:
                if v != p:
                    s += sub_sz[v]
            sub_sz[u] = s
        else:
            stack.append((u, p, True))
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, False))

    layout = []

    # side: 'L' means parent is to the right of this subtree, so u should be at the right boundary
    # 'R' means parent is to the left of this subtree, so u should be at the left boundary
    def build_layout(u, p, side):
        children = [v for v in adj[u] if v != p]
        children.sort(key=lambda x: sub_sz[x], reverse=True)
        
        if u == root:
            # Partition into left and right
            left_children = []
            right_children = []
            for i, c in enumerate(children):
                if i % 2 == 0:
                    left_children.append(c)
                else:
                    right_children.append(c)
            
            # Left children: placed in reverse order of proximity (furthest left first)
            for c in reversed(left_children):
                build_layout(c, u, 'L')
            
            layout.append(u)
            
            for c in right_children:
                build_layout(c, u, 'R')
        else:
            if side == 'L':
                # u is at right boundary, all children to the left
                # children sorted desc by size: closest to u is children[0]
                # so furthest from u is children[-1], should be placed first
                for c in reversed(children):
                    build_layout(c, u, 'L')
                layout.append(u)
            else:
                # side == 'R': u is at left boundary, all children to the right
                # children[0] is closest to u, so placed right after u
                layout.append(u)
                for c in children:
                    build_layout(c, u, 'R')

    build_layout(root, 0, '')

    pos = [0] * (n + 1)
    for bay, machine in enumerate(layout, 1):
        pos[machine] = bay

    print(*(pos[i] for i in range(1, n + 1)))

if __name__ == '__main__':
    solve()