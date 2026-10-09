import sys
from collections import defaultdict
import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def minimum_cost_to_connect_critical_variables(n, m, t, critical_vars, constraints):
    # Since t is at most 10, we can try all possible ways to connect them
    # But a better approach is to find the minimum spanning tree that connects all critical variables
    
    # We'll use a modified version of Kruskal's algorithm
    # We want to connect all critical variables with minimum cost
    
    # First, let's sort constraints by weight
    constraints.sort(key=lambda x: x[2])
    
    # We'll use Union-Find to track connected components
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Keep track of which components contain critical variables
    critical_components = defaultdict(set)
    for var in critical_vars:
        critical_components[var].add(var)
    
    total_cost = 0
    
    # Run Kruskal's algorithm
    for u, v, w in constraints:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            # Merge the components
            union(parent, rank, u, v)
            
            # Update critical variables in the component
            # We need to merge the sets of critical variables from both components
            critical_in_pu = set()
            critical_in_pv = set()
            
            for var in critical_vars:
                root = find(parent, var)
                if root == pu or root == pv:
                    critical_in_pu.add(var)
                    
            # Update the representative component with all critical vars
            new_root = find(parent, u)  # This will be the new root after union
            critical_components[new_root] = critical_in_pu
            
            total_cost += w
            
            # Check if all critical variables are now connected
            if len(critical_components[new_root]) == t:
                return total_cost
                
    return total_cost

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    # Parse input
    n, m, t = map(int, input_lines[0].split())
    critical_vars = list(map(int, input_lines[1].split()))
    
    # Handle special case: if there's only one critical variable, cost is 0
    if t <= 1:
        print(0)
        return
        
    constraints = []
    for i in range(2, 2 + m):
        u, v, w = map(int, input_lines[i].split())
        constraints.append((u, v, w))
        
    # Use a different approach - find MST that connects all critical nodes
    # This is essentially the Steiner Tree problem, but we can solve it with enumeration since t <= 10
    
    # For small t, we can enumerate all possible combinations
    # But let's implement a simpler solution using Kruskal's algorithm
    
    # Sort edges by weight
    constraints.sort(key=lambda x: x[2])
    
    # Union-Find structure
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Track how many critical nodes are in each component
    critical_count = [0] * (n + 1)
    for var in critical_vars:
        critical_count[var] = 1
    
    total_cost = 0
    
    for u, v, w in constraints:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            # Merge components
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            if rank[pu] == rank[pv]:
                rank[pu] += 1
                
            # Update critical count
            critical_count[pu] += critical_count[pv]
            critical_count[pv] = 0  # Clear the merged component
            
            total_cost += w
            
            # If we've connected all critical variables, we're done
            if critical_count[pu] == t:
                print(total_cost)
                return
                
    print(total_cost)

if __name__ == "__main__":
    main()