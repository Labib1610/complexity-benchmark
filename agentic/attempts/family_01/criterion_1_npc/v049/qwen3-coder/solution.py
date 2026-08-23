def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Create adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Try all possible assignments in lexicographical order
    # We can use backtracking with pruning
    assignment = [0] * (n + 1)  # assignment[i] = block of employee i
    
    def is_valid(employee, block):
        # Check if assigning 'block' to 'employee' conflicts with neighbors
        for neighbor in adj[employee]:
            if assignment[neighbor] == block:
                return False
        return True
    
    def backtrack(employee):
        if employee > n:
            return True
            
        for block in range(1, 4):
            if is_valid(employee, block):
                assignment[employee] = block
                if backtrack(employee + 1):
                    return True
                assignment[employee] = 0  # Backtrack
        return False
    
    # Start backtracking from employee 1
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

solve()