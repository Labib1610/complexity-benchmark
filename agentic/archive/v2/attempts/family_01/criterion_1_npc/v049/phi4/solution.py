import sys
input = sys.stdin.read

def solve():
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    def dfs(node, color):
        if used[node]:
            return colors[node] == color
        used[node] = True
        colors[node] = color
        for neighbor in graph[node]:
            if not dfs(neighbor, 6 - color):  # 6 - color gives the opposite color (1 <-> 3, 2 stays 2)
                return False
        return True
    
    def backtrack(pos):
        if pos > n:
            print("YES")
            for i in range(1, n + 1):
                sys.stdout.write(f"{colors[i]} ")
            sys.exit()
        
        for color in [1, 2, 3]:
            used[:] = [False] * (n + 1)
            colors[pos] = color
            if dfs(pos, color) and backtrack(pos + 1):
                return True
        
        return False
    
    # Try to assign each technician a frequency starting from the lexicographically smallest one
    colors = [0] * (n + 1)
    used = [False] * (n + 1)
    
    if not backtrack(1):
        print("NO")

solve()