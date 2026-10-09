from itertools import product

def calculate_load(fu, fv):
    diff = fu - fv
    diff_sq = diff * diff
    return diff_sq * diff_sq - 5 * diff_sq + 10

def is_valid_assignment(n, edges, assignment):
    total_load = 0
    for u, v in edges:
        total_load += calculate_load(assignment[u-1], assignment[v-1])
        if total_load > 6 * len(edges):
            return False
    return total_load <= 6 * len(edges)

def solve():
    n, m = map(int, input().split())
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        if is_valid_assignment(n, edges, assignment):
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()