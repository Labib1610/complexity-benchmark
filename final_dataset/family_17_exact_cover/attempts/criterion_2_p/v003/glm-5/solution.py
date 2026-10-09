import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        adj[a].append(b - q)
        idx += 2
        
    match_to_c = [0] * (q + 1)
    match_to_p = [0] * (q + 1)
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_to_c[v] == 0 or dfs(match_to_c[v], visited):
                    match_to_c[v] = u
                    match_to_p[u] = v
                    return True
        return False

    for u in range(1, q + 1):
        visited = [False] * (q + 1)
        if not dfs(u, visited):
            sys.stdout.write("NO\n")
            return
            
    sys.stdout.write("YES\n")
    for u in range(1, q + 1):
        sys.stdout.write(f"{u} {match_to_p[u] + q}\n")

if __name__ == '__main__':
    solve()