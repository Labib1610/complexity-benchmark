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
    # We'll use backtracking with pruning
    chosen = []
    
    def backtrack(start, chosen_mask, chosen_list):
        if len(chosen_list) == k:
            return True
        # Prune: not enough remaining vertices
        if n - start < k - len(chosen_list):
            return False
        for v in range(start, n):
            # Check if v is compatible with chosen set
            if (adj[v] & chosen_mask) == 0:
                chosen_list.append(v)
                if backtrack(v + 1, chosen_mask | (1 << v), chosen_list):
                    return True
                chosen_list.pop()
        return False
    
    if backtrack(0, 0, chosen):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()