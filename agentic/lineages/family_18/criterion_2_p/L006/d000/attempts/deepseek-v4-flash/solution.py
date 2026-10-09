import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Compute subtree sizes and min cost
    size = [0] * n
    min_cost = 0
    
    def dfs1(u, parent):
        nonlocal min_cost
        size[u] = 1
        for v in adj[u]:
            if v != parent:
                dfs1(v, u)
                size[u] += size[v]
                min_cost += size[v] * (n - size[v])
    
    dfs1(0, -1)
    
    if min_cost > B:
        print("NO")
        return
    
    # Assign slots via DFS preorder
    pos = [0] * n
    cur = 1
    def dfs2(u, parent):
        nonlocal cur
        pos[u] = cur
        cur += 1
        for v in adj[u]:
            if v != parent:
                dfs2(v, u)
    
    dfs2(0, -1)
    
    print("YES")
    print(" ".join(str(pos[i]) for i in range(n)))

if __name__ == "__main__":
    solve()