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
    
    # Try to find an independent set of size k
    chosen = []
    
    def backtrack(start, chosen_mask, chosen_list):
        if len(chosen_list) == k:
            return True
        if start >= n:
            return False
        # Prune: not enough remaining vertices
        if n - start < k - len(chosen_list):
            return False
        
        # Try to include vertex start
        if (chosen_mask & adj[start]) == 0:
            chosen_list.append(start)
            if backtrack(start + 1, chosen_mask | (1 << start), chosen_list):
                return True
            chosen_list.pop()
        
        # Try to exclude vertex start
        if backtrack(start + 1, chosen_mask, chosen_list):
            return True
        
        return False
    
    if backtrack(0, 0, chosen):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()