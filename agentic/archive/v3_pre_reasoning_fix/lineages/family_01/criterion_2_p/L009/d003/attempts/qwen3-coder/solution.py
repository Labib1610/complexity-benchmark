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
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each edge (u,v), the average of p_u and p_v must be 1.5
    # That means p_u + p_v = 3
    # So if p_u = 1, then p_v = 2, and vice versa.
    # This is a bipartite graph check.
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue:
            u = queue.popleft()
            c = color[u]
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - c  # flips 1->2 and 2->1
                    queue.append(v)
                elif color[v] == c:
                    return False  # Not bipartite
        return True
    
    # Check if all components are bipartite
    for i in range(1, n + 1):
        if color[i] == 0 and adj[i]:  # Only start BFS if node has neighbors
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, a valid assignment exists.
    # We need the lexicographically smallest one.
    # In a bipartite graph, we can choose which side gets 1 or 2.
    # To get lex smallest, for each component, we try assigning 1 to the side that contains the earliest node.
    
    visited = [False] * (n + 1)
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:
            # Collect component
            component_nodes = []
            queue = deque()
            queue.append(i)
            visited[i] = True
            component_nodes.append(i)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        component_nodes.append(v)
                        queue.append(v)
            
            # Determine bipartition
            comp_color = [0] * (n + 1)
            comp_color[i] = 1
            queue = deque()
            queue.append(i)
            
            bipartite = True
            while queue:
                u = queue.popleft()
                c = comp_color[u]
                for v in adj[u]:
                    if comp_color[v] == 0:
                        comp_color[v] = 3 - c
                        queue.append(v)
                    elif comp_color[v] == c:
                        bipartite = False
                        break
                if not bipartite:
                    break
            
            if not bipartite:
                print("NO")
                return
                
            # Assign colors to minimize lex order
            # Find the first node in component
            first_node = min(component_nodes)
            desired_color_for_first = 1
            actual_color_of_first = comp_color[first_node]
            
            if actual_color_of_first == desired_color_for_first:
                # Keep as is
                for node in component_nodes:
                    result[node] = comp_color[node]
            else:
                # Flip
                for node in component_nodes:
                    result[node] = 3 - comp_color[node]
        
        elif not visited[i]:  # Isolated node
            visited[i] = True
            result[i] = 1  # Assign 1 to isolated nodes for lex smallest
    
    # Handle any remaining unvisited nodes (shouldn't happen but just in case)
    for i in range(1, n + 1):
        if result[i] == 0:
            result[i] = 1
    
    print("YES")
    print(" ".join(map(str, result[1:])))

if __name__ == "__main__":
    main()