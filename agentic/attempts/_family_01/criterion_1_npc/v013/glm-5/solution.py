import sys
sys.setrecursionlimit(1000000)

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
    
    assignment = [0] * n
    
    def dfs(u):
        for v in adj[u]:
            if assignment[v] == 0:
                # Try to assign v a color different from u
                for c in range(1, 4):
                    if c != assignment[u]:
                        assignment[v] = c
                        if dfs(v):
                            break
                        assignment[v] = 0
                else:
                    return False
            elif assignment[v] == assignment[u]:
                return False
        return True
    
    for i in range(n):
        if assignment[i] == 0:
            assignment[i] = 1
            if not dfs(i):
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()