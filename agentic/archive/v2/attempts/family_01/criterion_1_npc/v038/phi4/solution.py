from itertools import combinations

def find_schedule(n, m, constraints):
    # Create adjacency list for each person
    adj_list = {i: [] for i in range(1, n+1)}
    for u, v in constraints:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def is_valid_assignment(personnel, assignment):
        for p in personnel:
            if assignment[p-1] == 0:
                continue
            for incompatible in adj_list[p]:
                if assignment[incompatible-1] == assignment[p-1]:
                    return False
        return True

    def dfs(personnel, index, assignment):
        if index == n:
            return True
        
        # Try assigning blocks 1 to 3 and choose the smallest lexicographically valid one
        for block in range(1, 4):
            assignment[index] = block
            if is_valid_assignment(personnel[:index+1], assignment):
                if dfs(personnel, index + 1, assignment):
                    return True
        
        # Reset assignment and backtrack
        assignment[index] = 0
        return False

    personnel = list(range(1, n+1))
    assignment = [0] * n

    if dfs(personnel, 0, assignment):
        print("YES")
        print(*assignment)
    else:
        print("NO")

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    constraints = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        constraints.append((u, v))
        index += 2

    find_schedule(n, m, constraints)