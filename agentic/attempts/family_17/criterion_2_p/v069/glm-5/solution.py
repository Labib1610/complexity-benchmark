import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    q = int(input[0])
    t = int(input[1])
    
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(input[idx])
        b = int(input[idx+1])
        idx += 2
        adj[a].append(b)
        
    match_to_artifact = [0] * (2 * q + 1)
    match_to_cabinet = [0] * (q + 1)
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_to_artifact[v] == 0 or dfs(match_to_artifact[v], visited):
                    match_to_artifact[v] = u
                    match_to_cabinet[u] = v
                    return True
        return False

    match_count = 0
    for u in range(1, q + 1):
        visited = [False] * (2 * q + 1)
        if dfs(u, visited):
            match_count += 1
            
    if match_count == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_to_cabinet[u])
    else:
        print("NO")

if __name__ == '__main__':
    solve()