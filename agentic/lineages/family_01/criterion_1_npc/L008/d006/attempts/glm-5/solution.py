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
    
    # Forbidden pairs: (s_u, s_v) such that 2^s_u + 2^s_v is a power of 2
    # Powers of 2: 2, 4, 8, 16, 32
    # 2^1 + 2^1 = 4 = 2^2 -> forbidden (1,1)
    # 2^2 + 2^2 = 8 = 2^3 -> forbidden (2,2)
    # 2^3 + 2^3 = 16 = 2^4 -> forbidden (3,3)
    # 2^1 + 2^2 = 6 not power of 2
    # 2^1 + 2^3 = 10 not power of 2
    # 2^2 + 2^3 = 12 not power of 2
    # So forbidden pairs are (1,1), (2,2), (3,3)
    
    # We need to assign values from {1,2,3} such that no edge has both endpoints with same value
    # This is equivalent to 3-coloring the graph
    
    # Try all 3^n assignments, n <= 40
    # But we can prune using backtracking
    
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        for val in [1, 2, 3]:
            valid = True
            for neighbor in adj[idx]:
                if neighbor < idx and assignment[neighbor] == val:
                    valid = False
                    break
            if valid:
                assignment[idx] = val
                if backtrack(idx + 1):
                    return True
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()