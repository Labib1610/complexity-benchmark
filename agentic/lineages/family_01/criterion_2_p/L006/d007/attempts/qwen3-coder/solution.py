import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    edge_indices = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(data[2 + 2*i])
        v = int(data[2 + 2*i + 1])
        if u == v:
            print("NO")
            return
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        edge_indices[u].append(i)
        edge_indices[v].append(i)
    
    # For each edge (u,v), we need c_u * c_v = 2
    # So the pair (c_u, c_v) must be (1,2) or (2,1)
    
    # This is a 2-SAT problem. We can model it as a graph coloring problem.
    # Each variable c_i has two possible values: 1 or 2.
    # For each edge (u,v), we have the constraint: c_u * c_v = 2
    # That means:
    # - if c_u = 1, then c_v must be 2
    # - if c_u = 2, then c_v must be 1
    # - if c_v = 1, then c_u must be 2
    # - if c_v = 2, then c_u must be 1
    
    # We can build a graph with 2n nodes:
    # Node i represents c_i = 1
    # Node i + n represents c_i = 2
    
    # For each constraint c_u * c_v = 2:
    # Add edges:
    # u=1 -> v=2  (if u is 1, then v must be 2)
    # v=1 -> u=2  (if v is 1, then u must be 2)
    # u=2 -> v=1  (if u is 2, then v must be 1)
    # v=2 -> u=1  (if v is 2, then u must be 1)
    
    # But since we only have two values {1,2}, we can simplify:
    # Node u means c_u = 1
    # Node u + n means c_u = 2
    
    graph = [[] for _ in range(2 * n + 1)]
    
    for u, v in edges:
        # c_u * c_v = 2
        # If c_u = 1, then c_v = 2
        graph[u].append(v + n)
        # If c_v = 1, then c_u = 2
        graph[v].append(u + n)
        # If c_u = 2, then c_v = 1
        graph[u + n].append(v)
        # If c_v = 2, then c_u = 1
        graph[v + n].append(u)
    
    # Now we need to check if there's a valid assignment
    # We can do 2-SAT by checking strongly connected components
    
    def scc():
        # Kosaraju's algorithm
        visited = [False] * (2 * n + 1)
        order = []
        
        def dfs1(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)
        
        for i in range(1, 2 * n + 1):
            if not visited[i]:
                dfs1(i)
        
        # Build reverse graph
        rev_graph = [[] for _ in range(2 * n + 1)]
        for u in range(1, 2 * n + 1):
            for v in graph[u]:
                rev_graph[v].append(u)
        
        visited = [False] * (2 * n + 1)
        components = [-1] * (2 * n + 1)
        component_id = 0
        
        def dfs2(u):
            visited[u] = True
            components[u] = component_id
            for v in rev_graph[u]:
                if not visited[v]:
                    dfs2(v)
        
        while order:
            u = order.pop()
            if not visited[u]:
                dfs2(u)
                component_id += 1
        
        return components
    
    components = scc()
    
    # Check if for each variable, the two values are in different SCCs
    for i in range(1, n + 1):
        if components[i] == components[i + n]:
            print("NO")
            return
    
    # To get the lexicographically smallest assignment, we need to try setting variables to 1 first
    # We can do this by checking which node (x or x+n) has a higher component ID in the reverse topological order
    # In Kosaraju, the component_id increases with the finishing time in reverse
    
    assignment = [0] * (n + 1)
    
    # For each variable, if component of i > component of i+n, then set c_i = 1, else c_i = 2
    # But we need to be careful about the order. 
    # Actually, in Kosaraju, the first component found in the second DFS is the "sink" component
    # So higher component_id means later in topological order, which means it's a "source" in the implication graph
    # For 2-SAT: if comp(i) > comp(i+n), then i is forced to be False (0), so c_i = 2
    # If comp(i) < comp(i+n), then i is forced to be True (1), so c_i = 1
    
    # Wait, let's think carefully:
    # In the implication graph, if there's a path from node A to node B, then A being true forces B to be true
    # In Kosaraju, components are numbered in reverse topological order of the condensation
    # So if component_id of A < component_id of B, then A is "earlier" in the topological order
    # That means B is a "source" or "earlier" to be decided
    # For 2-SAT, if comp(x) > comp(not x), then x should be True to avoid contradiction
    
    for i in range(1, n + 1):
        if components[i] > components[i + n]:
            assignment[i] = 1
        else:
            assignment[i] = 2
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()