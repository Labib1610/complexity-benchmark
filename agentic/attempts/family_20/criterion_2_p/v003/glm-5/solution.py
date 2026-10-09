import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))
    
    edges = []
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
    
    # Find Delta (busiest port degree)
    max_deg_L = max(deg_L) if nL > 0 else 0
    max_deg_R = max(deg_R) if nR > 0 else 0
    Delta = max(max_deg_L, max_deg_R)
    
    # Build adjacency lists for the bipartite graph
    # adj_L[u] contains list of (v, edge_idx)
    adj_L = [[] for _ in range(nL + 1)]
    adj_R = [[] for _ in range(nR + 1)]
    
    for i, (u, v) in enumerate(edges):
        adj_L[u].append((v, i))
        adj_R[v].append((u, i))
    
    # Initialize color assignment
    color = [0] * m
    
    # Process each L-node to assign colors to its edges
    # We maintain for each L-node a set of used colors (indices 1..Delta)
    # and for each R-node a set of used colors.
    # We use a greedy approach with a stack to resolve conflicts.
    
    # To speed up finding available colors, we track the first available color index.
    # Since we always fill from 1 upwards, the first available is used_count + 1.
    # We can use a simple counter for each node.
    
    # However, for the conflict resolution, we need to iterate.
    # The total complexity is O(M * Delta) in worst case, but with Delta <= max degree,
    # and M <= 400000, this might be too slow if Delta is large.
    # But the problem statement guarantees Delta is the max degree, and the graph is bipartite.
    # The standard edge coloring algorithm for bipartite graphs runs in O(M * sqrt(N)) or O(M * log N) or O(M * Delta).
    # Given the constraints, O(M * Delta) might pass if Delta is small, but Delta can be up to M.
    # Wait, the problem says "The rule that cables only connect L-type to R-type ports guarantees the unavoidable minimum is always achievable".
    # This is a known result: bipartite graphs have edge chromatic number equal to max degree.
    # The standard algorithm to find such a coloring involves finding augmenting paths.
    
    # Let's implement a standard algorithm for edge coloring bipartite graphs.
    # We can use the algorithm that colors edges one by one.
    # For each edge (u, v), we find the smallest color c not used by u and not used by v.
    # If c is available, we assign it.
    # If not (i.e., c is used by u and v), we find the smallest available color for u (c1) and for v (c2).
    # Since it's bipartite, we can find an alternating path from u using colors c and c2.
    # We swap colors along this path, which frees up color c for the current edge.
    
    # This algorithm is O(M * Delta).
    # With M=400000 and Delta potentially large, this might be tight.
    # But Python is slow. We need an efficient implementation.
    
    # Let's try to optimize.
    # We can use arrays to store the color of the edge incident to a node for a specific color index.
    # used_color_L[u][c] = edge_index of the edge incident to u with color c
    # Since nL, nR can be 100000 and Delta can be large, we cannot preallocate 2D arrays.
    # We can use dictionaries or lists of lists.
    # But for the algorithm, we need to quickly check if a color is used and find the edge.
    
    # Let's use lists of dictionaries or just lists if we can.
    # Since Delta is the max degree, the number of colors used by any node is at most Delta.
    # We can use a list of size Delta+1 for each node, but that's too much memory.
    # We can use a dictionary for each node, mapping color -> edge_index.
    
    # Let's try to implement the augmenting path algorithm.
    
    # Data structures:
    # For each L-node u: map color -> edge_index
    # For each R-node v: map color -> edge_index
    # We can use lists of size Delta+1, but initialized empty.
    # Actually, since we assign colors incrementally, we can use arrays.
    
    # Let's use `color_to_edge_L[u][c]` and `color_to_edge_R[v][c]`.
    # To avoid large memory, we can use `defaultdict` or `dict`.
    # But for speed, we can use a single large array if we are careful.
    # Or we can use the fact that we only need to store the edges for the colors that are used.
    
    # Let's use lists of lists. `color_to_edge_L[u]` is a list of length Delta+1, initialized to -1.
    # This would take O((nL + nR) * Delta) memory, which is too much.
    
    # Alternative: Since we process edges one by one, and we only need to find alternating paths,
    # we can use a more efficient representation.
    
    # Let's stick to the greedy approach with conflict resolution.
    # We'll use dictionaries for each node to store used colors.
    
    # Optimization: Since we are looking for the smallest available color,
    # and we are resolving conflicts, we can use a boolean array for the current search.
    
    # Let's implement the algorithm:
    
    # For each edge (u, v) with index i:
    #   Find smallest color c not in used_L[u] and not in used_R[v].
    #   If found, assign c to edge i.
    #   Else:
    #     Let c be the smallest color not in used_L[u] (or used_R[v], they must agree on the smallest missing).
    #     Actually, let c be the smallest color not used by u.
    #     Let d be the smallest color not used by v.
    #     We have c != d. (If c == d, it would be available).
    #     We need to find an alternating path starting from u using colors c and d.
    #     The path alternates between L and R nodes.
    #     From L-node, we follow color d.
    #     From R-node, we follow color c.
    #     We stop when we reach a node that does not have the expected color edge.
    #     Then we swap colors along the path.
    #     This will free up color c for the current edge.
    
    # This algorithm is correct and runs in O(M * Delta).
    # With M=400000, if Delta is small, it's fast.
    # If Delta is large, it might TLE.
    # However, for bipartite graphs, this is a standard approach.
    
    # Let's optimize the implementation.
    # We can use arrays for `used_L` and `used_R` but only for the colors that are used.
    # We can use a list of edge indices for each node, indexed by color.
    # To handle the "smallest unused color" query efficiently, we can maintain a pointer or use a bitset.
    # But since we are resolving conflicts, we might need to search.
    
    # Let's use a simple list for each node to store the edge index for each color.
    # We can use a dictionary for sparse storage.
    
    # To speed up "smallest unused color", we can maintain for each node the first available color.
    # But after swapping, the available colors might change.
    # However, the smallest unused color for a node can only increase or stay the same as we add edges.
    # Wait, during swapping, we are not adding new edges, just changing colors.
    # So the set of used colors for a node changes, but the count stays the same.
    # The smallest unused color can decrease if we swap a small color out.
    # So we cannot just maintain a pointer.
    
    # We can iterate from 1 to Delta to find the smallest unused color.
    # This is O(Delta) per query.
    # Total complexity: O(M * Delta).
    
    # Let's try to implement this efficiently in Python.
    
    # We'll use lists of dictionaries.
    # `L_color_edge[u]` maps color -> edge_index
    # `R_color_edge[v]` maps color -> edge_index
    
    L_color_edge = [dict() for _ in range(nL + 1)]
    R_color_edge = [dict() for _ in range(nR + 1)]
    
    # We also need to know the other end of an edge given its index.
    # We have `edges` list.
    
    for i in range(m):
        u, v = edges[i]
        
        # Find smallest unused color for u and v
        # We can iterate from 1 upwards
        # To optimize, we can track the number of used colors, but we need the specific missing color.
        
        # Let's find c1 (smallest unused for u) and c2 (smallest unused for v)
        c = 1
        while True:
            if c not in L_color_edge[u] and c not in R_color_edge[v]:
                break
            c += 1
        
        if c not in L_color_edge[u] and c not in R_color_edge[v]:
            # Assign color c
            color[i] = c
            L_color_edge[u][c] = i
            R_color_edge[v][c] = i
        else:
            # This case should not happen with the logic above
            # The loop breaks only when we find an available color
            pass
            
    # Wait, the logic above is not the augmenting path algorithm.
    # The simple greedy approach "find smallest unused color" works for vertex coloring, but for edge coloring we have conflicts.
    # The condition `c not in L_color_edge[u] and c not in R_color_edge[v]` is exactly what we need.
    # If such a c exists, we assign it.
    # If no such c exists, it means all colors 1..Delta are used by either u or v.
    # Since degree of u <= Delta and degree of v <= Delta, and we are processing one edge,
    # it means u uses some colors and v uses some colors, and their union is all colors 1..Delta.
    # In this case, we need the augmenting path.
    
    # Let's refine the loop.
    
    for i in range(m):
        u, v = edges[i]
        
        # Find smallest unused color for u and v
        c = 1
        while c in L_color_edge[u] and c in R_color_edge[v]:
            c += 1
        
        # Now c is either not used by u or not used by v (or both)
        
        if c not in L_color_edge[u] and c not in R_color_edge[v]:
            # Available for both, assign it
            color[i] = c
            L_color_edge[u][c] = i
            R_color_edge[v][c] = i
        elif c not in L_color_edge[u]:
            # c is used by v but not u
            # We need to find a color for the edge (u, v).
            # Let's find another color d that is used by u but not v.
            # Actually, we need to find an augmenting path.
            # Let's find the smallest color d not used by v.
            # Since c is used by v, d could be c or something else.
            # Wait, the standard algorithm is:
            # Let c be the smallest color not used by u.
            # Let d be the smallest color not used by v.
            # If c == d, we are good.
            # If c != d, we find an alternating path from u using colors c and d.
            
            # Let's re-find c and d properly.
            pass # This logic is getting complicated. Let's restart with the standard algorithm structure.

    # Restarting the coloring logic with the standard augmenting path approach.
    
    color = [0] * m
    L_color_edge = [dict() for _ in range(nL + 1)]
    R_color_edge = [dict() for _ in range(nR + 1)]
    
    for i in range(m):
        u, v = edges[i]
        
        # Find smallest color not used by u
        c = 1
        while c in L_color_edge[u]:
            c += 1
            
        # Find smallest color not used by v
        d = 1
        while d in R_color_edge[v]:
            d += 1
            
        if c == d:
            # Color c is available for both
            color[i] = c
            L_color_edge[u][c] = i
            R_color_edge[v][c] = i
        else:
            # c != d
            # c is not used by u, d is not used by v.
            # We need to find an alternating path starting from u using colors c and d.
            # The path starts at u (L-node).
            # From L-node, we follow color d.
            # From R-node, we follow color c.
            
            # We need to find a path: u --(d)--> r1 --(c)--> l1 --(d)--> ...
            # Until we reach a node that does not have the expected color edge.
            
            path = []
            curr_u = u
            curr_color_c = c
            curr_color_d = d
            
            # We are at L-node curr_u. We look for edge with color d.
            while True:
                if curr_color_d in L_color_edge[curr_u]:
                    edge_idx_d = L_color_edge[curr_u][curr_color_d]
                    v_neighbor = edges[edge_idx_d][1] # The R-node neighbor
                    
                    path.append((curr_u, curr_color_d, edge_idx_d, v_neighbor))
                    
                    # Now at R-node v_neighbor. Look for edge with color c.
                    if curr_color_c in R_color_edge[v_neighbor]:
                        edge_idx_c = R_color_edge[v_neighbor][curr_color_c]
                        u_neighbor = edges[edge_idx_c][0] # The L-node neighbor
                        
                        path.append((v_neighbor, curr_color_c, edge_idx_c, u_neighbor))
                        
                        curr_u = u_neighbor
                        # Swap colors for the next step
                        curr_color_c, curr_color_d = curr_color_d, curr_color_c
                    else:
                        # No edge with color c from v_neighbor. Path ends.
                        break
                else:
                    # No edge with color d from curr_u. Path ends.
                    break
            
            # Now we swap colors along the path.
            # The path contains alternating edges.
            # We swap c and d for all edges in the path.
            # This will free up color c for the current edge (u, v).
            
            for j in range(len(path)):
                node, col, edge_idx, neighbor = path[j]
                # We need to swap the colors.
                # But we stored the edge indices.
                # Let's just swap the colors in the data structures.
                
                # The path stores edges. Even indices are L->R edges (color d), odd are R->L edges (color c).
                # Actually, the logic is simpler: just swap c and d for all edges in the path.
                pass
            
            # Let's implement the swap carefully.
            # The path is a sequence of edges.
            # We iterate through the path and swap colors.
            
            for k in range(len(path)):
                # path[k] is (node, color_on_edge, edge_idx, neighbor)
                # We want to change the color of edge_idx.
                # But we need to know the new color.
                # The colors alternate: d, c, d, c, ...
                # So we swap c and d.
                
                # Let's just re-process the path.
                pass
            
            # Simpler approach for swapping:
            # We have a sequence of edges: e1, e2, e3, ...
            # e1 has color d, e2 has color c, e3 has color d, ...
            # We change e1 to c, e2 to d, e3 to c, ...
            # This frees up d for the first edge? No.
            # We want to free up c for the current edge (u, v).
            # The path starts with edge e1 from u with color d.
            # If we change e1 to c, then u has two edges with color c (the current edge and e1).
            # Wait, the current edge is not yet colored.
            # So we want to color the current edge with c.
            # So we need to free c from u.
            # The path starts from u with color d.
            # If we swap c and d along the path:
            # e1 (from u) changes from d to c. Now u has c used.
            # This doesn't help.
            
            # Let's re-read the algorithm.
            # We want to color edge (u, v).
            # c is smallest unused by u.
            # d is smallest unused by v.
            # If c != d, we find an alternating path from u using colors c and d.
            # The path starts with an edge of color d from u.
            # We swap colors along the path.
            # After swapping, c becomes available for u.
            # Then we color (u, v) with c.
            
            # Let's trace:
            # u has no edge with color c.
            # v has no edge with color d.
            # Path starts at u. We look for edge with color d.
            # If found, let it be (u, v1) with color d.
            # Now at v1. We look for edge with color c.
            # If found, let it be (u1, v1) with color c.
            # Now at u1. We look for edge with color d.
            # ...
            # We stop when we can't find the next edge.
            # Case 1: We stop at an R-node v_k where there is no edge with color c.
            #         We swap colors along the path.
            #         (u, v1) changes d -> c.
            #         (u1, v1) changes c -> d.
            #         (u1, v2) changes d -> c.
            #         ...
            #         (u_k, v_k) changes d -> c? No.
            #         Let's check u. Before swap, u had no edge with color c.
            #         After swap, (u, v1) has color c. So u now has c.
            #         But we wanted to free c for (u, v).
            #         This seems wrong.
            
            # Let's re-check the algorithm source or logic.
            # Ah, the path starts from u with color d.
            # We want to free color c for u.
            # If we swap, the first edge (u, v1) changes d -> c.
            # This makes u use color c.
            # But we wanted to color (u, v) with c.
            # So now u has two edges needing color c: (u, v) and (u, v1).
            # This is a conflict.
            
            # Correct logic:
            # We want to color (u, v).
            # c is smallest unused by u.
            # d is smallest unused by v.
            # If c < d (or c != d), we find path from u using colors d and c.
            # Wait, if c is unused by u, we can color (u, v) with c IF v does not use c.
            # If v uses c, then we have a conflict.
            # The path should start from v with color c.
            # Let's trace:
            # We want to color (u, v) with c.
            # v already has an edge (u1, v) with color c.
            # We look at u1. Does u1 have an edge with color d?
            # If yes, let it be (u1, v1).
            # We look at v1. Does v1 have an edge with color c?
            # ...
            # We stop when we find a node that does not have the expected color.
            # Case 1: We stop at an L-node u_k that has no edge with color d.
            #         We can shift colors.
            #         (u1, v) changes c -> d.
            #         (u1, v1) changes d -> c.
            #         ...
            #         (u_k, v_k) changes d -> c? No.
            #         Let's trace carefully.
            #         We want to color (u, v) with c.
            #         v has edge e1=(u1, v) with color c.
            #         We change e1 to color d.
            #         Now v is happy (no conflict with new edge).
            #         But u1 now has edge e1 with color d.
            #         If u1 already had an edge e2=(u1, v1) with color d, we have a conflict at u1.
            #         So we change e2 to color c.
            #         Now v1 has edge e2 with color c.
            #         If v1 had edge e3=(u2, v1) with color c, conflict at v1.
            #         Change e3 to d.
            #         ...
            #         We stop when we reach a node that does not have the conflict color.
            #         If we stop at u_k because it has no edge with color d, we are good.
            #         The last change was some edge to color d.
            #         u_k has no edge with color d, so no conflict.
            #         And we successfully colored (u, v) with c.
            
            # This is the correct augmenting path logic.
            # We start from v (since v is the one blocking color c).
            # We alternate between L and R nodes.
            # From R-node, we follow color c.
            # From L-node, we follow color d.
            # We swap c and d along the path.
            
            # Let's implement this.
            
            # Current edge (u, v) wants color c.
            # c is unused by u.
            # d is unused by v.
            # If c == d, we just assign.
            # If c != d, it means v uses c (since d is smallest unused for v, and c < d or c > d).
            # Actually, if c < d, then v must use c (otherwise d would be <= c).
            # If c > d, then u must use d.
            # We can always find a path.
            
            # Let's assume c < d (so v uses c).
            # We find path starting from v.
            
            # Path finding:
            # curr_node = v
            # path_edges = []
            # while True:
            #    if at R-node:
            #        if c in R_color_edge[curr_node]:
            #            edge_idx = R_color_edge[curr_node][c]
            #            path_edges.append(edge_idx)
            #            curr_node = edges[edge_idx][0] # move to L
            #        else:
            #            break
            #    else: # at L-node
            #        if d in L_color_edge[curr_node]:
            #            edge_idx = L_color_edge[curr_node][d]
            #            path_edges.append(edge_idx)
            #            curr_node = edges[edge_idx][1] # move to R
            #        else:
            #            break
            
            # After finding path, swap colors.
            # For all edges in path_edges, swap c and d.
            # Then assign c to current edge.
            
            # Wait, if c > d, then u uses d.
            # We want to color (u, v) with d? No, we want smallest colors.
            # The algorithm says: find smallest unused c for u, smallest unused d for v.
            # If c != d, we augment.
            # It doesn't matter which is smaller. The path will resolve it.
            # But we need to start from the correct node.
            # If c < d, v uses c. We start from v.
            # If c > d, u uses d. We start from u? No.
            # Let's stick to: we want to assign color c to (u, v).
            # So we check if v uses c.
            # If v uses c, we start augmenting path from v.
            # If v does not use c, then c is available for v.
            # Since c is unused by u, we can just assign c.
            # So the condition `c != d` implies v uses c (if c < d) or u uses d (if c > d).
            # If c < d, v uses c. We augment from v.
            # If c > d, u uses d. We want to assign c. v does not use c (since d < c and d is smallest unused).
            # So c is available for v. But u uses d.
            # We want to assign c. u does not use c. v does not use c.
            # So we can just assign c!
            # Wait, if c > d, then d is smallest unused for v. c > d.
            # u uses d (since c is smallest unused for u, and d < c).
            # So u uses d.
            # We want to assign c.
            # u does not use c. v does not use c.
            # So we can just assign c.
            # So the only conflict is when c < d.
            # In that case, v uses c. We need to augment.
            
            # Correct logic:
            # Find c (smallest unused for u).
            # If c is unused by v, assign c.
            # Else (v uses c):
            #    Find d (smallest unused for v).
            #    Find augmenting path from v using colors c and d.
            #    Swap colors.
            #    Assign c to (u, v).
            
            # Let's refine the path finding.
            # We are at v. We look for edge with color c.
            # Let it be (u1, v). We change it to d.
            # Now u1 has edge with color d.
            # If u1 already had edge with color d, we have conflict.
            # So we look for edge (u1, v1) with color d.
            # Change it to c.
            # Now v1 has edge with color c.
            # If v1 already had edge with color c, conflict.
            # Look for (u2, v1) with color c.
            # ...
            # Stop when we find a node that does not have the conflict color.
            
            # Implementation details:
            # We need to update L_color_edge and R_color_edge during the swap.
            
            if c in R_color_edge[v]: # Conflict, need to augment
                # Find d
                d = 1
                while d in R_color_edge[v]:
                    d += 1
                
                # Find path starting from v
                # We alternate: R-node -> L-node -> R-node ...
                # From R-node, we follow color c.
                # From L-node, we follow color d.
                
                path_edges = []
                curr_node = v
                is_r_node = True
                
                while True:
                    if is_r_node:
                        if c in R_color_edge[curr_node]:
                            edge_idx = R_color_edge[curr_node][c]
                            path_edges.append(edge_idx)
                            curr_node = edges[edge_idx][0] # move to L
                        else:
                            break
                    else:
                        if d in L_color_edge[curr_node]:
                            edge_idx = L_color_edge[curr_node][d]
                            path_edges.append(edge_idx)
                            curr_node = edges[edge_idx][1] # move to R
                        else:
                            break
                    is_r_node = not is_r_node
                
                # Swap colors along the path
                for edge_idx in path_edges:
                    eu, ev = edges[edge_idx]
                    old_color = color[edge_idx]
                    
                    # Determine new color
                    # If it was c, it becomes d. If it was d, it becomes c.
                    # We need to know which color it was.
                    # The path alternates: c, d, c, d ...
                    # Actually, we can just check.
                    new_color = d if old_color == c else c
                    
                    # Update data structures
                    # Remove old color mapping
                    del L_color_edge[eu][old_color]
                    del R_color_edge[ev][old_color]
                    
                    # Add new color mapping
                    L_color_edge[eu][new_color] = edge_idx
                    R_color_edge[ev][new_color] = edge_idx
                    color[edge_idx] = new_color
                
                # Now color c is free for v
                # Assign c to current edge
                color[i] = c
                L_color_edge[u][c] = i
                R_color_edge[v][c] = i
            else:
                # No conflict, assign c
                color[i] = c
                L_color_edge[u][c] = i
                R_color_edge[v][c] = i

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == '__main__':
    solve()