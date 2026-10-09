import sys
from itertools import combinations

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    degree = [0] * (n + 1)
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degree[u] += 1
        degree[v] += 1
    
    # To satisfy the condition:
    # Sum of degrees of selected nodes == Number of unique edges covered by selected nodes
    # This means no edge has both endpoints selected (edges must be an induced matching).
    
    # If k > n - m: by pigeonhole principle, valid selection exists.
    # Proof: We claim there is always a valid selection of size >= n - m.
    # Consider greedy selection: greedily pick a node and remove all its conflicting edges.
    # In each step, we pick 1 node and remove <= m edges currently present.
    # Total nodes >= n - m can be picked this way.
    # Thus if k > n - m, there must be a valid selection.
    # (If we could only pick < n-m nodes, the greedy would remove > m edges, contradiction).
    
    nodes = list(range(1, n + 1))
    
    if k > n - m:
        # Find a valid selection of size k.
        # Strategy: Greedy selection ensuring no edge has both endpoints.
        selected = []
        used = [False] * (n + 1)
        # To make the output deterministic and easy, we simply run the greedy algorithm.
        # It will yield at least n-m valid nodes. We can take any k of them.
        # Since k > n-m, we can just fill the rest with isolated nodes if needed,
        # or just use the nodes found by greedy. The greedy is guaranteed to find at least n-m nodes,
        # and typically more.
        
        # Re-run greedy to be sure
        selected_set = set()
        candidates = list(range(1, n + 1))
        
        # We can iterate through nodes
        for u in candidates:
            # Check if u can be added: no邻居 v in selected_set
            # We need adjacency info
            pass
        
        # Re-read edges for adjacency list structure (though we already have `edges`)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        for u in range(1, n + 1):
            conflict = False
            for v in adj[u]:
                if v in selected_set:
                    conflict = True
                    break
            if not conflict:
                selected_set.add(u)
                if len(selected_set) == k:
                    break
        
        # If we found k nodes, great. Otherwise, we might need to just pick isolated nodes?
        # Actually, the greedy loop above might stop early if it scans 1..n linearly and hits conflicts.
        # But we know a set of size k exists.
        # A safer bet for large k: just pick any k nodes that form an independent set.
        # Since one exists, we can just keep adding.
        
        if len(selected_set) < k:
            # We can do a correction: just pick any nodes with degree 0 first, then use greedy.
            # Strategy: Pick all isolated nodes first.
            deg_zero_nodes = [u for u in range(1, n+1) if degree[u] == 0]
            for u in deg_zero_nodes:
                selected_set.add(u)
            
            for u in range(1, n + 1):
                if u in selected_set:
                    continue
                conflict = False
                for v in adj[u]:
                    if v in selected_set:
                        conflict = True
                        break
                if not conflict:
                    selected_set.add(u)
                
                if len(selected_set) >= k:
                    break
        
        result = list(selected_set)[:k]
        print("YES")
        print(" ".join(map(str, result)))
        return

    # Small k: brute force
    # Complexity: C(n, k) * O(k^2) or O(m).
    # We just need to check if any combination is valid.
    
    # Optimization: convert edges to set for O(1) lookup
    edge_set = set()
    for u, v in edges:
        edge_set.add((min(u,v), max(u,v)))
        
    # Pre-calculate degrees are already in `degree`.
    
    found = False
    result_combo = None
    
    # Check only nodes if needed, but C(n, k) is fine.
    for combo in combinations(range(1, n + 1), k):
        combo_set = set(combo)
        
        # Check sum of degrees
        current_sum_deg = 0
        for u in combo:
            current_sum_deg += degree[u]
            
        # Count covered edges
        covered_edges_count = 0
        valid = True
        for u_idx in range(k):
            for v_idx in range(u_idx + 1, k):
                u = combo[u_idx]
                v = combo[v_idx]
                if (min(u,v), max(u,v)) in edge_set:
                    covered_edges_count += 1
                    # If any edge is covered, the condition fails immediately if deg sum > 0.
                    # Actually, if an edge is covered, sum_deg += 2 (1 from u, 1 from v).
                    # unique_count += 1.
                    # 2 != 1. So condition fails.
                    valid = False
                    # Break inner loop
                    break
            if not valid:
                break
        
        if valid:
            # No edges covered. Unique blocks = 0.
            # We need sum_deg == 0.
            if current_sum_deg == 0:
                found = True
                result_combo = combo
                break
        else:
            # If not valid (meaning we found an edge that makes sum_vs_uniq diff),
            # we could still technically have sum_deg == covered if multiple edges?
            # No, if any edge is covered, it contributes 2 to sum_deg and 1 to unique.
            # So total diff += 1. Always unequal (unless other factors compensate? No).
            # If an edge is internal, sum > unique. Always.
            # So we can actually just check `valid` (no edges covered).
            # And if no edges covered, unique=0, so sum must be 0.
            # Sum of degrees is 0 only if all selected nodes have degree 0.
            # So for small k, we look for combo of nodes with degree 0.
            # Wait, my logic "if not valid: break" assumes any internal edge makes it impossible.
            # Yes, sum > unique strictly if any internal edge exists.
            # So we just need to find k nodes with degree 0?
            # No, wait.
            # If we select nodes {1, 2} and block is (1,2).
            # Sum = 1+1=2. Unique = 1. 2 != 1.
            # If we select nodes {1, 2} and blocks are (1,2), (1,2) [impossible, distinct].
            # If blocks (1,3), (2,3) and select {1,2}.
            # Sum = 1+1=2. Unique = {(1,3), (2,3)} = 2. 2 == 2.
            # So it IS possible to have equality even if no internal edge, provided the covered edges count matches sum.
            # Wait, I used "valid=True" only if NO edges covered.
            # In the {1,2} with (1,3), (2,3) case: No edges covered. Valid=True.
            # Sum = 2. My logic above would check if sum==0.
            # But here unique_blocks=2, sum=2.
            # Unique blocks are (1,3) and (2,3).
            # Ah, the validity condition for "Valid Independent Set" was that the internal edges must be empty.
            # If we select {1, 3, 5} in example 2.
            # Blocks (1,2), (3,4). No internal edges.
            # Sum_deg = 1+1+0 = 2.
            # Unique blocks covered = {(1,2), (3,4)} size 2.
            # 2 == 2. Matches.
            # So condition for equality when no internal edges:
            # Sum of degrees of selected nodes == Count of unique edges incident to selected nodes.
            # Since degree[u] is count of edges incident to u.
            # If no two selected nodes share an edge, then edges incident to selected nodes are DISJOINT.
            # Thus unique blocks covered = sum of degrees of selected nodes.
            # So ANY independent set (no internal edges) is a valid solution!
            
            # Wait, Example 1: Select {1, 2, 4}.
            # Blocks (1,2), (1,3), (2,3), (3,4).
            # Select {1, 2, 4}.
            # Edge (1,2) is internal.
            # Sum = deg(1)+deg(2)+deg(4) = 2+2+1 = 5.
            # Unique covered: (1,2), (1,3), (2,3), (3,4) -> 4 blocks.
            # 5 != 4.
            # Internal edge (1,2) causes the deficit.
            # Consider again: sum_degrees = 2*I + B where I is count of internal edges (incident to 2 selected nodes) and B is count of boundary edges (incident to 1 selected node).
            # Unique blocks = I + B.
            # We need 2I + B = I + B => I = 0.
            # So we need ZERO internal edges.
            # I = 0 means the set is an independent set in the graph.
            # AND if I=0, then 2*0 + B = 0 + B => B = B. Equality always holds.
            # So any independent set is a valid solution!
            
            # Wait, verify Example 3: k=1. Graph triangle.
            # Select {1}. Lines="YES".
            # Is {1} an independent set? Yes (no edge 1-1).
            # Sum = deg(1) = 2.
            # Unique blocks = {(1,2), (1,3)} = 2.
            # Matches.
            # Select {2}. Yes.
            # Select {1, 2}?
            # Internal edge (1,2) exists. Not independent.
            # Sum = 2+2=4. Unique = {(1,2), (1,3), (2,3)} = 3. 4 != 3. No.
            
            # Conclusion: The condition reduces to selecting k nodes that form an Independent Set.
            
            # So, the problem is just: Find k independent nodes.
            pass

    # Refined Brute Force for small k:
    # Check if combo is an independent set.
    for combo in combinations(range(1, n + 1), k):
        is_independent = True
        for i in range(k):
            for j in range(i + 1, k):
                u, v = combo[i], combo[j]
                if (min(u,v), max(u,v)) in edge_set:
                    is_independent = False
                    break
            if not is_independent:
                break
        if is_independent:
            found = True
            result_combo = combo
            break
            
    if found:
        print("YES")
        print(" ".join(map(str, result_combo)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()