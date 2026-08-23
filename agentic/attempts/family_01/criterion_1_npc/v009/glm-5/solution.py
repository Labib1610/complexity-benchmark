import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We use backtracking with pruning.
    # assignment[i] stores the shift (1, 2, or 3) for worker i.
    # 0 means unassigned.
    assignment = [0] * n
    
    def backtrack(worker_idx):
        # Base case: all workers have been assigned a shift.
        if worker_idx == n:
            return True

        # Try shifts in increasing order to ensure lexicographically smallest result.
        for shift in range(1, 4):
            # Check if this shift is valid for the current worker.
            # A shift is invalid if any neighbor already has the same shift.
            is_valid = True
            for neighbor in adj[worker_idx]:
                if assignment[neighbor] == shift:
                    is_valid = False
                    break
            
            if is_valid:
                assignment[worker_idx] = shift
                if backtrack(worker_idx + 1):
                    return True
                # Backtrack: unassign the worker to try other shifts.
                assignment[worker_idx] = 0
        
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()