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
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        edge_indices[u].append(i)
        edge_indices[v].append(i)
    
    # The footprint is the product of (s_u + s_v) for each edge (u,v)
    # We want this product to be 3^m
    # Since each s_i is in {1,2}, each (s_u + s_v) is in {2, 3, 4}
    # For the product to be 3^m, each factor must be 3
    # So for every edge (u,v), we must have s_u + s_v = 3
    # This means (s_u, s_v) is either (1,2) or (2,1)
    
    # This is equivalent to 2-coloring the graph where each edge must connect colors 1 and 2
    # That is, the graph must be bipartite
    
    # If the graph is not bipartite, return "NO"
    # Otherwise, find a valid 2-coloring and check lex smallest
    
    color = [-1] * (n + 1)
    result = [1] * (n + 1)
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # The graph is bipartite. Assign states based on the bipartition
    # Color 0 -> state 1, Color 1 -> state 2
    for i in range(1, n + 1):
        if color[i] == 0:
            result[i] = 1
        else:
            result[i] = 2
    
    # Now we need to ensure it's lexicographically smallest
    # We can flip the entire coloring (1 <-> 2) and still have a valid configuration
    # We choose the one that gives lexicographically smaller sequence
    
    # To get lex smallest, we try both colorings and pick the better one
    option1 = []
    option2 = []
    for i in range(1, n + 1):
        option1.append(result[i])
        option2.append(3 - result[i])
    
    # Compare lexicographically
    chosen = option1
    for i in range(n):
        if option1[i] < option2[i]:
            chosen = option1
            break
        elif option1[i] > option2[i]:
            chosen = option2
            break
    
    print("YES")
    print(" ".join(map(str, chosen)))

if __name__ == "__main__":
    main()