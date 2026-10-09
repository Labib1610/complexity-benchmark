import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2

    # Check the orbital equilibrium equation for possible assignments
    # s_u and s_v can be 1 or 2
    valid_pairs = set()
    for s1 in [1, 2]:
        for s2 in [1, 2]:
            if s1**3 + s2**3 + (s1 * s2)**2 == 13:
                valid_pairs.add((s1, s2))
                valid_pairs.add((s2, s1))

    # For each edge, the pair of values must be in valid_pairs
    # This defines a 2-SAT problem
    
    # We'll model this as a graph coloring problem (since we only have 2 colors)
    # and check if the graph is bipartite. But we need to be more careful.
    # Actually, it's a constraint satisfaction problem.
    
    # Let's think of it this way:
    # Each satellite can be assigned 1 or 2.
    # For each edge (u,v), the pair (s_u, s_v) must be in valid_pairs.
    
    # Valid pairs are: (1,2) and (2,1) only.
    # Because:
    # 1,1: 1+1+1 = 3 != 13
    # 1,2: 1+8+4 = 13 OK
    # 2,1: 8+1+4 = 13 OK
    # 2,2: 8+8+16 = 32 != 13
    
    # So adjacent satellites must have different values.
    # This is a bipartite graph check.
    
    # Build the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Color the graph with BFS to check bipartiteness and get the lexicographically smallest coloring
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    
    for i in range(1, n + 1):
        if color[i] == -1:
            # Start BFS with color 0 (which corresponds to value 1)
            queue = deque()
            queue.append(i)
            color[i] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict: not bipartite
                        print("NO")
                        return
    
    # If we reach here, a valid coloring exists
    # Convert color 0 -> 1, color 1 -> 2 to get the actual values
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    main()