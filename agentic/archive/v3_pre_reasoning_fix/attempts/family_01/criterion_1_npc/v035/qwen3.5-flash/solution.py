import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    if idx >= len(input_data):
        return
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2
    
    # Build adjacency list for incompatible pairs
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    # Assignment array (1-indexed, 0 means unassigned)
    assignment = [0] * (n + 1)
    
    def is_valid(worker, shift):
        """Check if assigning worker to shift is valid"""
        for neighbor in adj[worker]:
            if assignment[neighbor] == shift:
                return False
        return True
    
    def dfs(worker):
        """Try to assign shifts starting from worker"""
        if worker > n:
            return True
        
        # Try shifts 1, 2, 3 in order for lexicographically smallest
        for shift in range(1, 4):
            if is_valid(worker, shift):
                assignment[worker] = shift
                if dfs(worker + 1):
                    return True
                assignment[worker] = 0  # Backtrack
        
        return False
    
    if dfs(1):
        print("YES")
        print(" ".join(map(str, assignment[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()