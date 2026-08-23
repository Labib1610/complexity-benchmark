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
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque()
            queue.append(start)
            color[start] = 1
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color  # flips 1->2 and 2->1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        print("NO")
                        return
    
    # If we reach here, it's bipartite
    # We need the lexicographically smallest assignment
    # That means we prefer to assign color 1 to lower-numbered nodes when possible
    # But our coloring already ensures that: we started with node 1 and gave it color 1
    # The bipartition is fixed once we decide the color of the first node in each component
    # To get lex smallest, we can ensure that in each component, 
    # the smallest node gets color 1
    
    # Re-color if necessary to make it lexicographically smallest
    # For each component, find the smallest node and ensure it has color 1
    visited_components = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited_components[start] and color[start] != 0:
            # Find all nodes in this component
            component_nodes = []
            queue = deque()
            queue.append(start)
            visited_components[start] = True
            component_nodes.append(start)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited_components[v]:
                        visited_components[v] = True
                        queue.append(v)
                        component_nodes.append(v)
            
            # Find the minimum node in this component
            min_node = min(component_nodes)
            
            # If the minimum node has color 2, we should swap the colors in this component
            if color[min_node] == 2:
                for node in component_nodes:
                    color[node] = 3 - color[node]
    
    # Now output the result
    print("YES")
    print(" ".join(str(color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()