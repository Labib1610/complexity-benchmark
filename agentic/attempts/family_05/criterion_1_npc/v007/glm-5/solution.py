import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Read all allowed combinations
    triples = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        triples.append((x, y, z))
    
    # Build adjacency: for each x, list of (y, z) pairs
    adj = [[] for _ in range(k + 1)]
    for x, y, z in triples:
        adj[x].append((y, z))
    
    # match_y[y] = x that is matched to y, match_z[z] = x that is matched to z
    match_y = [0] * (k + 1)
    match_z = [0] * (k + 1)
    
    def dfs(x, visited_y, visited_z):
        for y, z in adj[x]:
            if visited_y[y] or visited_z[z]:
                continue
            visited_y[y] = True
            visited_z[z] = True
            my = match_y[y]
            mz = match_z[z]
            if my == 0 and mz == 0:
                match_y[y] = x
                match_z[z] = x
                return True
            # Both my and mz should be same x (invariant)
            if my != 0 and dfs(my, visited_y, visited_z):
                match_y[y] = x
                match_z[z] = x
                return True
        return False
    
    for x in range(1, k + 1):
        visited_y = [False] * (k + 1)
        visited_z = [False] * (k + 1)
        if not dfs(x, visited_y, visited_z):
            print("NO")
            return
    
    # Build result
    result = [None] * (k + 1)
    for y in range(1, k + 1):
        x = match_y[y]
        # Find z such that match_z[z] == x
        for z in range(1, k + 1):
            if match_z[z] == x:
                result[x] = (x, y, z)
                break
    
    print("YES")
    for x in range(1, k + 1):
        r = result[x]
        print(f"{r[0]} {r[1]} {r[2]}")

if __name__ == "__main__":
    solve()