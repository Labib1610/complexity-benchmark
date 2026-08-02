def is_bipartite(graph, n):
    color = [-1] * n
    for start in range(n):
        if color[start] == -1:  # Not colored yet
            queue = [start]
            color[start] = 0  # Start coloring with 0
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # Not colored
                        color[neighbor] = 1 - color[node]  # Alternate color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # Conflict
                        return False, []
    return True, color

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n)]
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    bipartite, color = is_bipartite(graph, n)
    
    if not bipartite:
        print("NO")
        return
    
    # Convert color to shifts
    shifts = [c + 1 for c in color]  # +1 to convert from {0, 1} to {1, 2}
    # Assigning the third shift to uncolored workers (if any)
    for i in range(n):
        if shifts[i] == 1:
            shifts[i] = 1
        elif shifts[i] == 0:
            shifts[i] = 2
            
    print("YES")
    print(" ".join(map(str, shifts)))

if __name__ == "__main__":
    main()