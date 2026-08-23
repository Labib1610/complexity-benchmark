import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for the graph
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS for each component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 1  # Start with color 1
        
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
    
    # If we reach here, the graph is bipartite
    # The color array already gives a valid assignment
    # We need to make it lexicographically smallest
    # That means, for each component, if node 1 is in it, it should be color 1
    # If node 1 is not in the component, then the first node (smallest index) should be color 1
    
    # To ensure lex smallest, we can re-color components if needed
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        # BFS to get the component
        component = []
        queue = deque()
        queue.append(i)
        visited[i] = True
        component.append(i)
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    component.append(v)
        
        # In the component, find the minimum node
        min_node = min(component)
        # If its color is 2, we flip the whole component
        if color[min_node] == 2:
            for node in component:
                color[node] = 3 - color[node]
    
    print("YES")
    print(' '.join(map(str, color[1:])))

if __name__ == "__main__":
    main()