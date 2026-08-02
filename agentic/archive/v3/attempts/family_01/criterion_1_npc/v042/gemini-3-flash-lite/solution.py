import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    def is_safe(u, vault):
        for v in adj[u]:
            if assignment[v] == vault:
                return False
        return True
    
    def backtrack(u):
        if u > n:
            return True
        
        for vault in range(1, 4):
            if is_safe(u, vault):
                assignment[u] = vault
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False
    
    # Since n is small (up to 40), we can use backtracking with pruning.
    # The lexicographical requirement is naturally handled by trying 1, 2, 3 in order.
    # However, standard backtracking might be slow. Given n=40 and 3-coloring,
    # this is technically NP-hard, but typically fast for this constraint size.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    # Increase recursion depth for deep backtracking trees
    sys.setrecursionlimit(2000)
    solve()