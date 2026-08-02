def assign_vaults():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    from itertools import combinations
    
    # Read incompatible pairs
    incompatibilities = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        incompatibilities.append((u, v))
        index += 2

    artifacts = list(range(1, n + 1))

    # Generate all possible assignments (1, 2, 3) to n artifacts
    def generate_assignments(n):
        if n == 0:
            yield []
        else:
            for assignment in generate_assignments(n - 1):
                for vault in range(1, 4):
                    yield assignment + [vault]

    # Check if an assignment is valid
    def is_valid_assignment(assignment):
        artifact_to_vault = {artifact: vault for artifact, vault in zip(artifacts, assignment)}
        for u, v in incompatibilities:
            if artifact_to_vault[u] == artifact_to_vault[v]:
                return False
        return True

    # Find the lexicographically smallest valid assignment
    best_assignment = None
    for assignment in generate_assignments(n):
        if is_valid_assignment(assignment):
            if best_assignment is None or assignment < best_assignment:
                best_assignment = assignment
    
    if best_assignment is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, best_assignment)))

# Call the function to execute
assign_vaults()