import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        
    assignment = [0] * n
    
    def backtrack(person):
        if person == n:
            return True
        
        # Try slots 1, 2, 3 in order for lexicographical requirement
        for slot in [1, 2, 3]:
            can_assign = True
            for prev in range(person):
                if (adj[person] & (1 << prev)):
                    if assignment[prev] == slot:
                        can_assign = False
                        break
            
            if can_assign:
                assignment[person] = slot
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