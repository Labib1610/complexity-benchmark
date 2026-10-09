n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Precompute for each node and each possible value the contribution
# We'll just compute on the fly.

assignment = [0] * (n + 1)  # 1-indexed

def is_valid(u, val):
    # Check all edges involving u
    for a, b in edges:
        if a == u:
            other = b
            other_val = assignment[other]
            if other_val == 0:
                continue
            f1 = (u * val * val + other * other_val * other_val) % 41
            f2 = (u * other_val * other_val + other * val * val) % 41
            if f1 == f2:
                return False
        elif b == u:
            other = a
            other_val = assignment[other]
            if other_val == 0:
                continue
            f1 = (other * other_val * other_val + u * val * val) % 41
            f2 = (other * val * val + u * other_val * other_val) % 41
            if f1 == f2:
                return False
    return True

def dfs(node):
    if node > n:
        return True
    for val in (1, 2, 3):
        if is_valid(node, val):
            assignment[node] = val
            if dfs(node + 1):
                return True
            assignment[node] = 0
    return False

if dfs(1):
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))
else:
    print("NO")