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
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # For each edge (u,v), we need (p[u] XOR p[v]) = 3
    # Since p[u], p[v] are in {1,2}, let's see what XOR values are possible:
    # 1 XOR 1 = 0
    # 1 XOR 2 = 3
    # 2 XOR 1 = 3
    # 2 XOR 2 = 0
    # So we need p[u] != p[v]
    
    # This is a 2-coloring problem: each component must be bipartite
    
    color = [-1] * n  # -1 means unvisited, 0 and 1 are the two colors
    visited = [False] * n
    
    for start in range(n):
        if visited[start]:
            continue
        # BFS to check if component is bipartite and assign colors
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = 1 - current_color
                    queue.append(neighbor)
                else:
                    if color[neighbor] == current_color:
                        print("NO")
                        return
    
    # If bipartite, construct assignment
    # We want lexicographically smallest assignment
    # Color 0 -> mode 1, Color 1 -> mode 2 to get lex smallest
    assignment = []
    for i in range(n):
        if color[i] == 0:
            assignment.append('1')
        else:
            assignment.append('2')
    
    print("YES")
    print(" ".join(assignment))

if __name__ == "__main__":
    main()