import sys

def find_mutually_conflicting_group(n, m, conflicts):
    # Create a set for each staff member containing their conflicting partners
    conflict_sets = [set() for _ in range(n + 1)]
    
    for u, v in conflicts:
        conflict_sets[u].add(v)
        conflict_sets[v].add(u)
    
    # Find the lexicographically smallest triple (a, b, c) such that all pairs are conflicting
    for a in range(1, n + 1):
        for b in conflict_sets[a]:
            if b > a:
                for c in conflict_sets[b]:
                    if c > b and a in conflict_sets[c]:
                        return a, b, c

# Read input
input_data = sys.stdin.read().split()
index = 0
n = int(input_data[index])
index += 1
m = int(input_data[index])
index += 1

conflicts = []
for _ in range(m):
    u = int(input_data[index])
    index += 1
    v = int(input_data[index])
    index += 1
    conflicts.append((u, v))

# Find and print the result
a, b, c = find_mutually_conflicting_group(n, m, conflicts)
print(a, b, c)