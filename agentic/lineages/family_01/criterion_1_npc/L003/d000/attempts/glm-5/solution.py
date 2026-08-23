import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # We want the lexicographically smallest assignment.
    # Since n <= 40, we can use backtracking with pruning.
    # We assign employees 0 to n-1 in order, trying schedules 1, 2, 3.
    
    assignment = [0] * n
    
    def backtrack(idx):
        if idx == n:
            return True
        
        for color in range(1, 4):
            valid = True
            for neighbor in adj[idx]:
                if neighbor < idx and assignment[neighbor] == color:
                    valid = False
                    break
            
            if valid:
                assignment[idx] = color
                if backtrack(idx + 1):
                    return True
                # assignment[idx] = 0 # Not strictly necessary to reset
        
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()