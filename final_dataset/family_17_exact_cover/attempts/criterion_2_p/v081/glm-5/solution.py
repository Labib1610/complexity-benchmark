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
        
    match_r = [0] * (2 * q + 1)
    visited = [0] * (q + 1)
    visited_token = 1
    
    def dfs(u):
        for v in adj[u]:
            if match_r[v] == 0:
                match_r[v] = u
                return True
        for v in adj[u]:
            if visited[match_r[v]] != visited_token:
                visited[match_r[v]] = visited_token
                if dfs(match_r[v]):
                    match_r[v] = u
                    return True
        return False

    for u in range(1, q + 1):
        visited_token += 1
        if not dfs(u):
            print("NO")
            return
            
    print("YES")
    for v in range(q + 1, 2 * q + 1):
        if match_r[v] != 0:
            print(match_r[v], v)

if __name__ == '__main__':
    solve()