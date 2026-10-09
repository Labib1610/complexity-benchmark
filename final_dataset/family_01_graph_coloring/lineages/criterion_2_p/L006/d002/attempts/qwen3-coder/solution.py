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
    index = 2
    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * n
    visited = [False] * n
    
    # Check bipartiteness using BFS for each connected component
    for start in range(n):
        if visited[start]:
            continue
        queue = deque()
        queue.append(start)
        visited[start] = True
        color[start] = 1  # Start with color 1
        
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
    
    # If bipartite, construct the lexicographically smallest solution
    # We want s_u + s_v = 3 => if we color with 1 and 2, we can map:
    # color 1 -> state 1
    # color 2 -> state 2
    # This ensures s_u + s_v = 1+2 = 3 for every edge
    # To get lex smallest, we prefer node 0 to have state 1 if possible.
    # Actually, since we fixed the starting color as 1, and the coloring is unique up to swapping,
    # we just need to ensure our assignment gives lex smallest sequence.
    # Our coloring already ensures that: color 1 -> state 1, color 2 -> state 2
    # This will give us the lex smallest because we process nodes in order and always assign color 1 to the first unvisited node.
    
    result = []
    for c in color:
        if c == 1:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()