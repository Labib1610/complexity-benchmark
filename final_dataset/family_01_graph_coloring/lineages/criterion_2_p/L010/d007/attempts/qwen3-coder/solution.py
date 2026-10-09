import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        index += 2

    # Check resonance condition: s_u^3 + s_v^3 = 9
    # Since s_u, s_v ∈ {1,2}, we have:
    # 1^3 = 1, 2^3 = 8
    # So 1^3 + 2^3 = 9 and 2^3 + 1^3 = 9
    # Therefore, adjacent nodes must have different values (one 1, one 2)

    # This is a 2-coloring problem (bipartite check)
    color = [-1] * n
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # Check if the graph is bipartite
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # If bipartite, assign colors to minimize E
    # E = sum(s_i * 3^(n-1-i)) for i=0 to n-1
    # To minimize E, we want smaller values (1) in higher-weight positions (left)
    # So we should assign 1 to nodes with color 0 in earlier positions if possible
    
    # But since we need a valid 2-coloring, we just assign:
    # Color 0 -> 1
    # Color 1 -> 2
    
    # However, we can swap the roles of color 0 and 1 to get minimal E
    # Try both assignments and pick the one with smaller E
    
    def calculate_E(assignments):
        E = 0
        for i in range(n):
            E += assignments[i] * (3 ** (n - 1 - i))
        return E
    
    assignment1 = [1 if color[i] == 0 else 2 for i in range(n)]
    assignment2 = [2 if color[i] == 0 else 1 for i in range(n)]
    
    E1 = calculate_E(assignment1)
    E2 = calculate_E(assignment2)
    
    if E1 <= E2:
        result = assignment1
    else:
        result = assignment2
        
    print("YES")
    print(' '.join(map(str, result)))

solve()