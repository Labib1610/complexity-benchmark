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
    
    # Profiles: index 0, 1, 2 correspond to Profile IDs 1, 2, 3
    # Profile 1: (1, 2, 3)
    # Profile 2: (2, 3, 1)
    # Profile 3: (3, 1, 2)
    profiles = [(1, 2, 3), (2, 3, 1), (3, 1, 2)]
    
    # Precompute compatibility: compatible[p1][p2] is True if p1 and p2 can be assigned to adjacent tasks
    compatible = [[False] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            ok = True
            for k in range(3):
                if profiles[i][k] == profiles[j][k]:
                    ok = False
                    break
            compatible[i][j] = ok
    
    assignment = [-1] * n
    
    def dfs(u):
        for p in range(3):
            valid = True
            for v in adj[u]:
                if assignment[v] != -1:
                    if not compatible[p][assignment[v]]:
                        valid = False
                        break
            if valid:
                assignment[u] = p
                all_assigned = True
                for v in range(n):
                    if assignment[v] == -1:
                        all_assigned = False
                        if not dfs(v):
                            break
                else:
                    return True
                assignment[u] = -1
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(str(x + 1) for x in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()