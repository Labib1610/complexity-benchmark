def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    def is_valid(assignment):
        for i in range(n):
            for j in range(i + 1, n):
                if assignment[i] == assignment[j] and (i + 1) in adj[j + 1]:
                    return False
        return True
    
    def find_assignment(index, assignment):
        if index == n:
            if is_valid(assignment):
                return assignment
            else:
                return None
        
        for slot in [1, 2, 3]:
            new_assignment = assignment + [slot]
            result = find_assignment(index + 1, new_assignment)
            if result:
                return result
        
        return None
    
    assignment = find_assignment(0, [])
    
    if assignment:
        print("YES")
        print(*assignment)
    else:
        print("NO")

solve()