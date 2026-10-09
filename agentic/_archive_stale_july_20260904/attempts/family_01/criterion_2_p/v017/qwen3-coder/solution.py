import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors (shifts)
    color = [0] * n
    visited = [False] * n
    
    # Check if bipartite using BFS and ensure lexicographical order
    for start in range(n):
        if visited[start]:
            continue
        queue = deque()
        queue.append(start)
        color[start] = 1  # Start with color 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 2 if current_color == 1 else 1
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    print("NO")
                    return
    
    # If we reach here, the graph is bipartite
    # Now we need to make sure the assignment is lexicographically smallest
    # Since we start coloring with '1' for each component's starting node,
    # and we process nodes in order (0 to n-1), this already ensures lex smallest
    # However, for each connected component, we have a choice: 
    # whether the starting node is 1 or 2.
    # To get lex smallest overall, among the two colorings of a component,
    # we choose the one that gives smaller label to the earliest node.
    
    # Actually, since we're doing BFS from the lowest indexed unvisited node each time,
    # and always assigning it color 1, this already ensures the lex smallest result.
    # Because in any valid coloring, flipping the colors in a component gives another valid coloring.
    # Our approach picks the one where the first node of the component gets color 1.
    
    print("YES")
    # Convert back to 1-based labels
    result = []
    for i in range(n):
        if color[i] == 1:
            result.append('1')
        else:
            result.append('2')
    print(' '.join(result))

if __name__ == "__main__":
    main()