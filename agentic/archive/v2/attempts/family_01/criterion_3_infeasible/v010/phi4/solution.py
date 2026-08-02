import sys

def find_smallest_conflict_triple(n, m, conflicts):
    # Create adjacency list for conflicts
    adj = {i: set() for i in range(1, n + 1)}
    for u, v in conflicts:
        adj[u].add(v)
        adj[v].add(u)

    # Check all triples (a, b, c) where a < b < c
    for a in range(1, n + 1):
        for b in adj[a]:
            if b > a:
                for c in adj[b]:
                    if c > b and c in adj[a]:
                        return a, b, c

# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
conflicts = []
index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    conflicts.append((u, v))
    index += 2

# Find and print the smallest conflict triple
result = find_smallest_conflict_triple(n, m, conflicts)
print(" ".join(map(str, result)))