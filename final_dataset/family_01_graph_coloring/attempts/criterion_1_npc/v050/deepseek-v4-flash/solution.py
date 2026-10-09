import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    
    # Check if we can color the graph with 3 colors using backtracking
    def backtrack(idx):
        if idx == n:
            return True
        # Choose the uncolored vertex with the most colored neighbors
        best = -1
        best_degree = -1
        for v in range(n):
            if color[v] == -1:
                deg = sum(1 for nb in adj[v] if color[nb] != -1)
                if deg > best_degree:
                    best_degree = deg
                    best = v
        v = best
        # Try colors 1,2,3
        used = {color[nb] for nb in adj[v] if color[nb] != -1}
        for c in (1, 2, 3):
            if c not in used:
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()