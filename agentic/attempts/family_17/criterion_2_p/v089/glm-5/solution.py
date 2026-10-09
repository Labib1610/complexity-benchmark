import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    ptr = 0
    q = int(input[ptr])
    ptr += 1
    t = int(input[ptr])
    ptr += 1
    
    N = 2 * q
    adj = [[] for _ in range(N + 1)]
    for _ in range(t):
        a = int(input[ptr])
        ptr += 1
        b = int(input[ptr])
        ptr += 1
        adj[a].append(b)
        adj[b].append(a)
        
    match = [0] * (N + 1)
    
    for u in range(1, q + 1):
        visited = [False] * (N + 1)
        
        def dfs(u):
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if match[v] == 0 or dfs(match[v]):
                        match[u] = v
                        match[v] = u
                        return True
            return False
            
        if not dfs(u):
            print("NO")
            return
            
    print("YES")
    for u in range(1, q + 1):
        print(u, match[u])

if __name__ == '__main__':
    solve()