import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
        idx += 2
        
    assignment = [0] * n
    
    # We need the lexicographically smallest sequence of (s1, s2, ..., sn).
    # This means we try to assign 1 to worker 1, if possible, then 1 to worker 2, etc.
    # Since n is small (up to 40), we use backtracking.
    
    def backtrack(worker_idx):
        if worker_idx == n:
            return True
        
        # Try slots 1, 2, 3 in order
        for slot in [1, 2, 3]:
            # Check if any previously assigned worker in this slot conflicts
            possible = True
            for prev in range(worker_idx):
                if assignment[prev] == slot:
                    if (adj[worker_idx + 1] & (1 << prev)):
                        possible = False
                        break
            
            if possible:
                assignment[worker_idx] = slot
                if backtrack(worker_idx + 1):
                    return True
        
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()