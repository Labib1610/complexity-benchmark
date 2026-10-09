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
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Color the graph with 2 colors (1 and 2). Bipartite check.
    color = [0] * (n + 1)  # 0 means unvisited, 1 and 2 are the two colors
    
    # Check each component
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            while queue:
                node = queue.popleft()
                current_color = color[node]
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - current_color  # flips 1->2 and 2->1
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If bipartite, construct the lexicographically smallest solution
    # We want the sequence to be lex smallest, so we prefer color 1 over 2
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()