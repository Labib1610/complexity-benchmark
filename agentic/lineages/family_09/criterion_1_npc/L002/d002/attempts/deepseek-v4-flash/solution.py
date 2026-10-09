import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Try to find an independent set of size k
    # Use backtracking with pruning
    # We'll store the chosen set as a bitmask
    chosen = []
    
    def backtrack(start, count, mask):
        if count == k:
            return True
        if start >= n:
            return False
        # Prune: if even taking all remaining vertices can't reach k
        if count + (n - start) < k:
            return False
        
        # Try to include start if possible
        if (mask & adj[start]) == 0:
            chosen.append(start)
            if backtrack(start + 1, count + 1, mask | (1 << start)):
                return True
            chosen.pop()
        
        # Try to exclude start
        if backtrack(start + 1, count, mask):
            return True
        
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()