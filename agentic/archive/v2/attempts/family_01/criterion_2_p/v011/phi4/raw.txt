from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2

    def dfs(node, color):
        if node in colors:
            return colors[node] == color
        colors[node] = color
        for neighbor in graph[node]:
            if not dfs(neighbor, 3 - color):
                return False
        return True

    colors = {}
    
    for i in range(1, n + 1):
        if i not in colors:
            if not dfs(i, 1):
                print("NO")
                return
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        result.append(colors[i])
    print(*result)

if __name__ == "__main__":
    solve()