import sys

def find_committee(n, m, relations):
    # Create a set of tuples for fast membership checking
    edge_set = set()
    for u, v in relations:
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
    
    # Iterate over all possible triples (a, b, c)
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (a, b) not in edge_set:
                continue
            for c in range(b + 1, n + 1):
                if (b, c) in edge_set and (a, c) in edge_set:
                    return a, b, c

# Read input from standard input
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

relations = []
index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    relations.append((u, v))
    index += 2

# Find the committee and print it
result = find_committee(n, m, relations)
print(*result)