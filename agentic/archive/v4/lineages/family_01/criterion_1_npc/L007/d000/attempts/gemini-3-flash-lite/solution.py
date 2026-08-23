import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * n
    
    def is_valid(node, channel):
        for neighbor in adj[node]:
            if assignment[neighbor] == channel:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for channel in range(1, 4):
            if is_valid(node, channel):
                assignment[node] = channel
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()