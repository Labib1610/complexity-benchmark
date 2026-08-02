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
    
    def is_safe(worker, shift):
        for neighbor in adj[worker]:
            if assignment[neighbor] == shift:
                return False
        return True
    
    def backtrack(worker):
        if worker > n:
            return True
        
        for shift in [1, 2, 3]:
            if is_safe(worker, shift):
                assignment[worker] = shift
                if backtrack(worker + 1):
                    return True
                assignment[worker] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()