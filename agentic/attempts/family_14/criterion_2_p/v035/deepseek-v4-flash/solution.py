import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    required = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # pick any required node as root
    root = next(iter(required))
    
    total_cost = 0
    
    def dfs(u, parent):
        nonlocal total_cost
        has_required = u in required
        for v, w in adj[u]:
            if v == parent:
                continue
            child_has = dfs(v, u)
            if child_has and (t - child_has > 0):
                total_cost += w
            has_required |= child_has
        return has_required
    
    dfs(root, -1)
    print(total_cost)

if __name__ == "__main__":
    solve()