import sys
from itertools import permutations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        edges.append((u, v))
    
    # We'll try all permutations if n is small, otherwise we need a smarter approach.
    # Given the constraints (n up to 1000), trying all permutations is infeasible.
    # However, let's first check if even the optimal arrangement is possible.
    
    # The minimal total exposure is when we minimize sum of |pos[u] - pos[v]| for all edges.
    # This is a quadratic assignment problem, but we can try a greedy approach or 
    # use the fact that for small m, we can try to place related nodes close.
    
    # But first, let's check if even the best case is within B.
    # The minimal sum is achieved when the graph is laid out optimally on a line.
    # For a tree, this is solvable in poly time. For general graphs, it's harder.
    # However, we can try a heuristic or, for small n, brute-force.
    
    # Let's assume n <= 8 for brute-force to be feasible.
    if n <= 8:
        # Try all permutations
        ops = list(range(n))
        for perm in permutations(ops):
            total = 0
            for u, v in edges:
                total += abs(perm[u] - perm[v])
            if total <= B:
                print("YES")
                # Convert back to 1-based indexing
                result = [0] * n
                for i in range(n):
                    result[perm[i]] = i + 1
                print(' '.join(map(str, result)))
                return
        print("NO")
        return
    else:
        # For larger n, we need a heuristic.
        # One approach: build a layout that minimizes the total distance.
        # This is essentially the minimum linear arrangement problem.
        # A greedy approach: start with a node of highest degree, place neighbors close.
        
        # Let's try a simple greedy layout.
        # Build adjacency list
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Start with node of maximum degree
        order = []
        placed = [False] * n
        # Find node with max degree
        max_deg = -1
        start_node = 0
        for i in range(n):
            if degree[i] > max_deg:
                max_deg = degree[i]
                start_node = i
        
        order.append(start_node)
        placed[start_node] = True
        
        # Now, iteratively add the node that has the most neighbors in the current order
        while len(order) < n:
            best_node = -1
            best_score = -1
            best_pos = -1
            
            for u in range(n):
                if placed[u]:
                    continue
                # For each unplaced node, find the best position in current order
                # Position can be at beginning, end, or between any two
                score = 0
                positions = []
                for v in adj[u]:
                    if placed[v]:
                        pos_v = order.index(v)
                        positions.append(pos_v)
                
                if not positions:
                    # No neighbors placed yet, place it at the end
                    if 0 > best_score:
                        best_score = 0
                        best_node = u
                        best_pos = len(order)
                    continue
                
                # Try to place u to minimize sum of distances to neighbors
                min_cost = float('inf')
                best_internal_pos = -1
                # Try all positions: 0 to len(order)
                for pos in range(len(order) + 1):
                    cost = 0
                    for p in positions:
                        cost += abs(pos - p)
                    if cost < min_cost:
                        min_cost = cost
                        best_internal_pos = pos
                
                if min_cost > best_score:  # Wait, we want to maximize the score to choose the best node
                    # Actually, we want to choose the node that when placed optimally,
                    # gives the best improvement or has most connections.
                    # Let's redefine: choose node with most placed neighbors, break ties by min cost
                    if len(positions) > best_score or (len(positions) == best_score and min_cost < best_score):
                        best_score = len(positions)
                        best_node = u
                        best_pos = best_internal_pos
            
            if best_node == -1:
                # No node has a placed neighbor, pick any unplaced node
                for u in range(n):
                    if not placed[u]:
                        best_node = u
                        best_pos = len(order)
                        break
            
            # Insert best_node at best_pos
            order.insert(best_pos, best_node)
            placed[best_node] = True
        
        # Now compute total exposure
        pos = [0] * n
        for i in range(n):
            pos[order[i]] = i
        
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
        
        if total <= B:
            # Convert to 1-based result
            result = [0] * n
            for i in range(n):
                result[pos[i]] = i + 1
            print("YES")
            print(' '.join(map(str, result)))
            return
        
        # If greedy didn't work, try a refinement or say NO
        # For this problem, if the greedy fails and n is large, we assume NO
        # But let's try one more thing: sort by degree and place greedily
        order2 = list(range(n))
        order2.sort(key=lambda x: degree[x], reverse=True)
        
        # Assign positions greedily to minimize total distance
        # This is complex; let's just output the order2 as positions
        pos2 = [0] * n
        for i in range(n):
            pos2[order2[i]] = i
            
        total2 = 0
        for u, v in edges:
            total2 += abs(pos2[u] - pos2[v])
            
        if total2 <= B:
            result = [0] * n
            for i in range(n):
                result[pos2[i]] = i + 1
            print("YES")
            print(' '.join(map(str, result)))
            return
        
        print("NO")

if __name__ == "__main__":
    main()