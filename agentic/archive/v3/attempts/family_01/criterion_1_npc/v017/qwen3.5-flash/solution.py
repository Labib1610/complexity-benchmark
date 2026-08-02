import sys

# Increase recursion depth to accommodate deep recursion trees if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for forward checking
    # We only store neighbors v > u for each u.
    # This is because we assign nodes in order 1 to n.
    # When assigning node u, we only need to update constraints for nodes v > u.
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            adj[u].append(v)
        else:
            adj[v].append(u)
            
    # assignment[i] stores the shift for employee i (1-based)
    assignment = [0] * (n + 1)
    
    # counts[v][c] stores the number of assigned neighbors of v with shift c
    # c is 1, 2, 3. We use indices 1, 2, 3.
    counts = [[0] * 4 for _ in range(n + 1)]
    
    def backtrack(idx):
        if idx > n:
            return True
        
        # Try shifts 1, 2, 3 to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if shift c is valid for current employee idx
            # It is valid if no assigned neighbor has shift c.
            # Since we process in order, counts[idx][c] reflects constraints from neighbors < idx.
            if counts[idx][c] > 0:
                continue
            
            assignment[idx] = c
            
            conflict = False
            updated = []
            
            # Update counts for neighbors > idx (forward checking)
            for v in adj[idx]:
                counts[v][c] += 1
                # If a neighbor v has neighbors with shifts 1, 2, and 3 assigned, it cannot be colored.
                if counts[v][1] > 0 and counts[v][2] > 0 and counts[v][3] > 0:
                    conflict = True
                    updated.append(v)
                    break
            
            if conflict:
                # Revert changes
                for v in updated:
                    counts[v][c] -= 1
                assignment[idx] = 0
                continue
            
            # Recurse
            if backtrack(idx + 1):
                return True
            
            # Backtrack: revert changes
            for v in adj[idx]:
                counts[v][c] -= 1
            assignment[idx] = 0
            
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()