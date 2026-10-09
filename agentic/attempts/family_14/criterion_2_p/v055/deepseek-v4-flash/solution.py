import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    contaminated = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # DFS to find the minimal subtree cost
    visited = [False] * (n + 1)
    
    def dfs(u, parent):
        visited[u] = True
        total_cost = 0
        has_contaminated = u in contaminated
        
        for v, w in adj[u]:
            if v == parent:
                continue
            child_cost, child_has = dfs(v, u)
            if child_has:
                total_cost += child_cost + w
                has_contaminated = True
        
        return total_cost, has_contaminated
    
    # Start DFS from any contaminated node
    start = next(iter(contaminated))
    total_cost, _ = dfs(start, -1)
    
    print(total_cost)

if __name__ == "__main__":
    solve()