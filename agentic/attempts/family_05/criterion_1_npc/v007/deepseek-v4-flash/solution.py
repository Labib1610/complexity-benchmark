import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # adjacency: x -> list of (y,z)
    adj = [[] for _ in range(k+1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        adj[x].append((y, z))
    
    # We'll do DFS-based bipartite matching
    # Right side: (y,z) pairs, we map them to indices 0..k*k-1
    # But we only need to match k edges, so we can use dict for matchR
    
    matchR = {}  # (y,z) -> x
    # We'll try to match each x
    
    def dfs(x, visited):
        for (y, z) in adj[x]:
            if (y, z) in visited:
                continue
            visited.add((y, z))
            if (y, z) not in matchR or dfs(matchR[(y, z)], visited):
                matchR[(y, z)] = x
                return True
        return False
    
    for x in range(1, k+1):
        visited = set()
        if not dfs(x, visited):
            print("NO")
            return
    
    # If we matched all k specialists, we have a solution
    # But we must ensure each y and z appears exactly once.
    # Since each (y,z) is unique in matchR, and we have k matches,
    # we need to check that y's and z's are all distinct.
    used_y = [False]*(k+1)
    used_z = [False]*(k+1)
    for (y, z), x in matchR.items():
        if used_y[y] or used_z[z]:
            print("NO")
            return
        used_y[y] = True
        used_z[z] = True
    
    # If all used, we have a valid perfect matching
    print("YES")
    for (y, z), x in matchR.items():
        print(x, y, z)

if __name__ == "__main__":
    solve()