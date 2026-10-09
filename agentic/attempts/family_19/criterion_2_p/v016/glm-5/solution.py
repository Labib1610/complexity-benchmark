import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    n = int(next(iterator))
    m = int(next(iterator))
    _ = int(next(iterator)) # commodity type, always 1
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        edges.append((u, v, cap))
        adj[u].append((v, i, cap))
        adj[v].append((u, i, 0)) # residual edge info for graph building
    
    # Dinic's Algorithm
    # Edge structure: (to, rev_index, capacity)
    graph = [[] for _ in range(n + 1)]
    edge_capacity = [0] * (2 * m)
    
    for i, (u, v, cap) in enumerate(edges):
        # Forward edge index: 2*i
        graph[u].append((v, len(graph[v]), cap))
        # Backward edge index: 2*i + 1
        graph[v].append((u, len(graph[u]) - 1, 0))
    
    level = [0] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v, rev_idx, cap in graph[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[t] != -1
    
    def dfs(u, flow):
        if u == t:
            return flow
        while ptr[u] < len(graph[u]):
            v, rev_idx, cap = graph[u][ptr[u]]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap))
                if pushed > 0:
                    # Update capacities
                    graph[u][ptr[u]] = (v, rev_idx, cap - pushed)
                    # The reverse edge is stored at graph[v][rev_idx]
                    # We need its current capacity to update it
                    current_rev_cap = graph[v][rev_idx][2]
                    graph[v][rev_idx] = (u, graph[v][rev_idx][1], current_rev_cap + pushed)
                    return pushed
            ptr[u] += 1
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * (n + 1)
        while True:
            pushed = dfs(s, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow >= d:
        print("YES")
        # Extract flow values for original edges
        # The flow on edge i is original_cap - current_cap of forward edge
        # Forward edges are at even indices in the flattened adjacency list if we tracked it,
        # but here we stored them sequentially.
        # We iterate through the original edges list.
        # For edge i (u->v), it corresponds to graph[u][some_index].
        # We can find it because we added edges in order.
        
        # Let's reconstruct the flow on each original edge.
        # When we added edge i, we did:
        # graph[u].append((v, ..., cap))
        # graph[v].append((u, ..., 0))
        # So for edge i, the forward edge is the 2*i-th edge added to the graph in total?
        # No, graph[u] and graph[v] are separate lists.
        # However, we can iterate through graph[u] to find the edge going to v with original capacity.
        # Or simpler: the forward edge for input edge i is at graph[edges[i].u][2*i] is wrong.
        
        # Let's rely on the fact that we added edges in order.
        # For input edge i, we added one edge to graph[u] and one to graph[v].
        # We can find the flow by checking the residual capacity of the forward edge.
        
        res = []
        for i, (u, v, original_cap) in enumerate(edges):
            # Find the edge in graph[u] that corresponds to this original edge.
            # Since we added edges sequentially, the forward edge for input edge i
            # is the i-th edge added to graph[u]?
            # No, multiple edges can start from u.
            
            # We need to identify which entry in graph[u] is the forward edge for input edge i.
            # We can iterate through graph[u] to find (v, ..., cap).
            # But there might be multiple edges u->v.
            # However, we added them one by one.
            # Let's just iterate through graph[u] and find the edge pointing to v.
            # To handle parallel edges correctly, we can consume them.
            # Actually, since we iterate input edges in order 0..m-1,
            # and we added forward edges to graph[u] in that order,
            # we can maintain pointers or just search.
            
            # Search for the forward edge
            flow_val = 0
            for idx, (to, rev_idx, cap) in enumerate(graph[u]):
                if to == v:
                    # Check if this is the forward edge (original cap > 0)
                    # Backward edges were initialized with 0.
                    # But after flow, forward cap decreases, backward cap increases.
                    # We need to distinguish between original forward edge and residual backward edge.
                    # Original forward edge had original_cap.
                    # Backward edge had 0.
                    # If original_cap > 0, then this must be the forward edge.
                    # But we don't have original_cap handy here without lookup.
                    # Wait, edges list has original_cap.
                    # We look for an edge u->v.
                    # If there are parallel edges u->v, we need to match the correct one.
                    # We added them in order. So the first match we find is the first one added?
                    # Not necessarily, if we added u->v, then u->w, then u->v again.
                    # The graph[u] list will have them in order of addition.
                    # So we can just pick the first valid u->v edge.
                    # But we must ensure we don't pick the backward edge of some other flow.
                    # Backward edges are added to graph[v], not graph[u].
                    # So graph[u] only contains edges starting from u (forward) and backward edges of edges ending at u.
                    # Backward edge in graph[u] would be (neighbor, ..., cap) where neighbor has an edge to u.
                    # So if we look for edge u->v, we look for `to == v`.
                    # Is it possible we find a backward edge? 
                    # Backward edge in graph[u] corresponds to an edge v->u.
                    # So `to` would be v. This is a backward edge for v->u.
                    # If we have both u->v and v->u, graph[u] contains forward for u->v and backward for v->u.
                    # Both have `to == v`.
                    # We need to pick the one that corresponds to the input edge i.
                    # Input edge i is u->v.
                    # The forward edge for u->v was initialized with `cap`.
                    # The backward edge for v->u was initialized with 0.
                    # If we have both u->v and v->u in input.
                    # Input edge u->v: graph[u] gets (v, ..., cap_u_v). graph[v] gets (u, ..., 0).
                    # Input edge v->u: graph[v] gets (u, ..., cap_v_u). graph[u] gets (v, ..., 0).
                    # In graph[u], we have two entries with `to == v`.
                    # One is forward (cap_u_v), one is backward (0).
                    # We want the forward one.
                    # We can distinguish by checking if the edge was originally a forward edge.
                    # We don't store that flag.
                    # However, we know the flow is `original_cap - current_cap`.
                    # For the backward edge (originally 0), flow would be 0 - current_cap (negative or zero).
                    # We are only interested in non-negative flows.
                    # Also, we can just iterate and find the edge.
                    # To be safe against parallel edges, we can consume the edge (set cap to -1 or similar) or track indices.
                    # Given the constraints, simple search and match is likely fine.
                    # But we must be careful.
                    
                    # Correct approach for extraction:
                    # The flow on edge i is `original_cap - residual_cap`.
                    # We need to find the residual cap of the forward edge.
                    # We iterate `graph[u]` to find the edge `to=v`.
                    # We need to make sure we pick the one corresponding to edge `i`.
                    # Since we added edges in order, we can maintain a counter for each node `u`
                    # of how many edges we have "used" for extraction.
                    
                    pass
            
            # Let's use a more robust extraction.
            # We iterate through graph[u] and find the edge to v.
            # We calculate flow. If flow >= 0, that's our flow.
            # We must handle the case where we pick the wrong edge (backward edge of v->u).
            # If we pick the backward edge of v->u, its original cap was 0.
            # Current cap is `flow_v_u` (increased).
            # So `original_cap - current_cap` = `0 - flow_v_u` <= 0.
            # We want positive flow.
            # So we pick the edge where `original_cap - current_cap` matches expected flow?
            # We don't know expected flow.
            # But we know `original_cap` from input.
            # We look for the edge in `graph[u]` with `to=v` such that `original_cap - current_cap >= 0`.
            # Actually, we just need to find the forward edge.
            # The forward edge was added to `graph[u]` when we processed input edge `i`.
            # The backward edge was added to `graph[u]` when we processed some input edge `v->u`.
            # If there are multiple `u->v` edges, we need to match them.
            # We can iterate through `graph[u]` and find the first edge `to=v` that has not been "visited".
            # We can mark it as visited.
            
            # Actually, simpler:
            # We know for input edge i (u->v), we added a forward edge to graph[u].
            # We can find it by iterating graph[u] and checking `to=v`.
            # If multiple matches, we pick one. But we must ensure consistency.
            # Since we iterate input edges in order, and we added them in order,
            # the forward edges in `graph[u]` appear in the order they were added.
            # We can maintain a pointer `edge_ptr[u]` for each node `u`.
            # For edge i (u->v), we scan `graph[u]` starting from `edge_ptr[u]`
            # to find the first edge with `to=v`.
            # This works because edges in `graph[u]` are in insertion order.
            # Forward edges are inserted when processing input edge.
            # Backward edges are inserted when processing reverse input edge.
            # If we have u->v then v->u then u->v again.
            # graph[u] gets: Fwd(u->v), Back(v->u), Fwd(u->v).
            # Processing 1st u->v: scan finds Fwd(u->v). Correct.
            # Processing v->u: scan graph[v]. Finds Fwd(v->u). Correct.
            # Processing 2nd u->v: scan graph[u] continues. Finds Back(v->u)? No, `to` is v.
            # Back(v->u) has `to=u`. So it's skipped.
            # Finds 2nd Fwd(u->v). Correct.
            # So this logic works.
            pass
            
        # Implementing the pointer-based extraction
        edge_ptr = [0] * (n + 1)
        flows = []
        for i, (u, v, original_cap) in enumerate(edges):
            # Find forward edge in graph[u]
            idx = edge_ptr[u]
            while idx < len(graph[u]):
                to, rev_idx, cap = graph[u][idx]
                if to == v:
                    # Found candidate
                    # Calculate flow
                    flow = original_cap - cap
                    flows.append(str(flow))
                    edge_ptr[u] = idx + 1
                    break
                idx += 1
            else:
                # Should not happen if graph is constructed correctly
                flows.append("0")
        
        print(" ".join(flows))
    else:
        print("NO")

if __name__ == '__main__':
    solve()