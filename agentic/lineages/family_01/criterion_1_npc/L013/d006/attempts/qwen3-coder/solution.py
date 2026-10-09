def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def read_input():
    n, m = map(int, input().split())
    constraints = []
    for _ in range(m):
        u, v = map(int, input().split())
        constraints.append((u, v))
    return n, m, constraints

def is_invertible(u, v, eu, ev):
    det = u * ev - v * eu
    return det != 0

def solve(n, m, constraints):
    # Try all possible assignments of excitation states (1, 2, 3)
    # Since each variable can take 3 values, we have 3^n possibilities
    # For n <= 40, this is too large, but we can use backtracking with pruning
    
    # However, let's think differently. This is essentially a graph coloring problem
    # where each edge (u,v) imposes a constraint on the values of eu and ev
    
    # Let's model this as a CSP and use backtracking
    
    # We'll use backtracking with constraint propagation
    
    # First, let's build a graph
    adj = [[] for _ in range(n+1)]
    for u, v in constraints:
        adj[u].append(v)
        adj[v].append(u)
    
    # excitation states
    excitation = [0] * (n+1)  # excitation[i] will hold the state for emitter i
    
    def is_consistent_with_neighbors(var):
        # Check if assigning a value to var is consistent with all its neighbors
        for neighbor in adj[var]:
            if excitation[neighbor] != 0:  # if neighbor already assigned
                if not is_invertible(var, neighbor, excitation[var], excitation[neighbor]):
                    return False
        return True
    
    def backtrack(var):
        if var > n:
            return True  # All variables assigned successfully
        
        for state in [1, 2, 3]:
            excitation[var] = state
            if is_consistent_with_neighbors(var):
                if backtrack(var + 1):
                    return True
            excitation[var] = 0
            
        return False
    
    # Start backtracking from variable 1
    if backtrack(1):
        return "YES\n" + " ".join(map(str, excitation[1:]))
    else:
        return "NO"

def main():
    n, m, constraints = read_input()
    result = solve(n, m, constraints)
    print(result)

if __name__ == "__main__":
    main()