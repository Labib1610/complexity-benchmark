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
    
    assignment = [-1] * n
    
    def is_safe(pillar, grade):
        for neighbor in adj[pillar]:
            if assignment[neighbor] == grade:
                return False
        return True
    
    def dfs(idx):
        if idx == n:
            return True
        
        for grade in [1, 2, 3]:
            if is_safe(idx, grade):
                assignment[idx] = grade
                if dfs(idx + 1):
                    return True
                assignment[idx] = -1
        
        return False
    
    if dfs(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()