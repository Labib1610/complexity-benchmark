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
    
    # We want lexicographically smallest, so try assigning 1, then 2, then 3
    # Use backtracking with pruning
    def backtrack(worker_idx):
        if worker_idx == n:
            return True
        
        # Current worker is worker_idx + 1
        # Check which slots are available
        forbidden_slots = 0
        for prev_worker in range(worker_idx):
            if (adj[worker_idx + 1] >> prev_worker) & 1:
                forbidden_slots |= (1 << (assignment[prev_worker] - 1))
        
        for slot in range(1, 4):
            if not ((forbidden_slots >> (slot - 1)) & 1):
                assignment[worker_idx] = slot
                if backtrack(worker_idx + 1):
                    return True
                assignment[worker_idx] = 0
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()