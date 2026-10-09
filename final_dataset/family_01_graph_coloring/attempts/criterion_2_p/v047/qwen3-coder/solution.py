import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v))
    
    # Check if the graph is bipartite
    color = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            if visited[u]:
                continue
            visited[u] = True
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:
            if not bfs(i):
                print("NO")
                return
    
    # Assign default color 0 to isolated nodes
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
    
    # Now we need to check the condition on the sum of degrees
    # In any valid assignment, the number of edges crossing between partitions should be m
    # That means all edges are between different partitions
    # This is true iff the graph is bipartite (which we already checked)
    # And we want the lexicographically smallest such partition
    
    # We have a valid bipartition given by color[1..n]
    # But we want the lexicographically smallest one
    # So for each connected component, we can choose which side gets 0 and which gets 1
    # Choose the one that gives lexicographically smaller result
    
    # Let's recompute components and make consistent choices
    visited_comp = [False] * (n + 1)
    final_color = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        if visited_comp[i]:
            continue
        if not adj[i]:  # Isolated node
            final_color[i] = 1
            visited_comp[i] = True
            continue
            
        # BFS to get component
        comp_nodes = []
        queue = deque()
        queue.append(i)
        visited_comp[i] = True
        comp_nodes.append(i)
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited_comp[v]:
                    visited_comp[v] = True
                    queue.append(v)
                    comp_nodes.append(v)
        
        # For this component, determine which coloring is lex smaller
        # Option 0: color as per current bipartition
        # Option 1: flip the colors
        
        option0 = []
        option1 = []
        for node in comp_nodes:
            option0.append(color[node])
            option1.append(1 - color[node])
        
        # Compare lexicographically
        use_option0 = (option0 <= option1)
        
        for node in comp_nodes:
            if use_option0:
                final_color[node] = color[node] + 1  # Convert 0,1 to 1,2
            else:
                final_color[node] = (1 - color[node]) + 1
                
    # Verify that all edges cross
    crossing_edges = 0
    for u, v in edges:
        if final_color[u] != final_color[v]:
            crossing_edges += 1
            
    if crossing_edges != m:
        print("NO")
        return
        
    # Also verify the degree sum condition
    sum_deg_p1 = 0
    sum_deg_p2 = 0
    count_p1 = 0
    count_p2 = 0
    
    for i in range(1, n+1):
        if final_color[i] == 1:
            sum_deg_p1 += degree[i]
            count_p1 += 1
        else:
            sum_deg_p2 += degree[i]
            count_p2 += 1
            
    if sum_deg_p1 + sum_deg_p2 != 2 * m:
        print("NO")
        return
    
    print("YES")
    print(" ".join(map(str, final_color[1:])))

if __name__ == "__main__":
    main()