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
        v = int(input_data[idx + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * n
    
    def is_valid(person, window):
        for neighbor in adj[person]:
            if assignment[neighbor] == window:
                return False
        return True
    
    def backtrack(person):
        if person == n:
            return True
        
        for window in [1, 2, 3]:
            if is_valid(person, window):
                assignment[person] = window
                if backtrack(person + 1):
                    return True
                assignment[person] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()