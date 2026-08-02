import sys

def solve():
    # Increase recursion depth for safety, although n=40 is small
    sys.setrecursionlimit(2000)
    
    # Read input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # Assignment array: 0 means unassigned
    assignment = [0] * (n + 1)
    
    def is_valid(node, color):
        # Check if any neighbor already has the same color
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True

    def backtrack(node):
        # Base case: all workers assigned
        if node > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order for lexicographical smallest result
        for color in range(1, 4):
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()