import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color each component as 0 or 1 (bipartite check)
    color = [-1] * n
    components = []
    
    for i in range(n):
        if color[i] == -1:
            # BFS to color component
            queue = deque()
            queue.append(i)
            color[i] = 0
            comp_nodes = [[], []]
            comp_nodes[0].append(i)
            
            bipartite = True
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        comp_nodes[color[nei]].append(nei)
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        bipartite = False
            
            if not bipartite:
                print("NO")
                return
            
            components.append(comp_nodes)
    
    # For each edge, check the product condition
    # c1 = 3+4i, c2 = 3-4i
    # c1*c1 = (3+4i)^2 = 9 + 24i -16 = -7 + 24i
    # c2*c2 = (3-4i)^2 = 9 - 24i -16 = -7 - 24i
    # c1*c2 = (3+4i)(3-4i) = 9 + 16 = 25
    # So we need Re(c_u * c_v) > 0 => u and v have different assignments
    
    # This means for every edge (u,v), s_u != s_v
    # This is exactly a bipartite graph coloring with colors 1 and 2
    # We already checked bipartiteness, now assign values
    
    # For each component, we can choose which side gets 1 and which gets 2
    # We want the lexicographically smallest assignment
    
    assignment = [0] * n
    
    for comp_nodes in components:
        part0, part1 = comp_nodes
        # Try assigning 1 to part0 and 2 to part1
        # vs assigning 2 to part0 and 1 to part1
        # Choose the one that gives lexicographically smaller result
        
        # Find the first node in this component according to original indices
        nodes_list = part0 + part1
        first_node = min(nodes_list)
        
        # Determine which part the first_node belongs to
        if first_node in part0:
            # Assign 1 to part0, 2 to part1
            for node in part0:
                assignment[node] = 1
            for node in part1:
                assignment[node] = 2
        else:
            # Assign 2 to part0, 1 to part1
            for node in part0:
                assignment[node] = 2
            for node in part1:
                assignment[node] = 1
    
    # Check if any self-loop exists (which would make Re(c*c) = -7 < 0)
    for u, v in edges:
        if u == v:
            print("NO")
            return
    
    print("YES")
    # Convert 0/1 to 1/2 if needed, but our assignment is already 1/2
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()