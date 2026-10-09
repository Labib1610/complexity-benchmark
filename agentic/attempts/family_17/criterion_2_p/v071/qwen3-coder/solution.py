import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    index = 2
    edges = []
    adj_a = defaultdict(list)   # adjacency list for components 1 to q
    adj_b = defaultdict(list)   # adjacency list for components q+1 to 2q
    
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        edges.append((a, b))
        adj_a[a].append(len(edges)-1)
        adj_b[b].append(len(edges)-1)
        index += 2
    
    # For each component in A (1 to q) and B (q+1 to 2q), we need exactly one edge selected
    # This is a bipartite matching problem with degree constraints = 1 for all nodes
    # This is essentially a maximum matching where every node must be matched exactly once
    # This is equivalent to finding a perfect matching in this bipartite graph
    
    # Build a graph for matching: from A to B
    # We'll use a greedy approach with backtracking via augmenting paths (Hungarian / Hopcroft-Karp style)
    # But since every node needs degree exactly 1, it's a perfect matching problem
    
    # Let's try to model this as a matching problem:
    # Each element in A must be matched to exactly one element in B and vice versa
    # So both sides have degree exactly 1 in the solution
    
    # Use a greedy + BFS approach to find such a matching
    
    # For each node in A and B, keep track of their edges
    # Try to find a matching that covers all nodes exactly once
    
    # This is a special case: we want a subgraph where every vertex has degree exactly 1
    # This is a 1-factor or perfect matching in this bipartite graph
    
    # Let's build the matching using a standard algorithm approach:
    # We can model this as finding a maximum matching and then checking if it's perfect for our constraints
    
    # However, let's think simpler:
    # We just need to select edges such that each node in [1,q] and [q+1, 2q] appears exactly once
    # This is exactly the problem of finding a perfect matching in the bipartite graph formed by edges
    
    # Let's implement a simple augmenting path method
    
    # Map each node in A to its edges, same for B
    match_A = {}  # match_A[a] = edge_index
    match_B = {}  # match_B[b] = edge_index
    match_edge_to_a = {}  # match_edge_to_a[edge_index] = a
    match_edge_to_b = {}  # match_edge_to_b[edge_index] = b
    
    # Try to greedily match
    used_edges = [False] * t
    
    # Simple greedy initial matching
    for i, (a, b) in enumerate(edges):
        if a not in match_A and b not in match_B:
            match_A[a] = i
            match_B[b] = i
            match_edge_to_a[i] = a
            match_edge_to_b[i] = b
            used_edges[i] = True
    
    # Now try to improve with augmenting paths
    # For each unmatched a, try to find an augmenting path
    def find_augmenting_path(start_a):
        # BFS to find augmenting path
        visited_a = set()
        visited_b = set()
        queue = deque()
        parent_edge = {}
        start_edge = -1
        
        # Start with all edges from start_a that are not in matching
        for edge_idx in adj_a[start_a]:
            if not used_edges[edge_idx]:
                b = edges[edge_idx][1]
                if b not in visited_b:
                    visited_b.add(b)
                    parent_edge[edge_idx] = -1  # -1 means it's the first edge
                    if b not in match_B:
                        # Found an augmenting path
                        path = []
                        cur_edge = edge_idx
                        while cur_edge != -1:
                            path.append(cur_edge)
                            cur_edge = parent_edge[cur_edge]
                        path.reverse()
                        return path
                    else:
                        # This b is matched, continue from the matched edge
                        matched_edge = match_B[b]
                        queue.append((matched_edge, edge_idx))  # (edge to go next, parent edge)
        
        while queue:
            current_edge, parent = queue.popleft()
            a_node = edges[current_edge][0]
            
            if a_node in visited_a:
                continue
            visited_a.add(a_node)
            
            # From this matched edge, go to the other endpoint b
            b_node = edges[current_edge][1]
            visited_b.add(b_node)
            
            # Now look at all edges from a_node except the matched one
            for edge_idx in adj_a[a_node]:
                if edge_idx == current_edge or used_edges[edge_idx]:
                    continue
                next_b = edges[edge_idx][1]
                if next_b in visited_b:
                    continue
                visited_b.add(next_b)
                parent_edge[edge_idx] = parent
                
                if next_b not in match_B:
                    # Found an augmenting path
                    path = []
                    cur_edge = edge_idx
                    while cur_edge != -1:
                        path.append(cur_edge)
                        cur_edge = parent_edge[cur_edge] if cur_edge in parent_edge else -1
                    path.reverse()
                    return path
                else:
                    matched_edge = match_B[next_b]
                    queue.append((matched_edge, edge_idx))
                    
        return None
    
    # Try to improve matching
    changed = True
    while changed:
        changed = False
        for a in range(1, q+1):
            if a not in match_A:
                path = find_augmenting_path(a)
                if path:
                    # Augment along this path
                    for i in range(len(path)):
                        edge_idx = path[i]
                        a_node, b_node = edges[edge_idx]
                        if i % 2 == 0:  # Add this edge to matching
                            match_A[a_node] = edge_idx
                            match_B[b_node] = edge_idx
                            match_edge_to_a[edge_idx] = a_node
                            match_edge_to_b[edge_idx] = b_node
                            used_edges[edge_idx] = True
                        else:  # Remove this edge from matching
                            del match_A[a_node]
                            del match_B[b_node]
                            del match_edge_to_a[edge_idx]
                            del match_edge_to_b[edge_idx]
                            used_edges[edge_idx] = False
                    changed = True
                    break
    
    # Check if we have a perfect matching
    if len(match_A) == q:
        print("YES")
        result_edges = []
        for a in range(1, q+1):
            edge_idx = match_A[a]
            a_node, b_node = edges[edge_idx]
            result_edges.append((a_node, b_node))
        
        # Sort for consistent output
        result_edges.sort()
        for a, b in result_edges:
            print(a, b)
    else:
        print("NO")

if __name__ == "__main__":
    main()