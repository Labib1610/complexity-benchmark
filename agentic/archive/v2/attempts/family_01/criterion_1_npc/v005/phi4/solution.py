def shift_assignment(n, m, incompatibilities):
    from itertools import permutations

    # Create a list of workers and their incompatible pairs
    adj = [[] for _ in range(n)]
    for u, v in incompatibilities:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # Function to check if the assignment is valid
    def is_valid(assignment):
        for i in range(n):
            slot = assignment[i]
            for j in adj[i]:
                if assignment[j] == slot:
                    return False
        return True

    # Try all permutations of [1, 2, 3] repeated enough times to cover n slots
    slots = [1, 2, 3]
    min_assignment = None

    for perm in permutations(slots * (n // 3 + 1), n):
        if is_valid(perm):
            if min_assignment is None or perm < min_assignment:
                min_assignment = perm

    if min_assignment is not None:
        return "YES\n" + ' '.join(map(str, min_assignment))
    else:
        return "NO"

# Reading input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
incompatibilities = []
index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    incompatibilities.append((u, v))
    index += 2

# Get the result and print it
result = shift_assignment(n, m, incompatibilities)
print(result)