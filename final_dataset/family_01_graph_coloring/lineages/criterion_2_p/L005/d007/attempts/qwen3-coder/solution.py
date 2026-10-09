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
    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        graph[u].append((v, len(edges)-1))
        graph[v].append((u, len(edges)-1))
        index += 2
    
    # For each edge, the resonance factor must be x^3 + y^3
    # If x=1, y=1: 1+1=2
    # If x=1, y=2: 1+8=9
    # If x=2, y=1: 8+1=9
    # If x=2, y=2: 8+8=16
    # We want the product to be 9^m
    # So we need exactly m edges where x^3+y^3=9, i.e., one endpoint is 1, other is 2
    # All other edges must have x^3+y^3=1, which is impossible since min is 2
    # Or they must contribute factor 1, but that's also impossible
    # Actually, let's think differently:
    # Product over all edges of (x^3 + y^3) = 9^m
    # This means every edge must contribute a factor that multiplies to 9^m
    # Since 9 = 3^2, we need the prime factorization to be 3^{2m}
    # Let's see possible values:
    # 1^3 + 1^3 = 2
    # 1^3 + 2^3 = 9
    # 2^3 + 1^3 = 9  
    # 2^3 + 2^3 = 16
    # So only edges with one 1 and one 2 contribute factor 9
    # Edges with both 1 contribute 2
    # Edges with both 2 contribute 16
    # We want product = 9^m = 3^{2m}
    # But 2 = 2, 9 = 3^2, 16 = 2^4
    # So we can't get rid of factor 2 unless all edges are labeled 1-2
    # That means ALL edges must connect a 1-node to a 2-node
    # This is equivalent to checking if the graph is bipartite
    # And we want the bipartition to satisfy that every edge connects a 1-node to a 2-node
    # Which is exactly bipartite check
    
    # Check if the graph is bipartite
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, -1: color -1
    
    # Since the graph might not be connected, we need to check all components
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            for neighbor, _ in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = -current_color
                    queue.append(neighbor)
                else:
                    if color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If bipartite, assign colors such that the result is lexicographically smallest
    # Color 1 -> mode 1, Color -1 -> mode 2 to get lex smallest
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 1:
            assignment[i] = 1
        elif color[i] == -1:
            assignment[i] = 2
        else:
            assignment[i] = 1  # isolated vertex, just assign 1
    
    # Verify that this assignment gives product = 9^m
    # Every edge connects color 1 to color -1, so contributes 1^3 + 2^3 = 9
    # So product = 9^m, which is what we want
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

if __name__ == "__main__":
    main()