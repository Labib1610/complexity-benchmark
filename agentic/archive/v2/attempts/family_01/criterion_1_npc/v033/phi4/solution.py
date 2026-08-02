from sys import stdin

def solve():
    def dfs(process):
        if process == n + 1:
            print("YES")
            print(*assignments)
            exit()
        
        for channel in range(1, 4):
            valid = True
            for neighbor in graph[process]:
                if assignments[neighbor] == channel:
                    valid = False
                    break
            
            if not valid:
                continue

            assignments[process] = channel
            dfs(process + 1)
            assignments[process] = 0
    
    n, m = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    assignments = [0] * (n + 1)
    dfs(1)
    print("NO")

solve()