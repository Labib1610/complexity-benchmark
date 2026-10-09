import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    required = set(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count required nodes in subtree
    visited = [False] * (n+1)
    count = [0] * (n+1)
    
    def dfs(u):
        visited[u] = True
        cnt = 1 if u in required else 0
        for v, w in adj[u]:
            if not visited[v]:
                cnt += dfs(v)
        count[u] = cnt
        return cnt
    
    # start from any required node
    start = next(iter(required))
    dfs(start)
    
    total_cost = 0
    for u, v, w in edges:
        # if one side has required nodes and the other side also has required nodes
        # then this edge is on the Steiner tree
        if count[u] > 0 and count[u] < t:
            total_cost += w
        elif count[v] > 0 and count[v] < t:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()