import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 and 2 are the two colors (spin states)
    color = [0] * (n + 1)
    
    # Check each component
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
            
        # BFS to color the component
        queue = deque()
        queue.append(start)
        color[start] = 1  # Start with spin state 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # Because 1 -> 2 and 2 -> 1
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    # Conflict found
                    print("NO")
                    return
    
    # If we reach here, a valid assignment exists
    print("YES")
    # Assign spin state 1 to unlinked nodes to ensure lexicographically smallest
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append(str(color[i]))
    print(' '.join(result))

if __name__ == "__main__":
    main()