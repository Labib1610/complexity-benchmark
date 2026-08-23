import sys

def solve():
    # Increase recursion depth for deep DFS
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
    
    # We want the lexicographically smallest sequence s_1, s_2, ..., s_n.
    # This means we should try to assign 1 to s_1, then 1 to s_2, etc.
    # Since n is small (up to 40), we can use backtracking with pruning.
    
    assignment = [0] * (n + 1)
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True

    def backtrack(node):
        if node > n:
            return True
        
        # Try colors in increasing order to ensure lexicographical smallest result
        for color in (1, 2, 3):
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False

    # The problem is essentially 3-coloring a graph.
    # 3-coloring is NP-complete, but n=40 might pass with simple backtracking 
    # if the constraints are not specifically designed to break it, 
    # or if we use a more efficient approach.
    # However, the lexicographical requirement forces a specific search order.
    
    # To optimize, we can check if the remaining graph is 3-colorable, 
    # but that's also NP-complete. Simple backtracking with the 1,2,3 order is the way.
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()