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
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        idx += 2
        
    assignment = [0] * n
    
    def backtrack(person):
        if person == n:
            return True
        
        # Try shifts 1, 2, 3 in order for lexicographical smallest
        for shift in range(1, 4):
            can_assign = True
            for other in range(person):
                if (adj[person] & (1 << other)) and assignment[other] == shift:
                    can_assign = False
                    break
            
            if can_assign:
                assignment[person] = shift
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