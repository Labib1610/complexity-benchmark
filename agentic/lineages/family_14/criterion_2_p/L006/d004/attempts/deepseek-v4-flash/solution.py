import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # DP: dp[u] = minimum cost to connect all priority nodes in subtree of u
    # If u is priority, we must include it.
    # We'll do a DFS from any node, say 1.
    
    visited = [False] * (n+1)
    dp = [0] * (n+1)
    has_priority = [False] * (n+1)
    
    def dfs(u):
        visited[u] = True
        if u in priority:
            has_priority[u] = True
        total = 0
        for v, w in adj[u]:
            if not visited[v]:
                dfs(v)
                if has_priority[v]:
                    total += min(w, dp[v])
                    has_priority[u] = True
        dp[u] = total
    
    dfs(1)
    
    # The answer is the dp value at the root if it has priority, else we need to find
    # the minimal subtree connecting all priority nodes.
    # Since the tree is connected, we can just take the dp at the root if it has priority,
    # otherwise we need to find the minimal cost to connect all priority nodes.
    # Actually, the dp computed above gives the cost to connect all priority nodes in the subtree.
    # If root has no priority, we need to sum over all children that have priority.
    
    # Better approach: compute for each node the cost to connect all priority nodes in its subtree,
    # and then find the minimal total cost by considering the tree as rooted at any priority node.
    
    # Let's root at the first priority node.
    root = next(iter(priority))
    visited = [False] * (n+1)
    dp = [0] * (n+1)
    has_priority = [False] * (n+1)
    
    def dfs2(u):
        visited[u] = True
        if u in priority:
            has_priority[u] = True
        total = 0
        for v, w in adj[u]:
            if not visited[v]:
                dfs2(v)
                if has_priority[v]:
                    total += min(w, dp[v])
                    has_priority[u] = True
        dp[u] = total
    
    dfs2(root)
    print(dp[root])

if __name__ == "__main__":
    solve()