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
    edge_indices = defaultdict(list)
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
        edge_indices[(min(u,v), max(u,v))].append(i)
        index += 2
    
    # For each edge, the thermal footprint must be 5
    # 2^{s_u} + 2^{s_v} - 1 = 5
    # 2^{s_u} + 2^{s_v} = 6
    # Possible pairs: (1,2) and (2,1) since 2^1 + 2^2 = 2 + 4 = 6
    # So for every edge, one endpoint must be 1 and the other must be 2
    
    # This is equivalent to a 2-coloring problem where each edge must connect nodes of different colors
    # Color 1 represents s=1, Color 2 represents s=2
    
    color = [0] * (n+1)  # 0 means unvisited, 1 and 2 are the two colors
    
    # Check if the graph is bipartite
    visited = [False] * (n+1)
    
    for start in range(1, n+1):
        if not visited[start]:
            queue = deque()
            queue.append(start)
            visited[start] = True
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # flips 1->2 and 2->1
                
                for neighbor, edge_idx in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    else:
                        # Check if the edge constraint is satisfied
                        if color[neighbor] != next_color:
                            print("NO")
                            return
    
    # If we reach here, a valid coloring exists
    # We need the lexicographically smallest sequence
    # That means we prefer s_i = 1 over s_i = 2 when possible
    # In our coloring, we used 1 and 2. We can map 1 -> 1 and 2 -> 2
    
    result = []
    for i in range(1, n+1):
        if color[i] == 0:  # Isolated vertex, choose 1 for lex smallest
            result.append("1")
        else:
            result.append(str(color[i]))
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()