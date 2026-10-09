import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    R, S, P = map(int, input().split())
    mandatory = set(map(int, input().split()))
    
    adj = [[] for _ in range(R + 1)]
    for _ in range(S):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (R + 1)
    total_cost = 0
    
    def dfs(u):
        nonlocal total_cost
        visited[u] = True
        has_mandatory = u in mandatory
        for v, w in adj[u]:
            if not visited[v]:
                child_has = dfs(v)
                if child_has and has_mandatory:
                    total_cost += w
                has_mandatory = has_mandatory or child_has
        return has_mandatory
    
    # Start from any mandatory node
    start = next(iter(mandatory))
    dfs(start)
    
    print(total_cost)

if __name__ == "__main__":
    solve()