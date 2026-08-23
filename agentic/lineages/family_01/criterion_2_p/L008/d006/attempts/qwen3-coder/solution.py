import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = defaultdict(list)
    index = 2
    edges = []
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        index += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # If no edges, we can assign all 1s (lexicographically smallest)
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try to 2-color the graph (each node gets value 1 or 2)
    # The constraint is that adjacent nodes must have values differing by exactly 1
    # That means the graph must be bipartite and we assign colors 1 and 2
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    assignment = [0] * n  # Will store 1 or 2
    
    # Check if the graph is bipartite
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0
            assignment[start] = 1
            
            while queue:
                u = queue.popleft()
                current_val = assignment[u]
                neighbor_val = 2 if current_val == 1 else 1
                
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        assignment[v] = neighbor_val
                        queue.append(v)
                    elif assignment[v] != neighbor_val:
                        print("NO")
                        return
    
    # Verify all edges satisfy the constraint
    for u, v in edges:
        if abs(assignment[u] - assignment[v]) != 1:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()