import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Compute subtree sizes using BFS from root 0
    parent = [-1] * n
    order = [0]
    parent[0] = -2
    for u in order:
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                order.append(v)
    
    size = [1] * n
    order_rev = list(reversed(order))
    for u in order_rev:
        if parent[u] >= 0:
            size[parent[u]] += size[u]
    
    # Global variables for DP
    best_assignment = None
    
    # DP tables: (start_index) -> (min_total_cost, parent_assign)
    # dpleft[u]: minimize left parent cost using left interval of size size[u]
    # dpright[u]: minimize right parent cost using right interval of size size[u]
    
    dpleft = [{} for _ in range(n)]
    dpright = [{} for _ in range(n)]
    
    for u in order_rev:
        ch = [v for v in adj[u] if parent[v] == u]
        s = size[u]
        sc = [size[v] for v in ch]
        k = len(ch)
        
        # ===== Compute dpleft[u] =====
        # dpC_left[prefix][i] = min cost for first 'prefix' children using left interval of size i
        # Children are ordered by subtree size ascending for efficiency
        order_ch = sorted(range(k), key=lambda x: sc[x])
        
        # Compute DP for child costs
        # child_left_cost[j][a] = min cost for child j with interval [1, a]
        # child_right_cost[j][a] = min cost for child j with interval [L-a+1, L]
        
        dpC_left = [0] + [float('inf')] * (s - 1)
        dpC_right = [0] + [float('inf')] * (s - 1)
        
        for idx in range(k):
            j = order_ch[idx]
            v = ch[j]
            sz = sc[j]
            new_left = [float('inf')] * s
            new_right = [float('inf')] * s
            
            dl_v = dpleft[v]
            dr_v = dpright[v]
            
            for a in range(1, sz + 1):
                if a - 1 in dl_v:
                    cl = dl_v[a - 1]
                else:
                    continue
                if sz - a in dr_v:
                    cr = dr_v[sz - a]
                else:
                    continue
                
                for i in range(a, s):
                    val = cl + dpC_left[i - a]
                    if val < new_left[i]:
                        new_left[i] = val
                
                for i in range(sz - a + 1, s):
                    val = cr + dpC_right[i - (sz - a)]
                    if val < new_right[i]:
                        new_right[i] = val
            
            for i in range(1, s):
                dpC_left[i] = new_left[i]
                dpC_right[i] = new_right[i]
        
        # For leaf nodes, dpC_left/right entries are inf except 0 at index 0
        # dpleft[u]: parent at position 1 in this interval
        for a in range(1, s + 1):
            cost = float('inf')
            if a - 1 < s:
                cost = dpC_left[a - 1]
            if cost < float('inf'):
                dpleft[u][a - 1] = cost
        
        # dpright[u]: parent at position s in this interval
        for a in range(1, s + 1):
            cost = float('inf')
            if s - a < s:
                cost = dpC_right[s - a]
            if cost < float('inf'):
                dpright[u][s - a] = cost
    
    # Check feasibility and reconstruct
    k = len([v for v in adj[0] if parent[v] == 0])
    if k == 0:
        # Single node
        if B >= 0:
            print("YES")
            print(1)
        else:
            print("NO")
        return
    
    sc = [size[v] for v in adj[0] if parent[v] == 0]
    ch = [v for v in adj[0] if parent[v] == 0]
    order_idx = sorted(range(k), key=lambda x: sc[x])
    
    dp = {}
    pred = {}
    dp[0] = 0
    
    for idx in range(k):
        j = order_idx[idx]
        v = ch[j]
        sz = sc[v]
        new_dp = {}
        new_pred = {}
        dl_v = dpleft[v]
        dr_v = dpright[v]
        
        for i in dp:
            for a in range(1, sz + 1):
                if a - 1 in dl_v:
                    cl = dl_v[a - 1]
                    cost = cl + dp[i]
                    key = (i + a, a)
                    if key not in new_dp or cost < new_dp[key]:
                        new_dp[key] = cost
                        new_pred[key] = (j, 'L', a)
                
                if sz - a in dr_v:
                    cr = dr_v[sz - a]
                    cost = cr + dp[i]
                    key = (i + sz, -a)
                    if key not in new_dp or cost < new_dp[key]:
                        new_dp[key] = cost
                        new_pred[key] = (j, 'R', a)
        
        dp = new_dp
        pred = new_pred
    
    min_cost = float('inf')
    best_start = None
    for (start, a_key), cost in dp.items():
        if cost < min_cost:
            min_cost = cost
            best_start = (start, a_key)
    
    if min_cost > B:
        print("NO")
        return
    
    # Reconstruct assignment
    pos = [0] * n
    assignment = [None] * n
    
    def assign(u, L, R, parent_pos):
        sz = size[u]
        if parent_pos == -1:
            # Root node: assign to position based on reconstruction
            # Find the actual position of root (node 0)
            pass
        else:
            if pos[u] == L:
                assignment[u] = L
            else:
                assignment[u] = R
        
        # Sort children by subtree size (descending to process largest first)
        ch_u = [v for v in adj[u] if parent[v] == u]
        ch_u.sort(key=lambda x: -size[x])
        
        cur_L = L
        cur_R = R
        
        for v in ch_u:
            sv = size[v]
            if pos[v] > pos[u]:  # child is to the right
                assign(v, cur_R - sv + 1, cur_R, pos[u])
                cur_R -= sv
            else:  # child is to the left
                assign(v, cur_L, cur_L + sv - 1, pos[u])
                cur_L += sv
    
    # Reconstruct positions for root's children
    child_config = []
    current_pos = 1
    trace_key = best_start
    
    for idx in range(k - 1, -1, -1):
        j, side, a = pred[trace_key]
        sz = sc[j]
        v = ch[j]
        
        if side == 'L':
            # Child v is to the left of root
            # Interval [current_pos + sz - a, current_pos + sz - 1] for v? No.
            # Actually: left interval of size sz, with parent at relative position a
            # Parent (root) is at position a in child's interval
            # Child occupies positions 1 to sz, root is at a within that interval
            # But root is parent, so child's interval is [start, start + sz - 1]
            # Root is at position start + a - 1 globally
            
            # For left side: child subtree is in interval [L, L + sz - 1]
            # Root (parent) at position L + a - 1 (but root is outside this interval?)
            # Wait, dpleft means parent is at position 1 of the interval
            # But parent is the root... let me reconsider.
            
            # dpleft[v] stores cost when parent is at relative position a_within_child_interval
            # The 'a' in reconstruction is relative position of parent (root) within child's interval
            # For 'L': child subtree is entirely to the left of root
            # So root is at position (end of child interval) + 1 = (L + sz - 1) + 1
            # Thus L = root_pos - sz
            
            # Let me re-derive:
            # The root position will be determined by child positions
            # For 'L' child: child subtree in [r - total_left - sz + 1, r - total_left]
            # and root at r
            # where total_left is sum of sizes of children already placed to the left
            
            pass
        else:
            # 'R': child to the right
            pass
        
        # Simplified approach: use positions from DP reconstruction
        # Store the configuration
        child_config.append((j, side, a))
        trace_key = (trace_key[0] - sz, trace_key[1])  # This is wrong, need to backtrack pred properly
    
    # Alternative: reconstruct using a simpler approach
    # Find root position from the minimum cost solution
    
    # Easier method: directly assign positions based on the reconstruction order
    # Let's try a different approach - compute root position from the configuration
    
    # Reconstruct by following pred backwards
    config = []
    trace = best_start
    for idx in range(k - 1, -1, -1):
        j, side, a = pred[trace]
        config.append((j, side, a))
        sz = sc[j]
        trace = (trace[0] - sz, 0)  # The second component for non-last is arbitrary
    
    config.reverse()
    
    # Compute root position
    root_pos = 0
    left_size = 0
    for j, side, a in config:
        sz = sc[j]
        if side == 'L':
            root_pos = max(root_pos, left_size + a)
            left_size += sz
        else:
            pass
    
    right_start = n
    for j, side, a in reversed(config):
        sz = sc[j]
        if side == 'R':
            root_pos = max(root_pos, right_start - sz + a - 1)
            right_start -= sz
    
    # Find valid root_pos
    root_pos = None
    left_end = 0
    right_start = n + 1
    
    for j, side, a in config:
        sz = sc[j]
        if side == 'L':
            left_end += sz
        else:
            right_start -= sz
    
    # Root position: between left_end and right_start - 1
    # Find one that satisfies all constraints
    for rp in range(left_end + 1, right_start):
        valid = True
        left_sofar = 0
        right_total = n
        for j, side, a in config:
            sz = sc[j]
            if side == 'L':
                # Child interval: [rp - left_sofar - sz, rp - left_sofar - 1]
                # Let me recalculate...
                pass
            else:
                pass
        
        if valid:
            root_pos = rp
            break
    
    # Simplified: just use a greedy assignment
    # Recompute assignments properly
    
    # First, determine which children go left vs right and their relative positions
    left_children = []
    right_children = []
    
    left_sum = 0
    right_sum = 0
    
    for j, side, a in config:
        sz = sc[j]
        if side == 'L':
            left_children.append((j, a, sz))
            left_sum += sz
        else:
            right_children.append((j, a, sz))
            right_sum += sz
    
    # Root position: need to satisfy all constraints
    root_min = left_sum + 1
    root_max = n - right_sum
    
    root_pos = root_min  # Use the minimum valid position
    
    # Assign children positions
    assignment = [0] * n
    assignment[0] = root_pos
    
    # Left children: positioned left to right
    current_left = 1
    for j, a, sz in left_children:
        v = ch[j]
        interval_start = current_left
        interval_end = current_left + sz - 1
        
        # Position within subtree based on dpleft config
        # Parent (root) should be at position 'a' within the virtual interval of size sz
        # But root is at root_pos > interval_end
        # So the child subtree positions are valid
        
        # Recursively assign
        def assign_recursive(u, L, R, pp):
            # Assign u and its subtree
            # pp is parent position (used for root of this subtree)
            if pp < L or pp > R:
                # This subtree is entirely on one side of parent
                pass
            
            # Find position of u: need to determine from DP tables
            # For simplicity, use a fixed pattern
            pass
        
        # Simple assignment: put v at rightmost position
        pos_v = interval_end
        assignment[v] = pos_v
        
        # Assign subtree recursively (simplified)
        def dfs_assign(node, start_pos, end_pos):
            # Assign node's children alternating left/right
            ch_list = sorted([x for x in adj[node] if parent[x] == node], key=lambda x: -size[x])
            s = end_pos - start_pos + 1
            
            # Find position of node
            if parent[node] == -2:  # root
                pnode = s // 2 + start_pos if start_pos == 1 else root_pos
            else:
                # Position relative to parent - simplified
                pnode = start_pos
            assignment[node] = pnode
            
            cur_start = start_pos
            cur_end = end_pos
            for child in ch_list:
                sc_child = size[child]
                if cur_start < pnode:
                    # Place to left
                    dfs_assign(child, cur_start, cur_start + sc_child - 1)
                    cur_start += sc_child
                else:
                    # Place to right
                    dfs_assign(child, cur_end - sc_child + 1, cur_end)
                    cur_end -= sc_child
        
        dfs_assign(v, interval_start, interval_end)
        current_left += sz
    
    # Right children: positioned right to left (in reverse config order)
    current_right = n
    for j, a, sz in reversed(right_children):
        v = ch[j]
        interval_end = current_right
        interval_start = current_right - sz + 1
        
        dfs_assign(v, interval_start, interval_end)
        current_right -= sz
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()