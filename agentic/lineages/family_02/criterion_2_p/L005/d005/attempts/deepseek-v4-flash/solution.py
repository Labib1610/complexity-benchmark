import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(2 * n + 2))
rank = [0] * (2 * n + 2)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1

# For each qubit i, we have two nodes:
# i*2   -> x_i = 0
# i*2+1 -> x_i = 1

for _ in range(m):
    l1, l2 = map(int, input().split())
    a = abs(l1)
    b = abs(l2)
    # Determine required value for each
    val_a = 0 if l1 > 0 else 1
    val_b = 0 if l2 > 0 else 1
    # Force x_a = val_a, x_b = val_b
    # x_a = val_a means node (a*2 + val_a) is true
    # So union the opposite of x_a with x_a's opposite? Actually we force it:
    # We can force by unioning the "true" node with a special always-true node.
    # Use node 0 as always-true? Better: use 2n as true, 2n+1 as false.
    # Force x_a = val_a: union(a*2 + val_a, 2n)  # true node
    # Force x_b = val_b: union(b*2 + val_b, 2n)
    union(a * 2 + val_a, 2 * n)
    union(b * 2 + val_b, 2 * n)

# Check consistency: for each i, 0-node and 1-node must not be in same set
true_node = 2 * n
for i in range(1, n + 1):
    if find(i * 2) == find(i * 2 + 1):
        print("NO")
        sys.exit()

# Assign values
res = []
for i in range(1, n + 1):
    if find(i * 2) == find(true_node):
        res.append(0)
    else:
        res.append(1)

print("YES")
print(" ".join(map(str, res)))