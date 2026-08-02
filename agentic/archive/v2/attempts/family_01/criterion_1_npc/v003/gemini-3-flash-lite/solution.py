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
    
    def backtrack(person):
        if person == n:
            return True
        
        # Try slots 1, 2, 3 in order to ensure lexicographical smallest
        for slot in range(1, 4):
            can_assign = True
            for neighbor in adj[person]:
                if neighbor < person and assignment[neighbor] == slot:
                    can_assign = False
                    break
            
            if can_assign:
                assignment[person] = slot
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