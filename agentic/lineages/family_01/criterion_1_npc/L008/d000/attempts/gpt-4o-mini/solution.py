def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    incompatibilities = [list(map(int, line.split())) for line in data[1:m + 1]]
    
    from itertools import combinations
    
    # Create an adjacency list for the incompatibility graph
    graph = [[] for _ in range(n + 1)]
    for u, v in incompatibilities:
        graph[u].append(v)
        graph[v].append(u)
    
    # We will store the color (block) of each personnel
    color = [0] * (n + 1)
    
    def is_valid():
        # Check if the current color assignment is valid
        for u in range(1, n + 1):
            for v in graph[u]:
                if color[u] == color[v]:  # incompatible pair in the same block
                    return False
        return True
    
    def dfs(person):
        if person > n:
            return is_valid()  # Check if the color assignment is valid
        
        for c in range(1, 4):  # Try colors 1, 2, 3
            color[person] = c
            if dfs(person + 1):
                return True
            color[person] = 0  # Reset color
        
        return False
    
    if dfs(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

main()