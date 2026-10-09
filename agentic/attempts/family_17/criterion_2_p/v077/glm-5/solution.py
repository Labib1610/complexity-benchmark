import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    # Build adjacency list for bipartite graph
    # Left side: 1..q (Control Modules)
    # Right side: q+1..2q (Propulsion Units), remapped to 1..q
    head = [-1] * (q + 1)
    to = [0] * t
    nxt = [-1] * t
    
    idx = 2
    for i in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); idx += 2
        to[i] = b - q  # remap to 1..q
        nxt[i] = head[a]
        head[a] = i
    
    # Kuhn's algorithm for maximum bipartite matching
    match_r = [0] * (q + 1)  # match_r[v] = u means right v matched to left u
    # We need to find matching for all left nodes 1..q
    
    # Iterative DFS to avoid recursion limit
    for u in range(1, q + 1):
        # Try to find augmenting path from u
        stack = [(u, head[u], 0)]
        visited = [False] * (q + 1)
        found = False
        # We'll do iterative DFS
        # State: (current_left, edge_index, phase)
        # phase 0: exploring edges from left node
        # Actually let's do standard iterative DFS for augmenting path
        
        # Reset
        path = []
        # We use explicit stack
        # Each stack frame: (left_node, edge_iter, right_node_being_explored)
        # But simpler: do recursive-like with manual stack
        
        # Let's use a different approach: standard iterative DFS
        # stack contains (u, edge_idx) where edge_idx is current edge being processed from head[u]
        # We also need to track the path of right nodes
        
        # Actually, let's just use recursion with sys.setrecursionlimit
        # But q can be 100000, recursion might be deep. Let's do iterative.
        
        # Iterative DFS for augmenting path
        # We maintain a stack of (node, edge_index)
        # and a parent array for right nodes to reconstruct path
        
        parent = [0] * (q + 1)  # parent[v] = left node that discovered right node v
        stack = [u]
        # We need to track which edge we're at for each left node on stack
        edge_ptr = list(range(q + 1))  # not efficient, let's use dict or array
        
        # Actually, let's use a simpler iterative approach
        # For each left node u, we do DFS to find augmenting path
        
        # Reset visited
        # visited is for right nodes
        # We use parent to also mark visited (parent[v] != 0 means visited, except v=0)
        
        # Clear parent for this round
        # parent already initialized to 0
        
        # Stack of left nodes to process
        # But we need to iterate edges. Let's store (left_node, current_edge) on stack
        
        # Actually, let's just use recursion with increased limit
        # The depth of DFS is at most q, and with setrecursionlimit it should be fine
        # But Python recursion is slow. Let's do iterative properly.
        
        # Simple iterative DFS:
        # We process left node u, iterate its edges to find unvisited right node v
        # If v is unmatched, we found augmenting path
        # If v is matched to u', we push u' and continue
        
        # We need to track the path so we can augment
        # parent[v] = u means we reached right node v from left node u
        
        dfs_stack = [(u, head[u])]
        found = False
        aug_v = -1
        
        while dfs_stack:
            cur_u, cur_edge = dfs_stack[-1]
            if cur_edge == -1:
                # No more edges for this left node, backtrack
                dfs_stack.pop()
                continue
            
            # Get right node
            v = to[cur_edge]
            # Advance edge pointer for this node
            dfs_stack[-1] = (cur_u, nxt[cur_edge])
            
            if parent[v] != 0:
                # Already visited in this round
                continue
            
            parent[v] = cur_u
            
            if match_r[v] == 0:
                # v is unmatched, found augmenting path
                found = True
                aug_v = v
                break
            else:
                # v is matched to match_r[v], push it
                dfs_stack.append((match_r[v], head[match_r[v]]))
        
        if found:
            # Augment along path
            v = aug_v
            while v != 0:
                u_node = parent[v]
                prev_match = match_r[v]
                match_r[v] = u_node
                v = 0  # we're done after one step? No...
                # Actually the path is: u -> v1 -> u1 -> v2 -> u2 -> ... -> v (unmatched)
                # parent[v1] = u, match_r[v1] = u1, parent[v2] = u1, match_r[v2] = u2, ...
                # We need to flip: match_r[v] = u_node, then go to the right node that u_node was previously matched to
                # But u_node was previously matched to some right node? No...
                # Actually in augmenting path: u (unmatched) -> v1 (matched to u1) -> u1 -> v2 (matched to u2) -> ... -> v (unmatched)
                # After augmentation: u-v1, u1-v2, ..., prev_last-v
                # So match_r[v1] = u, match_r[v2] = u1, etc.
                # parent[v] = u_node gives us the left node. We set match_r[v] = u_node.
                # Then the previous match of u_node was... u_node was matched to some right node before?
                # No, u_node could be u (unmatched) or some matched left node.
                # If u_node = u (the starting node), it was unmatched, so we're done.
                # If u_node = match_r[some_v], then u_node was matched to some_v, and we need to find that.
                # Hmm, the parent array gives parent[v] = u_node, meaning we went u_node -> v.
                # If v was matched, match_r[v] = u_next, and parent[v_next] = u_next, etc.
                # So to augment: 
                #   match_r[v] = parent[v]  (new match)
                #   then we need to find the right node that parent[v] was previously matched to
                #   that right node is... we need to track it.
                
                # Actually, let me reconsider. The augmenting path is:
                # u -> v1 -> u1 -> v2 -> u2 -> ... -> vk (unmatched)
                # where u_i = match_r[v_i]
                # parent[v1] = u, parent[v2] = u1, ..., parent[vk] = u_{k-1}
                # After augmentation:
                # match_r[v1] = u, match_r[v2] = u1, ..., match_r[vk] = u_{k-1}
                # So we iterate: v = vk, match_r[v] = parent[v] = u_{k-1}
                #   then we need to go to v_{k-1} which was previously matched to u_{k-1}
                #   but we don't directly have v_{k-1} from u_{k-1}...
                
                # We need a different approach. Let's track the path differently.
                # Actually, the standard way: parent[v] = u means u -> v edge.
                # If v is matched to u' = match_r[v], then u' -> v' where parent[v'] = u'.
                # So the chain is: v -> parent[v] = u -> (u was matched to some v_prev?) 
                # No, u is a left node. If u != starting_u, then u = match_r[some_v_prev].
                # 
                # Let me think again. The augmenting path alternates:
                # left u (unmatched) -> right v1 (matched to u1) -> left u1 -> right v2 (matched to u2) -> ... -> right vk (unmatched)
                # parent[v1] = u, match_r[v1] = u1, parent[v2] = u1, match_r[v2] = u2, ..., parent[vk] = u_{k-1}, match_r[vk] = 0
                # 
                # Augmentation: match_r[v1] = u, match_r[v2] = u1, ..., match_r[vk] = u_{k-1}
                # 
                # So starting from vk:
                #   cur_v = vk
                #   cur_u = parent[cur_v] = u_{k-1}
                #   next_v = the v that was matched to cur_u before = v_{k-1}
                #     but how to find v_{k-1}? We know match_r[v_{k-1}] = u_{k-1} = cur_u
                #     but we don't know v_{k-1}...
                #   
                # Hmm, we need to also track the "previous right node" for each left node in the path.
                # Or we can just iterate: from vk, set match_r[vk] = parent[vk]. 
                #   Then the old match of parent[vk] is gone. But parent[vk] = u_{k-1} was matched to v_{k-1}.
                #   We need to find v_{k-1}. 
                #   v_{k-1} is the right node whose parent is... no.
                #   Actually, v_{k-1} is a right node such that match_r[v_{k-1}] = u_{k-1} = parent[vk].
                #   But we're about to change match_r, so we need to find it first.
                #   We can find it by: v_{k-1} is the right node v where parent[v] = u_{k-2} and match_r[v] = u_{k-1}.
                #   This is getting complicated.
                
                # Alternative: track the path as a list during DFS.
                # Or: use the standard approach where we store parent for left nodes too.
                
                # Let me use a different formulation:
                # parent_left[u'] = v means we reached left node u' from right node v
                # parent_right[v] = u means we reached right node v from left node u
                # 
                # Starting from left u (unmatched):
                #   u -> v1 (parent_right[v1] = u)
                #   v1 is matched to u1 (match_r[v1] = u1), so parent_left[u1] = v1
                #   u1 -> v2 (parent_right[v2] = u1)
                #   v2 is matched to u2, parent_left[u2] = v2
                #   ...
                #   u_{k-1} -> vk (parent_right[vk] = u_{k-1})
                #   vk is unmatched -> found!
                # 
                # Augmentation: walk back from vk
                #   match_r[vk] = parent_right[vk] = u_{k-1}
                #   then go to parent_left[u_{k-1}] = v_{k-1}
                #   match_r[v_{k-1}] = parent_right[v_{k-1}] = u_{k-2}
                #   then go to parent_left[u_{k-2}] = v_{k-2}
                #   ...
                #   match_r[v1] = parent_right[v1] = u
                #   parent_left[u] doesn't exist (u is starting node, unmatched)
                #   done!
                
                # This works! But I need to track parent_left too.
                # Let me redo the DFS with this approach.
                pass
            
            # Let me just redo this properly
            pass
        
        # I'll restart with a cleaner implementation
        pass
    
    # Let me just write a clean solution
    pass

def solve_clean():
    import sys
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    # Build adjacency list
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for i in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); idx += 2
        adj[a].append(b - q)  # remap right to 1..q
    
    match_r = [0] * (q + 1)  # match_r[v] = u
    
    # Iterative Kuhn's algorithm
    for u in range(1, q + 1):
        # DFS from u to find augmenting path
        parent_right = [0] * (q + 1)  # parent_right[v] = u (left node that discovered v)
        parent_left = [0] * (q + 1)   # parent_left[u] = v (right node that discovered u)
        
        stack = [u]
        parent_left[u] = -1  # mark as starting node
        found = False
        aug_v = -1
        
        while stack:
            cur_u = stack.pop()
            for v in adj[cur_u]:
                if parent_right[v] != 0:
                    continue
                parent_right[v] = cur_u
                if match_r[v] == 0:
                    # Found augmenting path
                    found = True
                    aug_v = v
                    break
                else:
                    # v is matched to match_r[v]
                    next_u = match_r[v]
                    parent_left[next_u] = v
                    stack.append(next_u)
            if found:
                break
        
        if found:
            # Augment
            v = aug_v
            while v != 0:
                u_node = parent_right[v]
                old_u = match_r[v]
                match_r[v] = u_node
                if parent_left[u_node] == -1:
                    break
                v = parent_left[u_node]
    
    # Check if all left nodes are matched
    match_l = [0] * (q + 1)
    for v in range(1, q + 1):
        if match_r[v] != 0:
            match_l[match_r[v]] = v
    
    for u in range(1, q + 1):
        if match_l[u] == 0:
            print("NO")
            return
    
    print("YES")
    out = []
    for u in range(1, q + 1):
        out.append(f"{u} {match_l[u] + q}")
    print("\n".join(out))

solve_clean()