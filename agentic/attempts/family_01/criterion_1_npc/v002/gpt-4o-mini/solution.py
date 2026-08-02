def can_color(graph, n):
    colors = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are the channel colors
    
    def is_valid(node, color):
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def dfs(node):
        if node > n:
            return True
        
        for color in range(1, 4):  # Try colors 1, 2, 3
            if is_valid(node, color):
                colors[node] = color
                if dfs(node + 1):
                    return True
                colors[node] = 0  # Backtrack
        return False

    if dfs(1):
        return colors[1:]  # Exclude the 0th index
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    graph = [[] for _ in range(n + 1)]
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    result = can_color(graph, n)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()