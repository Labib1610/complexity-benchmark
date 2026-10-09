import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Build line graph: vertices are edges of original graph
    line_adj = [[] for _ in range(m)]
    for u in range(n):
        for i in range(len(adj[u])):
            for j in range(i+1, len(adj[u])):
                e1 = adj[u][i][1]
                e2 = adj[u][j][1]
                line_adj[e1].append(e2)
                line_adj[e2].append(e1)
    
    color = [-1] * m
    
    # Greedy coloring with backtracking for safety
    def dfs(e):
        if e == m:
            return True
        used = [False]*4
        for nb in line_adj[e]:
            if color[nb] != -1:
                used[color[nb]] = True
        for c in range(1, 4):
            if not used[c]:
                color[e] = c
                if dfs(e+1):
                    return True
                color[e] = -1
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()