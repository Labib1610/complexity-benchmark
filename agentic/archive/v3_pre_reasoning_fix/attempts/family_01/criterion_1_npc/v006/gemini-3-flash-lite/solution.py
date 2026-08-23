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
    
    def backtrack(curr):
        if curr == n:
            return True
        
        # Try assigning 1, 2, then 3 for lexicographical smallest
        for color in [1, 2, 3]:
            can_assign = True
            for neighbor in adj[curr]:
                if neighbor < curr and assignment[neighbor] == color:
                    can_assign = False
                    break
            
            if can_assign:
                assignment[curr] = color
                if backtrack(curr + 1):
                    return True
                assignment[curr] = 0
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()