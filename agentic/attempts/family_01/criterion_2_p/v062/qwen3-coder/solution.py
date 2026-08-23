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
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        index += 2
    
    # Color array: -1 means unvisited, 0 and 1 are the two colors
    color = [-1] * n
    
    # Check if bipartite using BFS for each component
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Start coloring with 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If bipartite, construct the lexicographically smallest solution
    # Assign 0 -> 1 and 1 -> 2 (since shifts are 1 and 2)
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()