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

    # s[i] will store the vault assigned to substance i
    s = [0] * (n + 1)

    def is_valid(node, color):
        """Check if assigning 'color' to 'node' is valid given neighbors."""
        for neighbor in adj[node]:
            if s[neighbor] == color:
                return False
        return True

    def backtrack(node):
        """
        Try assigning vaults 1, 2, 3 in order to find the 
        lexicographically smallest sequence.
        """
        if node > n:
            return True
        
        # Try vault 1, then 2, then 3 for lexicographical order
        for color in range(1, 4):
            if is_valid(node, color):
                s[node] = color
                if backtrack(node + 1):
                    return True
                s[node] = 0
        
        return False

    # We need to find the lexicographically smallest assignment.
    # Standard backtracking from 1 to n trying colors 1, 2, 3
    # will find the lexicographically smallest sequence.
    if backtrack(1):
        print("YES")
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()