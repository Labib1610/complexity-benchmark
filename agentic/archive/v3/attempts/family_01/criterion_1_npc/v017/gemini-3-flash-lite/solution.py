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
        v = int(input_data[idx+1])
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
        idx += 2
        
    assignment = [0] * n
    
    def is_safe(u, shift):
        for i in range(u):
            if (adj[u + 1] & (1 << i)) and assignment[i] == shift:
                return False
        return True

    def backtrack(u):
        if u == n:
            return True
        
        for shift in [1, 2, 3]:
            if is_safe(u, shift):
                assignment[u] = shift
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()