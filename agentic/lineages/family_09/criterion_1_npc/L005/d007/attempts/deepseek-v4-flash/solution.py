import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Backtracking to find independent set of size k
    selected = []
    
    def backtrack(start, count):
        if count == k:
            return True
        if start >= n:
            return False
        # Prune: not enough remaining vertices
        if n - start < k - count:
            return False
        
        # Try to include start if possible
        can_include = True
        for v in selected:
            if (adj[start] >> v) & 1:
                can_include = False
                break
        if can_include:
            selected.append(start)
            if backtrack(start + 1, count + 1):
                return True
            selected.pop()
        
        # Skip start
        if backtrack(start + 1, count):
            return True
        return False
    
    if backtrack(0, 0):
        print("YES")
        print(" ".join(str(x + 1) for x in selected))
    else:
        print("NO")

if __name__ == "__main__":
    solve()