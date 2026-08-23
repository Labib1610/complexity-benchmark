import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Greedy assignment with backtracking
    # We try to assign the smallest valid color (1, 2, or 3) to each vertex
    # If we get stuck, we backtrack
    
    color = [0] * n
    
    def get_available_colors(u):
        used = set()
        for v in adj[u]:
            if color[v] != 0:
                used.add(color[v])
        available = []
        for c in range(1, 4):
            if c not in used:
                available.append(c)
        return available
    
    def backtrack(u):
        if u == n:
            return True
        available = get_available_colors(u)
        for c in available:
            color[u] = c
            if backtrack(u + 1):
                return True
            color[u] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()