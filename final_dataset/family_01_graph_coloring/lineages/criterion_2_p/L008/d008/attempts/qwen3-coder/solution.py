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
    
    # Build graph
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append((u, v))
    
    # For each component, we need to check bipartiteness
    color = [-1] * (n + 1)
    comp = [0] * (n + 1)
    comp_id = 1
    
    # Check if the graph is bipartite
    bipartite = True
    components = []
    
    for i in range(1, n + 1):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 0
            comp[i] = comp_id
            nodes = [i]
            
            while queue:
                u = queue.popleft()
                for v, _ in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        comp[v] = comp_id
                        queue.append(v)
                        nodes.append(v)
                    elif color[v] == color[u]:
                        bipartite = False
                        break
                if not bipartite:
                    break
            
            components.append(nodes)
            comp_id += 1
            if not bipartite:
                break
    
    if not bipartite:
        print("NO")
        return
    
    # For each component, assign modes based on bipartition
    # We want lexicographically smallest assignment
    # Color 0 -> mode 1, Color 1 -> mode 2 to get lex smallest
    result = [0] * (n + 1)
    
    for nodes in components:
        # Determine which coloring gives lexicographically smaller result
        # Try both assignments and pick the better one
        option1 = {}
        option2 = {}
        
        first_node = min(nodes)
        
        for node in nodes:
            option1[node] = 1 if color[node] == 0 else 2
            option2[node] = 1 if color[node] == 1 else 2
        
        # Compare which one is lexicographically smaller at the first node
        if option1[first_node] < option2[first_node]:
            chosen = option1
        elif option1[first_node] > option2[first_node]:
            chosen = option2
        else:
            # Need to compare further, but since it's bipartite and we're just swapping,
            # we can decide based on the pattern. To get lex smallest, we prefer 1 over 2
            # at the earliest position. Since first_node is the minimum, and we've already
            # compared, we stick with option1 if equal.
            chosen = option1
            
        for node in nodes:
            result[node] = chosen[node]
    
    print("YES")
    print(" ".join(map(str, result[1:])))

if __name__ == "__main__":
    main()