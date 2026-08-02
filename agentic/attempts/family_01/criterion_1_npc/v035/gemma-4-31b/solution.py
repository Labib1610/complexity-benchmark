import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # We need the lexicographically smallest sequence of shifts (1, 2, 3).
    # Since n is small (up to 40), we can use backtracking with pruning.
    # The state is (current_worker, current_assignments).
    
    assignment = [0] * n
    
    def can_assign(worker, shift):
        for neighbor in adj[worker]:
            if assignment[neighbor] == shift:
                return False
        return True

    def backtrack(worker):
        if worker == n:
            return True
        
        # Try shifts in order 1, 2, 3 to ensure lexicographical smallest result
        for shift in [1, 2, 3]:
            if can_assign(worker, shift):
                assignment[worker] = shift
                if backtrack(worker + 1):
                    return True
                assignment[worker] = 0
        
        return False

    # To optimize for n=40, we can use a simple check: 
    # The 3-coloring problem is NP-complete, but with n=40 and 
    # specific constraints, a basic backtracking might be slow.
    # However, we need the lexicographically smallest, so we must try 1, 2, 3 in order.
    # Let's implement a slightly more robust backtracking.
    
    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == "__main__":
    # Increase recursion depth for deep backtracking trees
    sys.setrecursionlimit(2000)
    solve()