import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priorities = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # If only one priority node, no edges needed
    if t == 1:
        print(0)
        return
    
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        count = 1 if u in priorities else 0
        total_cost = 0
        for v, w in adj[u]:
            if not visited[v]:
                sub_count, sub_cost = dfs(v)
                if sub_count > 0 and (t - sub_count) > 0:
                    total_cost += w + sub_cost
                else:
                    total_cost += sub_cost
                count += sub_count
        return count, total_cost
    
    # Start DFS from any node (1)
    _, result = dfs(1)
    print(result)

if __name__ == "__main__":
    solve()