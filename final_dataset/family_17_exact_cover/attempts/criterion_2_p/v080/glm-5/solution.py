import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        q = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for vocalists (1 to q)
    adj = [[] for _ in range(q + 1)]
    
    # Read edges
    for _ in range(t):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
    
    # match_v[v] = u means instrumentalist v is matched with vocalist u
    match_v = [0] * (2 * q + 1)
    
    def dfs(u, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match_v[v] == 0 or dfs(match_v[v], visited):
                match_v[v] = u
                return True
        return False

    # Run matching
    for u in range(1, q + 1):
        visited = [False] * (2 * q + 1)
        if not dfs(u, visited):
            print("NO")
            return

    # All matched
    print("YES")
    # Output matches in order of vocalists 1 to q
    match_u = [0] * (q + 1)
    for v in range(q + 1, 2 * q + 1):
        u = match_v[v]
        match_u[u] = v
    
    for u in range(1, q + 1):
        print(f"{u} {match_u[u]}")

if __name__ == "__main__":
    solve()