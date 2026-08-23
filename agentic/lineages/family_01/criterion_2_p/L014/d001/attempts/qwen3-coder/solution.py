import sys
sys.setrecursionlimit(10**6)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    color = [0] * (n+1)  # 0 means unvisited, 1 and 2 are the two colors/funds
    visited = [False] * (n+1)
    
    def dfs(node, c):
        visited[node] = True
        color[node] = c
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if not dfs(neighbor, 3 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True
    
    for i in range(1, n+1):
        if not visited[i]:
            if not dfs(i, 1):
                print("NO")
                return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()