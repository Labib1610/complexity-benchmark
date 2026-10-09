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
        idx += 2
        adj[a].append(b)
        
    for a in range(1, q + 1):
        adj[a].sort()
        
    match_R = [0] * (2 * q + 1)
    match_L = [0] * (q + 1)
    
    def dfs(u, vis):
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                if match_R[v] == 0 or dfs(match_R[v], vis):
                    match_R[v] = u
                    match_L[u] = v
                    return True
        return False

    for u in range(1, q + 1):
        vis = [False] * (2 * q + 1)
        dfs(u, vis)
        
    for u in range(1, q + 1):
        if match_L[u] == 0:
            print("NO")
            return
            
    print("YES")
    for u in range(1, q + 1):
        print(u, match_L[u])

if __name__ == '__main__':
    solve()