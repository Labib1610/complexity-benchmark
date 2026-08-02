import sys

def solve():
    # Increase recursion depth for deep backtracking
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # colors[i] stores the assignment for operator i (1, 2, or 3)
    # 0 means unassigned
    colors = [0] * (n + 1)

    def is_valid(u, color):
        for v in adj[u]:
            if colors[v] == color:
                return False
        return True

    # We need the lexicographically smallest sequence.
    # This means for each operator from 1 to n, we try assigning 1, then 2, then 3.
    # Because n is small (up to 40), backtracking with pruning should work.
    
    def backtrack(u):
        if u > n:
            return True
        
        # Try colors in increasing order to ensure lexicographical smallest result
        for c in [1, 2, 3]:
            if is_valid(u, c):
                colors[u] = c
                if backtrack(u + 1):
                    return True
                colors[u] = 0
        return False

    # To optimize, we can use a simple heuristic: 
    # Since we need the lexicographically smallest, we must try 1, 2, 3 for u=1, then u=2...
    # However, 3-coloring is NP-complete. With N=40, pure backtracking might be slow.
    # But the lexicographical requirement forces the order of assignment.
    
    # Let's implement a slightly more robust backtracking.
    # Since we must decide s_1, then s_2, etc., the order of nodes is fixed.
    
    if backtrack(1):
        print("YES")
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()