def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]
    
    graph = defaultdict(set)
    for u, v in edges:
        graph[u - 1].add(v - 1)
        graph[v - 1].add(u - 1)
    
    colors = [-1] * n
    
    def is_valid(node, color):
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def assign_colors(node):
        if node == n:
            return True
        
        for color in range(3):
            if is_valid(node, color):
                colors[node] = color
                if assign_colors(node + 1):
                    return True
                colors[node] = -1
        
        return False
    
    if assign_colors(0):
        print("YES")
        print(' '.join(str(c + 1) for c in colors))
    else:
        print("NO")

main()