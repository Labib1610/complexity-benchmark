import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    graph = defaultdict(list)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # Color the graph with 2 colors (1 and 2). This is essentially checking bipartiteness.
    color = [-1] * n
    
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 1  # Start coloring with 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # flips 1->2 and 2->1
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # If we reach here, the graph is bipartite and a valid assignment exists.
    # The color array gives us the assignment. We need to map 1->1 and 2->2.
    # Since we want the lexicographically smallest sequence, and we started with color 1,
    # this should already be the case.
    
    print("YES")
    result = []
    for c in color:
        result.append(str(c))
    print(' '.join(result))

if __name__ == "__main__":
    main()