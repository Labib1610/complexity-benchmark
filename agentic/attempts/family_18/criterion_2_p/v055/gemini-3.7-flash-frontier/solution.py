import sys
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    start_time = time.time()
    
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
        print("YES")
        print("1")
        return

    # Find centroids / candidate roots
    sz = [0] * (n + 1)
    def get_sizes(root):
        order = []
        parent = [0] * (n + 1)
        stack = [root]
        parent[root] = -1
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)
        for u in reversed(order):
            sz[u] = 1
            for v in adj[u]:
                if v != parent[u]:
                    sz[u] += sz[v]
        return order, parent

    # Find centroid
    order, parent = get_sizes(1)
    centroid = 1
    for u in range(1, n + 1):
        is_c = True
        for v in adj[u]:
            if v != parent[u]:
                if sz[v] > n // 2:
                    is_c = False
                    break
            else:
                if n - sz[u] > n // 2:
                    is_c = False
                    break
        if is_c:
            centroid = u
            break

    candidate_roots = [centroid]
    # Add high degree vertices
    degs = sorted(range(1, n + 1), key=lambda x: len(adj[x]), reverse=True)
    for u in degs:
        if u not in candidate_roots:
            candidate_roots.append(u)
        if len(candidate_roots) >= min(n, 30):
            break

    def build_layout(root):
        order, parent = get_sizes(root)
        layout = {}
        root_pos = {} # 0-indexed position of node in its layout list
        
        for u in reversed(order):
            children = [v for v in adj[u] if v != parent[u]]
            if not children:
                layout[u] = [u]
                root_pos[u] = 0
                continue
            
            # Sort children by subtree size descending
            children.sort(key=lambda x: sz[x], reverse=True)
            
            # Partition into left and right to balance size
            L = []
            R = []
            sum_L = 0
            sum_R = 0
            for v in children:
                if sum_L <= sum_R:
                    L.append(v)
                    sum_L += sz[v]
                else:
                    R.append(v)
                    sum_R += sz[v]
            
            # For L: sort by size ascending so larger are closer to u (on right of L)
            L.sort(key=lambda x: sz[x])
            # For R: sort by size descending so larger are closer to u (on left of R)
            R.sort(key=lambda x: sz[x], reverse=True)
            
            res = []
            for v in L:
                lay_v = layout[v]
                pv = root_pos[v]
                # We want v close to the right end of lay_v
                if pv < len(lay_v) - 1 - pv:
                    lay_v.reverse()
                    pv = len(lay_v) - 1 - pv
                res.extend(lay_v)
                
            u_pos = len(res)
            res.append(u)
            
            for v in R:
                lay_v = layout[v]
                pv = root_pos[v]
                # We want v close to the left end of lay_v
                if pv > len(lay_v) - 1 - pv:
                    lay_v.reverse()
                    pv = len(lay_v) - 1 - pv
                res.extend(lay_v)
                
            layout[u] = res
            root_pos[u] = u_pos
            
        return layout[root]

    best_cost = float('inf')
    best_perm = None

    def compute_cost(pos):
        c = 0
        for u, v in edges:
            c += abs(pos[u] - pos[v])
        return c

    for r in candidate_roots:
        lay = build_layout(r)
        pos = [0] * (n + 1)
        for i, u in enumerate(lay):
            pos[u] = i
        cost = compute_cost(pos)
        if cost < best_cost:
            best_cost = cost
            best_perm = lay[:]

    # Local search optimization
    P = best_perm[:]
    pos = [0] * (n + 1)
    for i, u in enumerate(P):
        pos[u] = i

    cur_cost = best_cost

    # Optimization loop: median relocations and adjacent swaps
    improved = True
    iterations = 0
    while improved and time.time() - start_time < 4.0 and cur_cost > B:
        improved = False
        iterations += 1
        
        # 1. Median relocation for all nodes
        for u in range(1, n + 1):
            if len(adj[u]) == 0:
                continue
            nbr_pos = sorted([pos[v] for v in adj[u]])
            target_pos = nbr_pos[len(nbr_pos) // 2]
            current_p = pos[u]
            if target_pos == current_p:
                continue
            
            # Try relocating u from current_p to target_pos
            old_edge_sum = sum(abs(pos[u] - pos[v]) for v in adj[u])
            # If we move u, intermediate nodes shift
            # To be fast and exact, we can evaluate delta:
            # Shift direction:
            if target_pos < current_p:
                # nodes in P[target_pos : current_p] shift right by 1 (+1 in pos)
                shifted_nodes = P[target_pos:current_p]
                new_edge_sum = sum(abs(target_pos - (pos[v] + 1 if target_pos <= pos[v] < current_p else pos[v])) for v in adj[u])
                delta = new_edge_sum - old_edge_sum
                # for shifted nodes, their edges to nodes outside shift change
                for v in shifted_nodes:
                    for w in adj[v]:
                        if w == u:
                            continue
                        old_d = abs(pos[v] - pos[w])
                        w_pos = pos[w] + 1 if target_pos <= pos[w] < current_p else (target_pos if w == u else pos[w])
                        # Wait, during shift, pos[v] becomes pos[v]+1
                        new_d = abs(pos[v] + 1 - w_pos)
                        delta += (new_d - old_d) // 2 # each edge counted twice if both in shifted
                # Wait, simpler: if small delta < 0 apply
                if delta < 0:
                    P.pop(current_p)
                    P.insert(target_pos, u)
                    for i in range(target_pos, current_p + 1):
                        pos[P[i]] = i
                    cur_cost += delta
                    improved = True
            else:
                shifted_nodes = P[current_p + 1:target_pos + 1]
                new_edge_sum = sum(abs(target_pos - (pos[v] - 1 if current_p < pos[v] <= target_pos else pos[v])) for v in adj[u])
                delta = new_edge_sum - old_edge_sum
                for v in shifted_nodes:
                    for w in adj[v]:
                        if w == u:
                            continue
                        old_d = abs(pos[v] - pos[w])
                        w_pos = pos[w] - 1 if current_p < pos[w] <= target_pos else (target_pos if w == u else pos[w])
                        new_d = abs(pos[v] - 1 - w_pos)
                        delta += (new_d - old_d) // 2
                if delta < 0:
                    P.pop(current_p)
                    P.insert(target_pos, u)
                    for i in range(current_p, target_pos + 1):
                        pos[P[i]] = i
                    cur_cost += delta
                    improved = True

        # 2. Adjacent swaps sweep
        for i in range(n - 1):
            u = P[i]
            v = P[i + 1]
            delta = 0
            for w in adj[u]:
                if w != v:
                    delta += abs(i + 1 - pos[w]) - abs(i - pos[w])
            for w in adj[v]:
                if w != u:
                    delta += abs(i - pos[w]) - abs(i + 1 - pos[w])
            if delta < 0:
                P[i], P[i + 1] = v, u
                pos[u] = i + 1
                pos[v] = i
                cur_cost += delta
                improved = True

        if cur_cost <= B:
            break

    # Recalculate true cost to be 100% safe
    cur_cost = compute_cost(pos)
    if cur_cost <= B:
        print("YES")
        ans = [pos[i] + 1 for i in range(1, n + 1)]
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()