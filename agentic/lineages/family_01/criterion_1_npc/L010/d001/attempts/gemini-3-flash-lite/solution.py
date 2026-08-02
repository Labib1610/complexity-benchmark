import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    def backtrack(task_idx):
        if task_idx > n:
            return True
        
        # Try tiers 1, 2, 3 in order for lexicographical smallest
        for tier in range(1, 4):
            can_assign = True
            for neighbor in adj[task_idx]:
                if assignment[neighbor] == tier:
                    can_assign = False
                    break
            
            if can_assign:
                assignment[task_idx] = tier
                if backtrack(task_idx + 1):
                    return True
                assignment[task_idx] = 0
        
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()