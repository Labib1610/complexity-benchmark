def solve():
    import sys
    data = sys.stdin.read().split()
    
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    assignment = [-1] * n
    valid_stages = [7] * n  # 0b111 = all stages valid
    
    def backtrack(task):
        if task == n:
            return True
        
        for stage in [1, 2, 3]:
            bit = 1 << (stage - 1)
            if not (valid_stages[task] & bit):
                continue
            
            valid = True
            for neighbor in adj[task]:
                if assignment[neighbor] == stage:
                    valid = False
                    break
            
            if not valid:
                continue
            
            assignment[task] = stage
            
            removed = []
            for neighbor in adj[task]:
                if assignment[neighbor] == -1 and (valid_stages[neighbor] & bit):
                    valid_stages[neighbor] &= ~bit
                    removed.append(neighbor)
            
            conflict = False
            for i in range(task + 1, n):
                if assignment[i] == -1 and valid_stages[i] == 0:
                    conflict = True
                    break
            
            if not conflict and backtrack(task + 1):
                return True
            
            assignment[task] = -1
            for neighbor in removed:
                valid_stages[neighbor] |= bit
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()