import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Graph representation
    graph = defaultdict(list)
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # Since tiers must divide 2, possible tiers are {1, 2}
    # XOR condition: for any edge (u,v), tier[u] ^ tier[v] = 3
    # 1 ^ 2 = 3, so adjacent nodes must have different tiers
    
    # This is a 2-coloring problem (Bipartite check)
    color = [-1] * n  # -1: unvisited, 0: color A, 1: color B
    
    # Check each connected component
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Assign first color
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict: same color for adjacent nodes
                        print("NO")
                        return
    
    # Valid assignment exists
    print("YES")
    
    # To get lexicographically smallest assignment:
    # For each node, if color[node] == 0, assign 1; if color[node] == 1, assign 2
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print(' '.join(result))

if __name__ == "__main__":
    main()