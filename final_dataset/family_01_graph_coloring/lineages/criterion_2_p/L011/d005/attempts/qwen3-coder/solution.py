import sys
from collections import defaultdict, deque

def solve():
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
    adj = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # For each edge (u,v), the stability is 6(p_u + p_v) - (p_u + p_v)^2
    # We want the sum over all edges to be 9m
    # Let's analyze what values of (p_u + p_v) give a stability of 9:
    # 6x - x^2 = 9 => x^2 - 6x + 9 = 0 => (x-3)^2 = 0 => x = 3
    # So for each edge, we need p_u + p_v = 3
    # This means for each edge, one endpoint gets 1 and the other gets 2
    
    # This is equivalent to 2-coloring the graph where each edge must connect a 1-node and a 2-node
    # In other words, the graph must be bipartite and each edge must connect nodes from different partitions
    
    # But we also need p_u + p_v = 3 for every edge
    # This means the graph must be bipartite, and we assign 1 to one part and 2 to the other
    
    color = [-1] * n  # -1: unvisited, 0: color A (assign 1), 1: color B (assign 2)
    result = [0] * n
    
    # Check if the graph is bipartite
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 0
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If bipartite, assign 1 to color 0 nodes and 2 to color 1 nodes
    # This ensures p_u + p_v = 3 for every edge
    for i in range(n):
        result[i] = 1 if color[i] == 0 else 2
    
    # To get lexicographically smallest, we need to decide which color gets 1
    # Try both and pick the lex smaller one
    # Actually, we can just try assigning 1 to color 0 and see if it's lex smaller than the reverse
    # But to ensure lex smallest, we can do this:
    # Among all valid assignments (there are two: color 0 = 1 or color 0 = 2)
    # We want the lex smallest sequence
    
    option1 = []
    option2 = []
    for i in range(n):
        option1.append(1 if color[i] == 0 else 2)
        option2.append(2 if color[i] == 0 else 1)
    
    # Choose the lexicographically smaller one
    chosen = option1
    for i in range(n):
        if option1[i] < option2[i]:
            chosen = option1
            break
        elif option2[i] < option1[i]:
            chosen = option2
            break
    
    print("YES")
    print(" ".join(map(str, chosen)))

solve()