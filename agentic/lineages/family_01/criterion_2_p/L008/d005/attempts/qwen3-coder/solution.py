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
    adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # For each edge (u,v), the contribution to the product is x^2 + y^2 - xy
    # We want the product of all such terms to be 3^m
    # Let's compute x^2 + y^2 - xy for all possible pairs (x,y) in {1,2}
    # (1,1): 1+1-1 = 1
    # (1,2): 1+4-2 = 3
    # (2,1): 4+1-2 = 3
    # (2,2): 4+4-4 = 4
    
    # So we need every edge to contribute a factor of 3.
    # That means for every edge (u,v), we need (c_u, c_v) to be (1,2) or (2,1)
    # This is equivalent to a 2-coloring problem where each edge must connect different colors
    # i.e., a bipartite graph check
    
    # Check if the graph formed by the edges is bipartite
    color = [-1] * (n+1)
    visited = [False] * (n+1)
    
    # Build the graph
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to check bipartiteness and assign colors
    for start in range(1, n+1):
        if not visited[start]:
            queue = deque()
            queue.append(start)
            color[start] = 0
            visited[start] = True
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If bipartite, construct the assignment
    # We want the lexicographically smallest assignment
    # Color 0 -> 1, Color 1 -> 2
    assignment = [0] * (n+1)
    for i in range(1, n+1):
        if color[i] == 0:
            assignment[i] = 1
        else:
            assignment[i] = 2
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()