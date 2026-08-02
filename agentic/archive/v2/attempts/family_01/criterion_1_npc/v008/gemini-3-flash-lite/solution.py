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
        
    shifts = [0] * (n + 1)
    
    def backtrack(u):
        if u > n:
            return True
        
        # Try shifts 1, 2, 3 in order to get lexicographically smallest result
        for s in range(1, 4):
            possible = True
            for neighbor in adj[u]:
                if shifts[neighbor] == s:
                    possible = False
                    break
            
            if possible:
                shifts[u] = s
                if backtrack(u + 1):
                    return True
                shifts[u] = 0
        
        return False

    if backtrack(1):
        print("YES")
        print(*(shifts[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()