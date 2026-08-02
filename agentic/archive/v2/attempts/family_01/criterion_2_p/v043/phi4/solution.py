def shift_allocation():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    # Create adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Try to color the graph using two colors (1 and 2)
    shift_assignment = [0] * (n + 1)
    
    def is_bipartite(node, color):
        if shift_assignment[node] != 0:
            return shift_assignment[node] == color
        shift_assignment[node] = color
        
        for neighbor in graph[node]:
            if not is_bipartite(neighbor, 3 - color):  # Switch colors between 1 and 2
                return False
        return True

    possible = True
    for i in range(1, n + 1):
        if shift_assignment[i] == 0:  # Not yet colored
            if not is_bipartite(i, 1):  # Try to color with 1
                possible = False
                break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        result = [str(shift_assignment[i]) for i in range(1, n + 1)]
        print(" ".join(result))

shift_allocation()