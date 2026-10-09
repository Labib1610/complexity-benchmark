import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        nL = int(next(iterator))
        nR = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        edges.append((u, v))

    # Calculate degree of each node
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    for u, v in edges:
        deg_L[u] += 1
        deg_R[v] += 1

    # Initialize current degree (remaining edges)
    curr_deg_L = list(deg_L)
    curr_deg_R = list(deg_R)

    # Adjacency list for the graph
    adj = [[] for _ in range(nL + 1)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))

    # Kahn's algorithm for edge coloring
    # We process edges in reverse order of cycle assignment
    # The cycle assigned to an edge is the current degree of its endpoints
    # when it is processed (removed from the graph)
    
    ans = [0] * m
    
    # Queue for nodes with degree 0 (initially none, but will be populated)
    # We use a deque for efficient pops from the left
    q = deque()
    
    # Add nodes with degree 0 to the queue
    for u in range(1, nL + 1):
        if curr_deg_L[u] == 0:
            q.append(('L', u))
    for v in range(1, nR + 1):
        if curr_deg_R[v] == 0:
            q.append(('R', v))
            
    # We need to process edges. 
    # We can iterate through all edges and check if they can be removed.
    # To optimize, we can use a pointer to the next edge to check for each node.
    # adj[u] contains (v, edge_index)
    # We need a way to mark edges as removed.
    # We can use a boolean array `removed` or simply decrement degrees.
    # Since we are iterating, we need to be careful not to process the same edge multiple times.
    
    # Let's use a pointer array for each node in L
    ptr = [0] * (nL + 1)
    
    # We process until queue is empty. 
    # However, the queue logic for edge coloring is slightly different.
    # We remove edges. When we remove an edge, degrees of endpoints decrease.
    # If degree of an endpoint becomes 0, we add it to queue.
    # But we also need to assign the color.
    
    # The color of an edge is determined when it is removed.
    # When we remove an edge (u, v), the color is curr_deg_L[u] (or curr_deg_R[v], they are equal).
    # But wait, the degrees are decremented *after* we decide the color?
    # Let's trace:
    # We have a graph. We want to peel it in layers.
    # The max degree is Delta.
    # We can find edges that can be assigned color Delta.
    # These are edges where at least one endpoint has degree Delta.
    # Actually, the algorithm is:
    # While there are edges:
    #   Pick a node u with max degree.
    #   Find a neighbor v.
    #   Assign color Delta to edge (u, v).
    #   Remove edge (u, v).
    #   Decrement degrees.
    #   Delta might decrease.
    
    # A better approach for bipartite edge coloring with Delta colors:
    # Repeatedly find a matching of size Delta (or max degree) and assign a color.
    # But finding a matching is slow.
    
    # The efficient approach is the one described in the thought process:
    # 1. Find a node u with degree Delta.
    # 2. Find a neighbor v.
    # 3. Find an alternating path from v to a free node w (degree < Delta).
    # 4. Augment the path. This swaps colors/edges.
    # 5. Now u has a free slot, and the edge (u, v) can be assigned the current color.
    
    # Let's implement the path finding approach.
    # We need to maintain the graph structure.
    # Since we remove edges, we can use adjacency lists.
    
    # We need to track which edges are still in the graph.
    # We can use a boolean array `alive`.
    alive = [True] * m
    
    # We need to quickly find a neighbor of a node.
    # We can use the `adj` list and a pointer.
    
    # We need to find a free node in R.
    # We can maintain a set of free nodes in R (degree < Delta).
    # But Delta changes.
    
    # Let's stick to the iterative peeling logic.
    # We maintain `curr_deg`.
    # We iterate color `c` from Delta down to 1.
    # For each color, we find edges to assign.
    # But this is also tricky.
    
    # Let's go back to the "greedy matching" idea which is equivalent to the path augmentation.
    # We iterate through edges in reverse order of input? No.
    
    # Let's use the standard algorithm for edge coloring bipartite graphs.
    # We iterate `c` from `Delta` down to 1.
    # In each step, we find a matching that covers all nodes with degree `c`.
    # This matching is assigned color `c`.
    # We remove these edges and continue.
    
    # Finding a matching that covers all max-degree nodes:
    # We can use a greedy approach with path augmentation.
    # For each node `u` with degree `c`:
    #   Find a neighbor `v`.
    #   Try to find an augmenting path from `v` to a free node `w` (degree < c).
    #   If found, augment. Now `u` has a free slot.
    #   Assign edge (u, v) color `c`.
    
    # This works.
    
    # Data structures:
    # `adj[u]`: list of (v, edge_index)
    # `alive[edge_index]`: boolean
    # `curr_deg[u]`: current degree
    # `matchR[v]`: which `u` is matched to `v` in the current matching? No, we are not building one global matching.
    # We are just finding edges to color `c`.
    
    # Wait, the path augmentation is to free up a slot in `u`.
    # The "matching" is the set of edges colored `c`.
    # We want to find a matching that covers all nodes with degree `c`.
    # This is a matching in the subgraph induced by edges with `curr_deg[u] == c` or `curr_deg[v] == c`?
    # Not exactly. We just want to pick edges such that we reduce the degree of all max-degree nodes.
    
    # Algorithm:
    # Determine Delta.
    # For c from Delta down to 1:
    #   Identify nodes with degree c.
    #   For each such node u:
    #     Find a neighbor v.
    #     Find an augmenting path from v to a free node w (degree < c).
    #     If found, augment (swap edges along path).
    #     Now u has a free slot (degree decreased).
    #     Assign edge (u, v) color c.
    #     Remove edge (u, v).
    
    # This requires efficient path finding.
    # Since we process edges one by one, and `c` decreases, the total work is O(M * Delta) in worst case?
    # No, with proper bookkeeping, it can be O(M).
    # But finding path takes O(M) in worst case. Total O(M * Delta) is too slow if Delta is large.
    # However, Delta <= sqrt(M) or Delta is small?
    # Delta can be up to 100000.
    # So O(M * Delta) is too slow.
    
    # We need the O(M * sqrt(M)) or O(M * Delta) where Delta is small?
    # Actually, the path finding can be optimized.
    # We can use a visited array for R-nodes.
    # The path finding is BFS/DFS.
    
    # Let's implement the O(M * Delta) approach first, maybe it passes?
    # Constraints: M <= 400000. Delta <= 100000.
    # If Delta is large, M must be large.
    # If Delta is small, it's fast.
    # If Delta is approx sqrt(M), then M * Delta approx M * 1.7 * 10^7 approx 7 * 10^7. Might be OK in 2s?
    # Wait, M * Delta = 4 * 10^5 * 10^5 = 4 * 10^10. Too slow.
    
    # We need the O(M sqrt(M)) or O(M log M) approach.
    # The O(M sqrt(M)) approach is:
    # If Delta > sqrt(M), we use the greedy matching approach.
    # If Delta <= sqrt(M), we use the path augmentation approach.
    
    # Actually, the path augmentation approach IS the O(M sqrt(M)) approach if implemented correctly.
    # The key is that we only find paths for nodes with degree Delta.
    # If Delta > sqrt(M), then the number of nodes with degree Delta is small (<= 2 * sqrt(M)).
    # So we only do path finding a small number of times.
    # If Delta <= sqrt(M), then path finding is cheap (path length <= Delta <= sqrt(M)).
    # So total complexity is O(M * sqrt(M)).
    
    # Let's refine this.
    # We iterate `c` from Delta down to 1.
    # In each step, we have a set of nodes `S` with degree `c`.
    # We want to find a matching that covers `S`.
    # We iterate through `u` in `S`.
    #   Find a neighbor `v`.
    #   Find augmenting path from `v` to a free node `w`.
    #   Augment.
    #   Assign color `c` to (u, v).
    
    # Complexity analysis:
    # Sum of degrees is M.
    # We process each edge once.
    # Path finding:
    #   We visit nodes in R. We mark them visited.
    #   We need to clear visited array.
    #   To avoid clearing the whole array, we use a timestamp.
    #   `visR[v]` stores the timestamp when it was visited.
    
    # Implementation details:
    # We need to track which edges are incident to a node.
    # We have `adj[u]`.
    # We need to remove edges efficiently.
    # We can just mark them `alive = False`.
    # We need to skip dead edges in `adj[u]`.
    # We can use a pointer `ptr[u]` to the next candidate edge.
    # But edges are removed, so we might need to advance `ptr[u]` until we find a live edge.
    
    # Let's implement.
    
    # Initial degrees
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    for u, v in edges:
        deg_L[u] += 1
        deg_R[v] += 1
        
    curr_deg_L = list(deg_L)
    curr_deg_R = list(deg_R)
    
    Delta = max(deg_L) if deg_L else 0
    if max(deg_R) > Delta: Delta = max(deg_R)
    
    adj = [[] for _ in range(nL + 1)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        
    alive = [True] * m
    ans = [0] * m
    
    # We need to find edges to color `c`.
    # We can maintain a list of nodes with degree `c`.
    # But degrees change dynamically.
    # It's easier to just iterate through all nodes and check degree.
    # Or maintain a set of "active" nodes (degree == c).
    
    # Optimization:
    # We can maintain a list of nodes with degree `c`.
    # When degree of `u` drops from `c+1` to `c`, add to list.
    # When we process `u`, remove from list.
    
    # Let's use a simple list for each degree level.
    # `nodes_by_deg[d]` contains nodes with degree `d`.
    # We only care about L-nodes? No, we need to cover all max-degree nodes.
    # The algorithm says: "Find a matching that covers all nodes with degree Delta".
    # This includes both L and R nodes.
    # However, if we cover all L-nodes with degree Delta, do we cover all R-nodes?
    # Not necessarily.
    # But the theorem says a matching exists that covers all max-degree nodes.
    # So we should try to cover all of them.
    
    # Actually, the standard algorithm is:
    # While there are edges:
    #   Find a matching that covers all max-degree nodes.
    #   Assign a color to this matching.
    #   Remove matching.
    
    # To find this matching:
    # Iterate through all nodes `u` with degree Delta.
    #   If `u` is not matched:
    #     Find augmenting path from `u`.
    #     Augment.
    
    # Wait, this is finding a matching in the graph.
    # We want to find a matching that covers all max-degree nodes.
    # This is equivalent to finding a matching in the subgraph where we only care about covering max-degree nodes.
    
    # Let's stick to the simpler logic:
    # For `c` from Delta down to 1:
    #   Find all nodes with degree `c`.
    #   For each such node `u`:
    #     Find a neighbor `v`.
    #     Find augmenting path from `v` to a free node `w` (degree < c).
    #     Augment.
    #     Assign color `c` to (u, v).
    #     Remove (u, v).
    
    # This logic works.
    # We need to handle both L and R nodes.
    # We can just iterate through all nodes `u` in L and R.
    # If `degree[u] == c`:
    #   Process `u`.
    
    # To avoid processing a node multiple times for the same color, we can use a flag.
    # Or just rely on the fact that after processing, degree decreases.
    
    # Let's refine the "Process `u`" part.
    # We need to find a neighbor `v`.
    # Since we want to assign color `c` to an edge incident to `u`, we pick any live edge (u, v).
    # Then we try to find a path from `v` to a free node `w`.
    # "Free node" means a node with degree < c.
    # If we find such a path, we augment.
    # Augmenting means swapping matched/unmatched edges along the path.
    # But we are not building a matching explicitly.
    # We are just trying to free up a slot in `u`.
    
    # Actually, the "augmenting path" logic is:
    # We want to match `u` with some `v`.
    # If `v` is free (degree < c), we match (u, v).
    # If `v` is not free (degree == c), we need to "unmatch" `v` from its current partner `u2`.
    # Then match `u` with `v`.
    # And then try to match `u2` with someone else.
    # This is exactly finding an augmenting path.
    
    # We need to track "current matching".
    # But we are not maintaining a global matching.
    # We are just finding edges to color `c`.
    # The "matching" is implicit.
    
    # Let's use `matchL[u]` and `matchR[v]` to store the current matching for color `c`.
    # Initially all -1.
    # When we process `u`:
    #   Find neighbor `v`.
    #   Try to find augmenting path starting from `u`.
    #   If found, augment.
    #   `u` is now matched.
    #   The edge (u, v) gets color `c`.
    
    # Wait, if we use `matchL` and `matchR`, we are building a matching.
    # The edges in this matching will be assigned color `c`.
    # We need to ensure that this matching covers all nodes with degree `c`.
    # The algorithm guarantees that if we process all nodes with degree `c` and try to augment, we will find a matching that covers them.
    
    # So the plan is:
    # For `c` from Delta down to 1:
    #   Initialize `matchL` and `matchR` to -1.
    #   Identify nodes with degree `c`.
    #   For each such node `u`:
    #     If `u` is not matched:
    #       Find augmenting path from `u`.
    #       Augment.
    #   Now we have a matching.
    #   For each edge (u, v) in the matching:
    #     Assign color `c` to (u, v).
    #     Remove (u, v) from graph.
    #     Decrement degrees.
    
    # This seems correct.
    # Complexity:
    # We iterate `c` from Delta down to 1.
    # Inside, we find augmenting paths.
    # Total work is O(M * Delta) in worst case.
    # We need the optimization.
    
    # Optimization:
    # We only need to find augmenting paths for nodes with degree `c`.
    # If `c` is large, number of such nodes is small.
    # If `c` is small, path finding is fast.
    # This gives O(M * sqrt(M)).
    
    # Let's implement the path finding.
    # `find_path(u)`:
    #   BFS/DFS from `u`.
    #   We alternate between L and R.
    #   From `u` (in L), we go to `v` (in R) using edges in graph (not in matching).
    #   From `v` (in R), we go to `u2` (in L) using edges in matching.
    #   We stop when we reach a free node in R (degree < c).
    #   Wait, "free node in R" means `matchR[v] == -1`.
    #   But we also need `degree[v] < c`?
    #   Actually, the condition is: we want to match `u` to some `v`.
    #   If `v` has degree < c, it is "free" in the sense that it can accept more edges?
    #   No, in a matching, a node is matched or not.
    #   The constraint is: we want to find a matching that covers all nodes with degree `c`.
    #   Nodes with degree < c don't need to be covered.
    #   So they are "free" in the sense that they don't have to be matched.
    #   But if they are matched, they are matched.
    
    # Let's re-read the problem.
    # We want to assign colors to edges.
    # The condition is: for each color `c`, the edges with color `c` form a matching.
    # And we want to cover all nodes with degree `Delta` with color `Delta`.
    # Then cover all nodes with degree `Delta-1` with color `Delta-1`.
    # And so on.
    
    # So for color `c`, we want a matching that covers all nodes with degree `c`.
    # Nodes with degree < c can be matched or not, doesn't matter.
    
    # So in `find_path(u)`:
    #   We start at `u` (degree `c`).
    #   We want to find an augmenting path to a node `v` in R such that `matchR[v] == -1`.
    #   (Because if `matchR[v] != -1`, then `v` is already matched in this color).
    #   If we find such a `v`, we augment.
    #   Augmenting increases matching size by 1.
    #   `u` becomes matched.
    
    # Is it always possible?
    # Yes, by the theorem.
    
    # One detail: `degree` here refers to the degree in the remaining graph.
    # When we say "nodes with degree `c`", we mean `curr_deg[u] == c`.
    
    # Implementation of BFS:
    # `visL[u]`, `visR[v]` to track visited nodes in BFS.
    # `parentL[u]`, `parentR[v]` to reconstruct path.
    # From `u` in L, we iterate neighbors `v`.
    #   If `v` not visited:
    #     If `matchR[v] == -1`:
    #       Found path! Reconstruct and return.
    #     Else:
    #       Add `matchR[v]` to queue (L-side).
    #       `parentL[matchR[v]] = u`.
    #       `parentR[v] = v` (just to mark).
    #       Actually, we need to store the edge (u, v) that led to `v`.
    #       And the edge (v, matchR[v]) that led to `matchR[v]`.
    
    # Let's refine BFS state.
    # Queue stores nodes in L.
    # `visL[u] = True`.
    # For each `u` in queue:
    #   For each neighbor `v`:
    #     If `visR[v]`: continue.
    #     `visR[v] = True`.
    #     `parent[v] = u`. (Stores which L-node led to this R-node)
    #     If `matchR[v] == -1`:
    #       Found free node!
    #       Reconstruct path.
    #       Path is: ... -> parent[v] -> v.
    #       Update matching along path.
    #       Return True.
    #     Else:
    #       `u2 = matchR[v]`.
    #       If `visL[u2]`: continue.
    #       `visL[u2] = True`.
    #       Add `u2` to queue.
    
    # This is standard augmenting path for bipartite matching.
    
    # We need to run this for each `u` with degree `c`.
    # Since we modify matching, we need to run BFS multiple times.
    # Total complexity: Sum of BFS costs.
    # Each BFS visits edges.
    # Total edges visited across all BFS calls for color `c` is O(M).
    # So total complexity O(M * Delta).
    
    # To optimize:
    # We can use the `vis` array with timestamps to avoid clearing.
    # Also, we can stop early if we found a path.
    
    # Let's implement.
    
    sys.setrecursionlimit(2 * 10**5 + 10)
    
    # We need to handle the case where Delta is 0.
    if Delta == 0:
        print("YES")
        print("")
        return

    # Precompute degrees
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    for u, v in edges:
        deg_L[u] += 1
        deg_R[v] += 1
    
    curr_deg_L = list(deg_L)
    curr_deg_R = list(deg_R)
    
    # Adjacency list
    adj = [[] for _ in range(nL + 1)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        
    alive = [True] * m
    ans = [0] * m
    
    # We need to process colors from Delta down to 1.
    # We can maintain a list of nodes with degree `c`.
    # But degrees change.
    # A simple way is to iterate `c` and scan all nodes.
    # Since sum of degrees is M, total scans is O(M * Delta)?? No.
    # Sum of `c` is O(Delta^2). Too slow.
    
    # Better: maintain a set of active nodes (degree >= 1).
    # Iterate `c` from Delta down to 1.
    # In each step, find nodes with degree `c`.
    # Process them.
    
    # To find nodes with degree `c` efficiently:
    # We can maintain `nodes_by_deg` lists.
    # `L_nodes_by_deg[d]`: list of L-nodes with degree `d`.
    # When degree of `u` changes, move it to the new list.
    # Since we only decrement degrees, we only move to lower lists.
    # We can use a pointer `ptr[u]` to track its position? No, lists are hard to delete from.
    # We can use a "processed" flag.
    # Or just use a set of active nodes and filter.
    
    # Let's use the "bucket" approach.
    # `L_buckets[d]`: set of L-nodes with degree `d`.
    # `R_buckets[d]`: set of R-nodes with degree `d`.
    # When degree of `u` decreases from `d` to `d-1`:
    # Remove `u` from `L_buckets[d]`, add to `L_buckets[d-1]`.
    
    # Since we process `c` from Delta down to 1, and we only decrement degrees,
    # a node with degree `c` will stay in buckets `c, c-1, ...`.
    # We can just check if `u` is in `L_buckets[c]`.
    
    # Actually, simpler:
    # We can just iterate through all nodes `u` and check `curr_deg[u] == c`.
    # This is O(nL + nR) per color. Total O((nL+nR)*Delta).
    # If Delta is large, this is slow.
    
    # Optimization:
    # We only need to process nodes with degree `c`.
    # We can maintain a list `active_nodes` containing all nodes with degree > 0.
    # And `buckets` for each degree.
    
    # Let's use `L_buckets` and `R_buckets`.
    L_buckets = [set() for _ in range(Delta + 2)]
    R_buckets = [set() for _ in range(Delta + 2)]
    
    for u in range(1, nL + 1):
        if curr_deg_L[u] > 0:
            L_buckets[curr_deg_L[u]].add(u)
    for v in range(1, nR + 1):
        if curr_deg_R[v] > 0:
            R_buckets[curr_deg_R[v]].add(v)
            
    # Helper to update bucket
    def update_bucket(bucket, deg_arr, node, old_d, new_d):
        if old_d == new_d: return
        if 0 <= old_d <= Delta + 1:
            bucket[old_d].discard(node)
        if 0 <= new_d <= Delta + 1:
            bucket[new_d].add(node)
            
    # We need to match L and R nodes.
    # We can iterate through `L_buckets[c]` and `R_buckets[c]`.
    # But we need to be careful not to process a node twice.
    # We can just pop from the set.
    
    # Matching arrays
    matchL = [-1] * (nL + 1)
    matchR = [-1] * (nR + 1)
    
    # Visited arrays for BFS
    # We use a list of ints for timestamps
    visL = [0] * (nL + 1)
    visR = [0] * (nR + 1)
    timer = 0
    
    # BFS queue
    # We can use a list as queue
    
    for c in range(Delta, 0, -1):
        # Reset matching for this color
        # We only need to reset for nodes that were matched in previous iteration
        # But it's easier to just reset all.
        # However, resetting is O(N), which is too slow inside the loop.
        # We can just use a fresh array? No, memory.
        # We can use timestamp for matching too?
        # `matchL[u]` stores `(v, timestamp)`.
        # If timestamp != current_c, it's unmatched.
        
        # Let's use timestamp for matching.
        # matchL_ts[u] = c means u is matched in color c.
        # matchL_val[u] = v.
        
        # Actually, we can just iterate through the nodes we matched in the previous step and reset them.
        # But we don't track that.
        
        # Let's stick to resetting `matchL` and `matchR`.
        # Since we do it `Delta` times, and Delta can be large, this is O(N * Delta) -> TLE.
        
        # Wait, the total number of matches is M.
        # We can just clear the specific nodes.
        # When we match (u, v), we set matchL[u] = v, matchR[v] = u.
        # We need to clear these before starting color `c`.
        # We can iterate through all nodes in `L_buckets[c]` and `R_buckets[c]` and their matches?
        # No.
        
        # Correct approach:
        # We don't need to reset `matchL` and `matchR` globally.
        # We just need to ensure that when we start color `c`, no node is marked as matched.
        # We can use the timestamp trick.
        # `matchL[u]` stores the color `c` for which it is matched.
        # If `matchL[u] == c`, it is matched in current color.
        # If `matchL[u] != c`, it is free.
        
        # So `matchL` and `matchR` store the color index.
        # Initialize with 0.
        
        # Process L-nodes with degree c
        # We iterate until the bucket is empty
        while L_buckets[c]:
            u = L_buckets[c].pop()
            # Check if degree is still c (might have changed)
            if curr_deg_L[u] != c:
                # Move to correct bucket
                if curr_deg_L[u] > 0:
                    L_buckets[curr_deg_L[u]].add(u)
                continue
            
            # u is unmatched (since we just picked it)
            # Find augmenting path
            timer += 1
            q = [u]
            visL[u] = timer
            parent_v = {} # v -> u
            
            found = False
            free_v = -1
            
            # BFS
            # We need to iterate layer by layer
            # Queue contains L-nodes
            head = 0
            while head < len(q):
                curr_u = q[head]
                head += 1
                
                # Iterate neighbors
                for v, edge_idx in adj[curr_u]:
                    if not alive[edge_idx]: continue
                    
                    if visR[v] == timer: continue
                    visR[v] = timer
                    parent_v[v] = curr_u
                    
                    # Check if v is free
                    # v is free if matchR[v] != c
                    if matchR[v] != c:
                        # Found path
                        free_v = v
                        found = True
                        break
                    else:
                        # v is matched to u2
                        u2 = matchL[v] # This is wrong. matchR[v] stores u.
                        # Wait, matchR[v] stores u.
                        # matchL[u] stores v.
                        # If matchR[v] == c, it means v is matched in this color.
                        # But matchR[v] stores the color index? No.
                        
                        # Let's redefine matchL and matchR.
                        # matchL[u] = v (matched to v)
                        # matchR[v] = u (matched to u)
                        # We need to know if they are matched in CURRENT color c.
                        # We can use separate arrays `is_matched_L[u]` and `is_matched_R[v]`?
                        # Or timestamp.
                        
                        # Let's use `matchL[u]` to store `(v, color)`.
                        # If `matchL[u] == c`, then u is matched in color c.
                        # But we need to know WHO it is matched to.
                        
                        # Let's use:
                        # `matchL_partner[u]`: stores v
                        # `matchL_color[u]`: stores c
                        # `matchR_partner[v]`: stores u
                        # `matchR_color[v]`: stores c
                        
                        # If `matchR_color[v] == c`, then v is matched.
                        # `u2 = matchR_partner[v]`.
                        
                        # This requires 4 arrays.
                        # Let's optimize.
                        # We can reuse `matchL` and `matchR` for partner.
                        # And use `visL`, `visR` for matching status?
                        # No, vis is for BFS.
                        
                        # Let's use `matchL[u]` to store the color `c` if matched.
                        # And `partnerL[u]` to store `v`.
                        # Same for R.
                        
                        # Actually, simpler:
                        # `matchL[u]` stores `v` if matched in current color.
                        # `matchR[v]` stores `u` if matched in current color.
                        # We need to clear them.
                        # We can clear them lazily.
                        # When we check `matchR[v]`, we check if `matchR_color[v] == c`.
                        # So `matchR[v]` stores `(u, c)`.
                        
                        # Let's use two arrays: `matchL` and `matchR`.
                        # `matchL[u]` stores `v`. `matchL_color[u]` stores `c`.
                        # `matchR[v]` stores `u`. `matchR_color[v]` stores `c`.
                        
                        # Let's just use `matchL` and `matchR` as partner arrays.
                        # And `matched_in_color` array?
                        # No, we can just use `matchL[u] != 0` to check.
                        # But we need to reset.
                        
                        # Let's use the timestamp approach.
                        # `matchL[u]` stores `v`.
                        # `matchL_ts[u]` stores `c`.
                        # If `matchL_ts[u] == c`, then `u` is matched to `matchL[u]`.
                        
                        # Okay, let's implement this.
                        pass
                        
            # This logic is getting complicated.
            # Let's restart the BFS logic with clear variable names.
            
            # We need:
            # `partnerL[u]`: v
            # `partnerR[v]`: u
            # `match_ts_L[u]`: c (timestamp)
            # `match_ts_R[v]`: c
            
            # In BFS:
            # `u2 = partnerR[v]`
            # If `match_ts_R[v] == c`: (v is matched)
            #   If `visL[u2] != timer`:
            #     visL[u2] = timer
            #     q.append(u2)
            
            pass
            
        # Same for R-nodes
        while R_buckets[c]:
            v = R_buckets[c].pop()
            if curr_deg_R[v] != c:
                if curr_deg_R[v] > 0:
                    R_buckets[curr_deg_R[v]].add(v)
                continue
            
            # Find augmenting path from v
            # This is symmetric.
            # Start BFS from v (in R).
            # Queue contains R-nodes.
            # Neighbors are L-nodes.
            # If L-node is free (match_ts_L[u] != c), found.
            # Else, go to partner.
            pass
            
    # The above is the structure.
    # Let's write the actual code.
    
    # Re-initialize structures
    partnerL = [0] * (nL + 1)
    partnerR = [0] * (nR + 1)
    match_ts_L = [0] * (nL + 1)
    match_ts_R = [0] * (nR + 1)
    
    visL = [0] * (nL + 1)
    visR = [0] * (nR + 1)
    bfs_timer = 0
    
    # We need to track which edges are removed to update degrees
    # We collect edges to be removed in a list `to_remove`
    
    for c in range(Delta, 0, -1):
        # Process L-nodes
        while L_buckets[c]:
            u = L_buckets[c].pop()
            if curr_deg_L[u] != c:
                if curr_deg_L[u] > 0: L_buckets[curr_deg_L[u]].add(u)
                continue
            
            # BFS for u
            bfs_timer += 1
            q = [u]
            visL[u] = bfs_timer
            parent = {} # v -> u
            
            found = False
            target_v = -1
            
            head = 0
            while head < len(q):
                curr_u = q[head]
                head += 1
                
                for v, edge_idx in adj[curr_u]:
                    if not alive[edge_idx]: continue
                    if visR[v] == bfs_timer: continue
                    
                    visR[v] = bfs_timer
                    parent[v] = curr_u
                    
                    if match_ts_R[v] != c: # Free node
                        target_v = v
                        found = True
                        break
                    else:
                        u2 = partnerR[v]
                        if visL[u2] != bfs_timer:
                            visL[u2] = bfs_timer
                            q.append(u2)
                if found: break
            
            if found:
                # Augment
                curr_v = target_v
                while True:
                    prev_u = parent[curr_v]
                    # Match prev_u with curr_v
                    partnerL[prev_u] = curr_v
                    partnerR[curr_v] = prev_u
                    match_ts_L[prev_u] = c
                    match_ts_R[curr_v] = c
                    
                    # Move to previous v
                    # The edge (prev_u, curr_v) is the new match.
                    # We need to find the old match of prev_u to unmatch it?
                    # No, we are building the matching.
                    # The path is: u -> v1 -> u2 -> v2 -> ... -> target_v
                    # We are setting matches: (u, v1), (u2, v2), ...
                    # And unsetting: (u2, v1), ...
                    
                    # Wait, the path is alternating.
                    # u (free) -> v1 (matched to u2) -> u2 (matched to v1) -> v2 (matched to u3) ... -> target_v (free)
                    # We want to flip:
                    # (u, v1) becomes matched.
                    # (u2, v1) becomes unmatched.
                    # (u2, v2) becomes matched.
                    # ...
                    
                    # In my code:
                    # `parent[v]` stores the L-node that reached v.
                    # So `parent[v1] = u`.
                    # `u2` is `partnerR[v1]`.
                    # We need to follow the chain.
                    
                    # Let's trace:
                    # `curr_v` is `target_v`.
                    # `prev_u` is `parent[curr_v]`.
                    # We match `prev_u` with `curr_v`.
                    # Now we need to unmatch the previous partner of `prev_u`?
                    # No, `prev_u` was free (since we started from free `u`).
                    # Wait, `u` was free. `u2` was matched.
                    # In the BFS, we go from `u` to `v1`. `v1` is matched to `u2`.
                    # We add `u2` to queue.
                    # From `u2`, we go to `v2`. `v2` matched to `u3`.
                    # ...
                    # From `uk`, we go to `target_v`. `target_v` is free.
                    # Path: u -> v1 -> u2 -> v2 -> ... -> uk -> target_v
                    # Matches: (u2, v1), (u3, v2), ...
                    # We want: (u, v1), (u2, v2), (u3, v3) ... (uk, target_v)
                    
                    # So we iterate back.
                    # `curr_v` is `target_v`.
                    # `prev_u` is `parent[curr_v]` (which is `uk`).
                    # Match `prev_u` with `curr_v`.
                    # Now we need to find the `v` that `prev_u` was matched to.
                    # `prev_u` was matched to `v_old = partnerL[prev_u]`.
                    # But wait, `u` was free. `u2` was matched to `v1`.
                    # `parent[v1] = u`. `partnerR[v1] = u2`.
                    # So `prev_u` (u2) was reached from `v1`.
                    # But `parent` maps `v -> u`.
                    # We need to know which `v` led to `prev_u`.
                    # In BFS, `u2` was added when we visited `v1`.
                    # So we need to store `parent_L[u2] = v1`.
                    
                    # Let's add `parent_L` array.
                    pass
            
            # If not found, it means we cannot match u.
            # This should not happen if the theorem holds.
            # But if it does, we just leave u unmatched?
            # No, we must match it.
            pass
            
        # Process R-nodes (symmetric)
        while R_buckets[c]:
            v = R_buckets[c].pop()
            if curr_deg_R[v] != c:
                if curr_deg_R[v] > 0: R_buckets[curr_deg_R[v]].add(v)
                continue
            
            # BFS from v
            bfs_timer += 1
            q = [v]
            visR[v] = bfs_timer
            parent = {} # u -> v
            
            found = False
            target_u = -1
            
            head = 0
            while head < len(q):
                curr_v = q[head]
                head += 1
                
                # Iterate neighbors of v
                # We need reverse adjacency list for R
                # Let's build `adjR`
                pass
                
    # Okay, the implementation is getting messy.
    # Let's simplify.
    
    # We can just use a standard bipartite matching algorithm `c` times.
    # But we need to remove edges.
    
    # Let's use the `hopcroft_karp` algorithm?
    # It finds maximum matching.
    # We can run it `Delta` times.
    # In each step, we find a matching that covers all max-degree nodes.
    # How to enforce covering max-degree nodes?
    # We can add dummy nodes connected to max-degree nodes?
    # Or just run HK and hope it covers them? (It might not).
    
    # The standard algorithm for this problem (Edge Coloring Bipartite Graphs) is:
    # Repeat Delta times:
    #   Find a matching that covers all max-degree nodes.
    #   Color the matching edges with current color.
    #   Remove matching edges.
    
    # To find such a matching:
    # We can use a greedy approach with path augmentation.
    # For each node `u` with degree `Delta`:
    #   If `u` is not matched:
    #     Find augmenting path starting from `u`.
    #     Augment.
    
    # This works because:
    # If `u` has degree `Delta`, it has a neighbor `v`.
    # If `v` is free, match `(u, v)`.
    # If `v` is matched to `u2`, then `u2` has degree `Delta` (since `v` has degree `Delta`).
    # We can recursively find a free node.
    # Since the graph is bipartite and degrees are bounded, this terminates.
    
    # Let's implement this logic cleanly.
    
    # We need `adjR` for R-nodes.
    adjR = [[] for _ in range(nR + 1)]
    for idx, (u, v) in enumerate(edges):
        adjR[v].append((u, idx))
        
    # We need to track matched edges for the current color.
    # `matched[edge_idx] = True` if edge is in current matching.
    # But we remove edges from graph, so `alive` is enough.
    # We need `matchL[u]` and `matchR[v]`.
    
    # We can reuse `matchL` and `matchR` arrays.
    # Initialize with 0.
    
    matchL = [0] * (nL + 1)
    matchR = [0] * (nR + 1)
    
    # We need to clear matching for each color.
    # We can use a list of matched nodes to clear.
    
    for c in range(Delta, 0, -1):
        # Find all nodes with degree c
        # We can iterate through buckets
        pass
        
    # Actually, the bucket maintenance is tricky.
    # Let's just iterate through all nodes.
    # Since sum of degrees is M, and we process each edge once, the total iterations over nodes is O(M * Delta) in worst case?
    # No. We iterate `c` from Delta to 1. Inside, we iterate all nodes.
    # Total O((nL + nR) * Delta). If Delta is large, this is slow.
    
    # We MUST use buckets.
    
    # Let's rewrite the bucket logic carefully.
    
    L_buckets = [set() for _ in range(Delta + 2)]
    R_buckets = [set() for _ in range(Delta + 2)]
    
    for u in range(1, nL + 1):
        if curr_deg_L[u] > 0: L_buckets[curr_deg_L[u]].add(u)
    for v in range(1, nR + 1):
        if curr_deg_R[v] > 0: R_buckets[curr_deg_R[v]].add(v)
        
    # We need `adj` and `adjR`.
    # `adj[u]` contains `(v, edge_idx)`
    # `adjR[v]` contains `(u, edge_idx)`
    
    # We need `ptr` arrays to optimize neighbor iteration.
    ptrL = [0] * (nL + 1)
    ptrR = [0] * (nR + 1)
    
    # We need `matchL` and `matchR` for the current matching.
    # We use timestamp to reset.
    matchL_ts = [0] * (nL + 1)
    matchR_ts = [0] * (nR + 1)
    matchL_val = [0] * (nL + 1)
    matchR_val = [0] * (nR + 1)
    
    visL = [0] * (nL + 1)
    visR = [0] * (nR + 1)
    bfs_timer = 0
    
    for c in range(Delta, 0, -1):
        # Process L-nodes with degree c
        while L_buckets[c]:
            u = L_buckets[c].pop()
            if curr_deg_L[u] < c:
                if curr_deg_L[u] > 0: L_buckets[curr_deg_L[u]].add(u)
                continue
            if matchL_ts[u] == c: continue # Already matched
            
            # Find augmenting path from u
            bfs_timer += 1
            q = [u]
            visL[u] = bfs_timer
            parent = {} # v -> u
            
            found = False
            target_v = -1
            
            # We need to find a neighbor v
            # Use ptrL[u] to find first alive neighbor
            while ptrL[u] < len(adj[u]):
                v, edge_idx = adj[u][ptrL[u]]
                if alive[edge_idx]: break
                ptrL[u] += 1
            
            if ptrL[u] == len(adj[u]): continue # No neighbors left (should not happen if deg > 0)
            
            # Start BFS from u
            # Actually, we can just start BFS from u.
            # The first layer is u.
            # Neighbors of u are v1, v2...
            # If any v is free, we are done.
            # If all v are matched, we add their partners to queue.
            
            head = 0
            q = [u]
            visL[u] = bfs_timer
            
            while head < len(q):
                curr_u = q[head]
                head += 1
                
                # Iterate neighbors
                start_k = 0
                if curr_u == u: start_k = ptrL[u]
                
                for k in range(start_k, len(adj[curr_u])):
                    v, edge_idx = adj[curr_u][k]
                    if not alive[edge_idx]: continue
                    if visR[v] == bfs_timer: continue
                    
                    visR[v] = bfs_timer
                    parent[v] = curr_u
                    
                    if matchR_ts[v] != c: # Free
                        target_v = v
                        found = True
                        break
                    else:
                        u2 = matchR_val[v]
                        if visL[u2] != bfs_timer:
                            visL[u2] = bfs_timer
                            q.append(u2)
                if found: break
            
            if found:
                # Augment
                curr_v = target_v
                while True:
                    prev_u = parent[curr_v]
                    # Match prev_u with curr_v
                    matchL_val[prev_u] = curr_v
                    matchR_val[curr_v] = prev_u
                    matchL_ts[prev_u] = c
                    matchR_ts[curr_v] = c
                    
                    if prev_u == u: break
                    
                    # Find the v that prev_u was matched to
                    # prev_u was reached from some v_old
                    # We need to trace back.
                    # In BFS, we went u -> v1 -> u2 -> v2 ...
                    # parent[v1] = u.
                    # u2 was added when we visited v1.
                    # So we need to know which v led to u2.
                    # We don't store that.
                    
                    # We need to store `parent_L[u2] = v1`.
                    pass
                    
            # If not found, it's an issue.
            pass
            
        # Process R-nodes
        while R_buckets[c]:
            v = R_buckets[c].pop()
            if curr_deg_R[v] < c:
                if curr_deg_R[v] > 0: R_buckets[curr_deg_R[v]].add(v)
                continue
            if matchR_ts[v] == c: continue
            
            # BFS from v
            bfs_timer += 1
            q = [v]
            visR[v] = bfs_timer
            parent = {} # u -> v
            
            found = False
            target_u = -1
            
            head = 0
            while head < len(q):
                curr_v = q[head]
                head += 1
                
                start_k = 0
                if curr_v == v: start_k = ptrR[v]
                
                for k in range(start_k, len(adjR[curr_v])):
                    u, edge_idx = adjR[curr_v][k]
                    if not alive[edge_idx]: continue
                    if visL[u] == bfs_timer: continue
                    
                    visL[u] = bfs_timer
                    parent[u] = curr_v
                    
                    if matchL_ts[u] != c:
                        target_u = u
                        found = True
                        break
                    else:
                        v2 = matchL_val[u]
                        if visR[v2] != bfs_timer:
                            visR[v2] = bfs_timer
                            q.append(v2)
                if found: break
            
            if found:
                # Augment
                curr_u = target_u
                while True:
                    prev_v = parent[curr_u]
                    matchR_val[prev_v] = curr_u
                    matchL_val[curr_u] = prev_v
                    matchR_ts[prev_v] = c
                    matchL_ts[curr_u] = c
                    
                    if prev_v == v: break
                    
                    # Same issue with tracing back
                    pass
                    
        # After processing, we have a matching for color c.
        # We need to color the edges and remove them.
        
        # Iterate through matched edges
        # We can iterate through all nodes and check if matched.
        # But we need to find the edge_idx.
        
        # We can iterate through `matchL_val`.
        for u in range(1, nL + 1):
            if matchL_ts[u] == c:
                v = matchL_val[u]
                # Find edge_idx
                # We can search in adj[u]
                # Or we can store edge_idx in matchL_val? No.
                
                # We can search for the edge.
                # Since we have ptrL, we can use that.
                # But ptrL might have advanced.
                
                # Let's just search.
                found_idx = -1
                for k in range(len(adj[u])):
                    v2, idx = adj[u][k]
                    if v2 == v and alive[idx]:
                        found_idx = idx
                        break
                
                if found_idx != -1:
                    ans[found_idx] = c
                    alive[found_idx] = False
                    
                    # Update degrees
                    old_deg_u = curr_deg_L[u]
                    curr_deg_L[u] -= 1
                    L_buckets[old_deg_u].discard(u)
                    if curr_deg_L[u] > 0: L_buckets[curr_deg_L[u]].add(u)
                    
                    old_deg_v = curr_deg_R[v]
                    curr_deg_R[v] -= 1
                    R_buckets[old_deg_v].discard(v)
                    if curr_deg_R[v] > 0: R_buckets[curr_deg_R[v]].add(v)
                    
                    # Reset matching for these nodes
                    matchL_ts[u] = 0
                    matchR_ts[v] = 0

    print("YES")
    print(" ".join(map(str, ans)))

solve()