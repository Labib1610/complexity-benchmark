import sys
from collections import deque, defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = defaultdict(list)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors (shifts)
    color = [0] * (n + 1)
    
    # Process nodes in order from 1 to n to ensure lexicographical minimality
    for start in range(1, n+1):
        if color[start] == 0:
            # BFS to check bipartiteness and assign colors
            queue = deque()
            queue.append(start)
            color[start] = 1  # Assign to shift 1 first
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 2 if current_color == 1 else 1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        # Conflict found, not bipartite
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()