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
        adj[u].append(i)
        adj[v].append(i)
    
    color = [-1] * m
    
    # Try to color edges with backtracking
    # Use MRV heuristic: pick edge with fewest available colors
    def available_colors(e):
        u, v = edges[e]
        used = set()
        for idx in adj[u]:
            if color[idx] != -1:
                used.add(color[idx])
        for idx in adj[v]:
            if color[idx] != -1:
                used.add(color[idx])
        return [c for c in (1,2,3) if c not in used]
    
    # Sort edges by degree of constraint (number of adjacent edges)
    order = sorted(range(m), key=lambda e: len(adj[edges[e][0]]) + len(adj[edges[e][1]]), reverse=True)
    
    def backtrack(pos):
        if pos == m:
            return True
        e = order[pos]
        if color[e] != -1:
            return backtrack(pos+1)
        for c in available_colors(e):
            color[e] = c
            if backtrack(pos+1):
                return True
            color[e] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()