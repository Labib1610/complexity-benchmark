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
    
    assignment = [0] * n
    
    def is_valid(v, val):
        for neighbor in adj[v]:
            if assignment[neighbor] == val:
                return False
        return True
    
    def backtrack(idx):
        if idx == n:
            return True
        for val in range(1, 4):
            if is_valid(idx, val):
                assignment[idx] = val
                if backtrack(idx + 1):
                    return True
                assignment[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()