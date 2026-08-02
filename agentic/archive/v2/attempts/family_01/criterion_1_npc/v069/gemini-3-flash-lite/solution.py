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
    
    def backtrack(person):
        if person == n:
            return True
        
        # Try windows 1, 2, 3 in order to ensure lexicographical smallest
        for window in range(1, 4):
            can_assign = True
            for prev in range(person):
                if (adj[person + 1] & (1 << prev)):
                    if assignment[prev] == window:
                        can_assign = False
                        break
            
            if can_assign:
                assignment[person] = window
                if backtrack(person + 1):
                    return True
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()