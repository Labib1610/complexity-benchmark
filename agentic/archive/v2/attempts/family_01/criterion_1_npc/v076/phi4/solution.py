from itertools import product

def find_channel_assignment(n, m, constraints):
    # Create adjacency list for conflicts
    adj_list = {i: set() for i in range(1, n + 1)}
    for u, v in constraints:
        adj_list[u].add(v)
        adj_list[v].add(u)

    # Generate all possible channel assignments
    channels = [1, 2, 3]
    min_assignment = None

    for assignment in product(channels, repeat=n):
        valid = True
        
        for i in range(n):
            current_unit = i + 1
            assigned_channel = assignment[i]
            
            # Check conflicts with adjacent units
            for neighbor in adj_list[current_unit]:
                if assignment[neighbor - 1] == assigned_channel:
                    valid = False
                    break
            
            if not valid:
                break
        
        # If a valid assignment is found, check if it's lexicographically smallest
        if valid:
            if min_assignment is None or assignment < min_assignment:
                min_assignment = assignment

    return min_assignment


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    constraints = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        constraints.append((u, v))
        index += 2
    
    result = find_channel_assignment(n, m, constraints)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))