import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # degree of each node
    deg = [len(adj[i]) for i in range(n)]
    # suffix sum of degrees
    suffix_deg = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix_deg[i] = suffix_deg[i+1] + deg[i]
    
    colors = [0] * n
    found = False
    
    def dfs(idx, diff_count):
        nonlocal found
        if found:
            return
        if diff_count > m:
            return
        if diff_count + suffix_deg[idx] < m:
            return
        if idx == n:
            if diff_count == m:
                found = True
            return
        
        # try colors 1,2,3
        for c in (1,2,3):
            new_diff = diff_count
            for nb in adj[idx]:
                if nb < idx:
                    if colors[nb] != c:
                        new_diff += 1
            if new_diff > m:
                continue
            if new_diff + suffix_deg[idx+1] < m:
                continue
            colors[idx] = c
            dfs(idx+1, new_diff)
            if found:
                return
        colors[idx] = 0
    
    dfs(0, 0)
    
    if not found:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(c) for c in colors))

if __name__ == "__main__":
    solve()