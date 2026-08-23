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
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite (i.e., 2-colorable)
    # For each component, we start with color 1 for the first node
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            queue = deque()
            queue.append(i)
            color[i] = 1
            visited[i] = True
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # flips 1->2 and 2->1
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    else:
                        if color[neighbor] != next_color:
                            print("NO")
                            return
    
    # If we reach here, a valid coloring exists
    # We need to ensure it's lexicographically smallest
    # That means among the two possible colorings of each component,
    # we choose the one that gives the smallest lex sequence
    
    # For that, we can just check the first node of each component
    # and decide whether to flip the colors or not
    
    visited_check = [False] * (n + 1)
    final_color = color[:]
    
    for i in range(1, n + 1):
        if not visited_check[i]:
            # BFS again to collect all nodes in component
            component_nodes = []
            queue = deque()
            queue.append(i)
            visited_check[i] = True
            component_nodes.append(i)
            
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if not visited_check[neighbor]:
                        visited_check[neighbor] = True
                        component_nodes.append(neighbor)
                        queue.append(neighbor)
            
            # Decide whether to flip colors in this component
            # We want the first node (smallest index) to be as small as possible
            min_node = min(component_nodes)
            if final_color[min_node] == 2:
                # Flip all colors in this component
                for node in component_nodes:
                    final_color[node] = 3 - final_color[node]
    
    # Output result
    print("YES")
    print(" ".join(str(final_color[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()