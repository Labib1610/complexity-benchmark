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
        v = int(input_data[idx+1])
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

    # Subtree sizes
    sz = [0] * (n + 1)
    
    def get_sizes(u, p):
        s = 1
        for v in adj[u]:
            if v != p:
                s += get_sizes(v, u)
        sz[u] = s
        return s

    def get_centroid(u, p, total):
        for v in adj[u]:
            if v != p and sz[v] > total // 2:
                return get_centroid(v, u, total)
        return u

    get_sizes(1, 0)
    c1 = get_centroid(1, 0, n)
    get_sizes(c1, 0)
    
    # Candidates for root
    candidates = [c1]
    for v in adj[c1]:
        if sz[v] * 2 == n:
            candidates.append(v)
            
    # Also add a few high-degree vertices if small n
    if n <= 2000:
        deg_nodes = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
        for u in deg_nodes[:min(n, 50)]:
            if u not in candidates:
                candidates.append(u)

    best_cost = float('inf')
    best_pos = None

    for root in candidates:
        get_sizes(root, 0)
        
        # Build layout
        # dir: -1 means parent is to the right (children go to the left)
        # dir: +1 means parent is to the left (children go to the right)
        order = []
        
        def layout(u, p, direction):
            children = [v for v in adj[u] if v != p]
            children.sort(key=lambda x: sz[x])
            
            if direction == 0: # Root
                # Balance children between left and right
                left_children = []
                right_children = []
                sum_l, sum_r = 0, 0
                
                # Assign to keep balanced sizes, smaller closest to root
                for c in children:
                    if sum_l <= sum_r:
                        left_children.append(c)
                        sum_l += sz[c]
                    else:
                        right_children.append(c)
                        sum_r += sz[c]
                
                # Left children: furthest to closest, each expanding to the left
                for c in reversed(left_children):
                    layout(c, u, -1)
                    
                order.append(u)
                
                # Right children: closest to furthest, each expanding to the right
                for c in right_children:
                    layout(c, u, 1)
                    
            elif direction == -1: # Children to the left, u at right
                for c in reversed(children):
                    layout(c, u, -1)
                order.append(u)
                
            else: # Children to the right, u at left
                order.append(u)
                for c in children:
                    layout(c, u, 1)

        layout(root, 0, 0)
        
        pos = [0] * (n + 1)
        for i, u in enumerate(order):
            pos[u] = i + 1
            
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
            
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