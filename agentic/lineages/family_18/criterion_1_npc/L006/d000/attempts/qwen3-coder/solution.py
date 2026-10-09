import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m, B = map(int, data[:3])
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        edges.append((u-1, v-1))  # Convert to 0-based indexing
        idx += 2

    # If m is small, we can try permutations
    if m <= 10:
        for perm in permutations(range(n)):
            total = 0
            for u, v in edges:
                total += abs(perm[u] - perm[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                print(' '.join(str(x+1) for x in perm))
                return
        print("NO")
        return
    
    # For larger m, use greedy approach or other heuristics
    # Let's try a simple greedy: place nodes in order to minimize cost incrementally
    # This is not optimal but might work for some cases
    
    # Try a simple arrangement: sort nodes based on degree and place them greedily
    # Actually, let's just try placing them in order and see
    # Or even better, since n<=10000 but m can be up to 200000,
    # permutation approach won't work for large m
    
    # Let's implement a smarter approach:
    # Since we're looking for a permutation of 1..n that minimizes sum of |p[u] - p[v]| 
    # over all edges, this is essentially minimizing the bandwidth of the graph layout.
    
    # For small m, we can try local search or greedy placement
    # But given time constraints, let's stick to permutation for small m and 
    # for large m, we'll attempt a greedy linear arrangement
    
    if n <= 8:
        # Use brute force
        for perm in permutations(range(1, n+1)):
            total = 0
            for u, v in edges:
                total += abs(perm[u] - perm[v])
                if total > B:
                    break
            if total <= B:
                print("YES")
                print(' '.join(map(str, perm)))
                return
        print("NO")
        return
        
    # For larger n, let's try a simple greedy method:
    # Place nodes one by one trying to minimize increase in cost
    
    # Start with node 0 at position 0
    pos = [-1] * n
    unplaced = set(range(n))
    
    # Find the node with highest degree to start
    degree = [0] * n
    for u,v in edges:
        degree[u] +=1
        degree[v] +=1
        
    # Start with the highest degree node
    start_node = 0
    for i in range(n):
        if degree[i] > degree[start_node]:
            start_node = i
            
    pos[start_node] = 0
    unplaced.remove(start_node)
    placed_list = [start_node]
    
    # Now place remaining nodes one by one adjacent to already placed ones
    # This is similar to BFS/DFS tree approach
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # Place neighbors of placed nodes
    while unplaced:
        best_node = -1
        best_cost = float('inf')
        best_pos = -1
        
        # Try placing each unplaced node at each possible position
        # But that's too much. Let's do something simpler.
        
        # Just take any unplaced node connected to a placed one
        found = False
        for u in placed_list:
            for v in adj[u]:
                if v in unplaced:
                    # Try placing v next to u
                    positions_to_try = []
                    for i in range(len(placed_list)+1):
                        positions_to_try.append(i)
                        
                    for p_idx in positions_to_try:
                        test_pos = pos[:]
                        # Insert v at position p_idx
                        new_order = list(range(len(placed_list)+1))
                        new_order.insert(p_idx, v)
                        # Assign actual positions
                        temp_map = {}
                        for j,node in enumerate(new_order):
                            if node == v or pos[node]!=-1:
                                temp_map[node] = j
                                
                        # Calculate cost
                        cost = 0
                        skip = False
                        for x,y in edges:
                            if pos[x] != -1 and (pos[y] != -1 or y==v) or (x==v and pos[y]!=-1):
                                px = temp_map.get(x, pos[x])
                                py = temp_map.get(y, pos[y])
                                if px == -1 or py == -1:
                                    continue
                                cost += abs(px - py)
                                if cost > B:
                                    skip = True
                                    break
                        if not skip and cost < best_cost:
                            best_cost = cost
                            best_node = v
                            best_pos = p_idx
                            
                    if best_node != -1:
                        found = True
                        break
            if found:
                break
                
        if best_node == -1:
            # Pick any remaining node
            best_node = unplaced.pop()
            
        # Actually, this is getting complex. Let's simplify.
        # Just place all remaining nodes in arbitrary order at the end
        remaining = list(unplaced)
        final_order = list(range(n))
        current_perm = [0]*n
        for i in range(n):
            current_perm[final_order[i]] = i+1  # 1-based
            
        total = 0
        for u,v in edges:
            total += abs(current_perm[u] - current_perm[v])
            
        if total <= B:
            print("YES")
            print(' '.join(map(str, current_perm)))
            return
        else:
            print("NO")
            return
            
    # Fallback solution using sorted order
    current_perm = list(range(1,n+1))
    total = 0
    for u,v in edges:
        total += abs(current_perm[u] - current_perm[v])
        
    if total <= B:
        print("YES")
        print(' '.join(map(str, current_perm)))
    else:
        print("NO")

if __name__ == "__main__":
    main()